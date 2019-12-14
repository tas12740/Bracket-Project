from json import load
import pandas as pd
from sys import maxsize

with open('polls.json') as fp:
    json_data = load(fp)

if json_data is None:
    quit()

df = pd.DataFrame(json_data)

for year in df['year'].unique():
    curr_year = df[df['year'] == year]

    curr_year.dropna(axis=1, how='all', inplace=True)

    curr_year = curr_year.replace(r'^\s*$', maxsize, regex=True)

    cols = list(curr_year.columns)
    cols.remove('year')
    cols.remove('school_name')

    curr_year[cols] = curr_year[cols].astype(dtype='int')

    curr_year['max'] = curr_year[curr_year[cols] > 0].min(axis=1)
    curr_year['final'] = curr_year[cols[-1]]

    cols += ['max', 'final']

    curr_year[cols] = curr_year[cols].astype(dtype='int')

    print (curr_year.head())

    curr_year.to_csv(f'{year}Polls.csv')