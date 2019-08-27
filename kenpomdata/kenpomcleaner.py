import pandas as pd
import numpy as np
import json

data_dict = dict()
kenpom_json_file = open('../kenpom/kenpom.json', 'r')
kenpom_data = json.load(kenpom_json_file)
firstrow = kenpom_data[0]

for row in kenpom_data:
    year = row['Year']
    if data_dict.get(year) is None:
        data_dict[year] = np.array([[]])
    vals = list(row.values())
    data_dict[year] = np.append(data_dict[year], np.array(list(row.values())))

numvals = len(firstrow.keys())

for k, v in data_dict.items():
    vals = v.reshape(v.shape[0]//numvals, numvals)
    df = pd.DataFrame(data=vals,columns=list(firstrow.keys()))
    df.set_index(keys='Rank',inplace=True)
    year = df['Year'].unique()
    df.drop(columns=['Year'],inplace=True)
    filename = 'KenPomData{}.csv'.format(year[0])
    df.to_csv(filename)

kenpom_json_file.close()