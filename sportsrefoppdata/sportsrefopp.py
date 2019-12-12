from json import load
import pandas as pd

with open('sportsrefoppadvanced.json') as fp:
    json_data = load(fp)

year_map = dict()

for row in json_data:
    if row['year'] not in year_map:
        year_map[row['year']] = []
    year_map[row['year']].append(row)

for year, data in year_map.items():
    df = pd.DataFrame(data)

    df.to_csv(str(year) + 'sportsrefoppadvanced.csv')