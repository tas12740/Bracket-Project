import scrapy

class KenPomSpider(scrapy.Spider):
    name="kenpom"
    start_urls = ['https://kenpom.com/index.php?y=' + str(x) for x in range(2002, 2020)]
    
    def parse(self, response):
        year = response.url.split('=')[1]
        for tr in response.css('tr'):
            classes = tr.xpath('@class').getall()
            if 'thead1' in classes or 'thead2' in classes:
                continue
            seeds = len(tr.css('span.seed').getall())
            if seeds != 9:
                continue
            tds = tr.xpath('td')
            data = []
            for td in tds:
                atext = td.css('a::text').get()
                if atext is not None:
                    data.append(atext)
                else:
                    tdtext = td.css('td::text').get()
                    if tdtext is not None:
                        data.append(tdtext)
            yield {
                'Rank' : float(data[0]),
                'Team' : data[1],
                'Conference' : data[2],
                'W-L' : data[3],
                'AdjEM' : float(data[4]),
                'AdjO' : float(data[5]),
                'AdjD' : float(data[6]),
                'AdjT' : float(data[7]),
                'Luck' : float(data[8]),
                'Opp AdjEM' : float(data[9]),
                'OppO' : float(data[10]),
                'OppD' : float(data[11]),
                'NCSOS AdjEM' : float(data[12]),
                'Year' : int(year)
            }