import pandas as pd
from json import load

with open('kenpom.json') as fp:
    kenpom_json = load(fp)

if kenpom_json is None:
    quit()

data_dict = dict()
for row in kenpom_json:
    year = row['Year']
    if year not in data_dict:
        data_dict[year] = []
    data_dict[year].append(row)

for year, val in data_dict.items():
    df = pd.DataFrame(val)
    df.drop(columns=['Year'], inplace=True)
    df.to_csv(f'KenpomData{year}.csv')