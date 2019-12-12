from json import load
import pandas as pd

with open('results.json') as fp:
    json_data = load(fp)

if json_data is None:
    quit()

df = pd.DataFrame(json_data)

print (df.head())
print (df.shape)

df.to_csv('Results.csv')