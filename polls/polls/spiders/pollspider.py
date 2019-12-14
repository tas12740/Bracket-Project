import scrapy
from bs4 import BeautifulSoup as BS
from re import findall

class PollSpider(scrapy.Spider):
    name="polls"
    start_urls = [f'https://www.sports-reference.com/cbb/seasons/{yr}-polls.html' for yr in range(2002, 2020)]

    def parse(self, response):
        year = response.url.split('/')[-1][0:4]

        tbody = response.css('tbody')

        for tr in tbody.css('tr'):
            if tr.attrib.get('class') and 'thead' in tr.attrib.get('class'): 
                continue
            curr_data = dict()
            curr_data['year'] = year
            school_name = tr.css('th>a::text').get()
            curr_data['school_name'] = school_name

            for td in tr.css('td'):
                stat = td.attrib['data-stat']
                if stat == 'conf':
                    continue
                soup = BS(td.extract())
                text = soup.get_text()
                # if not text.strip():
                #     text = '-1'
                curr_data[stat] = text
            
            yield curr_data