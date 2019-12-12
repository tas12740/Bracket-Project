import scrapy
from bs4 import BeautifulSoup as BS
from re import findall

class ResultsSpider(scrapy.Spider):
    name="results"
    start_urls = [f'https://www.collegerpi.com/subs/tournament/{yr}bracket.html' for yr in range(2002, 2020)]

    def parse(self, response):
        year = response.url.split('/')[-1][0:4]

        for tr in response.css('tr'):
            tds = tr.css('td')
            
            for td in tds:
                curr_data = dict(
                    year=year
                )

                curr_td = BS(td.extract(), features='lxml')

                winner = curr_td.find_all('b')
                
                if not winner:
                    continue
                winner = winner[0]

                text = winner.getText()
                if not text.strip():
                    continue

                winner = text.strip()
                winner = ' '.join(winner.split()[1:-1])

                curr_data['winner'] = winner
                
                text = findall(r'\S+', curr_td.getText())

                teams = []
                curr_item = ''
                for item in text[1:]:
                    try:
                        int(item)
                        teams.append(curr_item)
                        curr_item = ''
                    except ValueError:
                        curr_item = curr_item + ' ' + item
                
                teams = [s.strip() for s in teams]

                curr_data['team_one'] = teams[0]
                curr_data['team_two'] = teams[1]
                yield curr_data
                
