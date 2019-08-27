import scrapy
from selenium import webdriver

class SportsRefTeamSpider(scrapy.Spider):
    name="sportsref"
    start_urls = ['https://www.sports-reference.com/cbb/seasons/' + str(y) + '-advanced-school-stats.html' for y in range(2002, 2020)]
    
    def parse(self, response):
        year = int(response.url.split('/')[-1].split('-')[0])
        for tr in response.css('tr'):
            ncaa = tr.css('small').getall()
            if len(ncaa) == 0:
                continue
            # only get the stats of NCAA tournament teams
            row = {}
            for td in tr.css('td'):
                stat = td.attrib['data-stat']
                if stat == 'x':
                    continue
                atext = td.css('a::text').get()
                if atext is not None:
                    link = td.css('a').attrib['href']
                    row[stat] = atext
                else:
                    tdtext = td.css('td::text').get()
                    row[stat] = tdtext
            row['year'] = year
            yield row

            if link is not None:
                yield response.follow(link, callback=self.parse_players)

    def parse_players(self, response):
        year = int(response.url.split('/')[-1].split('.')[0])
        tables = response.css('table')
        for table in tables:
            tbody = table.css('tbody')
            id = table.attrib['id']
            for tr in tbody.css('tr'):
                row = dict()
                for td in tr.css('td'):
                    link = None
                    stat = td.attrib['data-stat']
                    atext = td.css('a::text').get()
                    if atext is not None:
                        link = td.css('a').attrib['href']
                        row[stat] = atext
                    else:
                        tdtext = td.css('td::text').get()
                        if tdtext is None or len(tdtext) == 0:
                            continue
                        row[stat] = tdtext
                    row['year'] = year
                    row['type'] = id
                    if link is not None:
                        yield response.follow(link, callback=self.parse_player)
                if id =='roster':
                    player_name = tr.css('th').css('a::text').get()
                    row['player'] = player_name
                yield row


    def parse_player(self, response):
        player_name = response.url.split('/')[-1].split('.')[0]
        player_name = self.convert_player_name(player_name)
        tables = response.css('table')
        for table in tables:
            id = table.attrib['id']
            tbody = table.css('tbody')
            for tr in tbody.css('tr'):
                row = dict()
                for td in tr.css('td'):
                    stat = td.attrib['data-stat']
                    atext = td.css('a::text').get()
                    if atext is not None:
                        row[stat] = atext
                    else:
                        tdtext = td.css('td::text').get()
                        if tdtext is None or len(tdtext) == 0:
                            continue
                        row[stat] = tdtext
                season = tr.css('th').css('a::text').get()
                row['season'] = season
                row['type'] = id
                row['player'] = player_name
                yield row

    def convert_player_name(self, name):
        parts = name.split('-')
        try:
            int(parts[-1])
            return ' '.join(parts[0:-1]).title()
        except:
            return ' '.join(parts).title()


class SportsRefOpponentSpider(scrapy.Spider):
    name="sportsrefoppadvanced"
    start_urls = ['https://www.sports-reference.com/cbb/seasons/' + str(y) + '-advanced-opponent-stats.html' for y in range(2002, 2020)]

    def parse(self, response):
        year = int(response.url.split('/')[-1].split('-')[0])
        for tr in response.css('tr'):
            ncaa = tr.css('small').getall()
            if len(ncaa) == 0:
                continue
            # only get the stats of NCAA tournament teams
            row = {}
            for td in tr.css('td'):
                stat = td.attrib['data-stat']
                if stat == 'x':
                    continue
                atext = td.css('a::text').get()
                if atext is not None:
                    row[stat] = atext
                else:
                    tdtext = td.css('td::text').get()
                    row[stat] = tdtext
            row['year'] = year
            yield row