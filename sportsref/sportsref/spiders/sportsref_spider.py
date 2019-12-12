import scrapy

class SportsRefTeamSpider(scrapy.Spider):
    name="sportsref"
    start_urls = ['https://www.sports-reference.com/cbb/seasons/' + str(yr) + '-advanced-school-stats.html' for yr in range(2002, 2020)]
    
    def parse(self, response):
        year = int(response.url.split('/')[-1].split('-')[0])
        for tr in response.css('tr'):
            ncaa = tr.css('small').getall()
            if len(ncaa) == 0:
                # only get the stats of NCAA tournament teams
                continue
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
            row['is_team_stats'] = False
            yield row

            if link is not None:
                yield response.follow(link, callback=self.parse_players)

    def parse_players(self, response):
        year = int(response.url.split('/')[-1].split('.')[0])
        team_name = response.url.split('/')[-2]
        tables = response.css('table')
        for table in tables:
            tbody = table.css('tbody')
            table_id = table.attrib['id']
            for tr in tbody.css('tr'):
                row = dict()
                for td in tr.css('td'):
                    # link = None
                    stat = td.attrib['data-stat']
                    atext = td.css('a::text').get()
                    if atext is not None:
                        # link = td.css('a').attrib['href']
                        row[stat] = atext
                    else:
                        tdtext = td.css('td::text').get()
                        if tdtext is None or len(tdtext) == 0:
                            continue
                        row[stat] = tdtext
                row['year'] = year
                row['type'] = table_id
                if len(tr.css('th').css('a').getall()) > 0:
                    player_name = tr.css('th').css('a::text').get()
                    row['player'] = player_name
                row['is_player'] = False if table_id == 'team_stats' else True
                row['team_name'] = team_name
                yield row


class SportsRefOpponentSpider(scrapy.Spider):
    name="sportsrefoppadvanced"
    start_urls = ['https://www.sports-reference.com/cbb/seasons/' + str(yr) + '-advanced-opponent-stats.html' for yr in range(2002, 2020)]

    def parse(self, response):
        year = int(response.url.split('/')[-1].split('-')[0])
        for tr in response.css('tr'):
            ncaa = tr.css('td.left::text').get()
            if not ncaa:
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