from json import load
import pandas as pd
from team_map import team_mapper

with open('results.json') as fp:
    json_data = load(fp)

if json_data is None:
    quit()

final_data = pd.read_csv('../combine/FinalJoinedData.csv')

df = pd.DataFrame(json_data)
df['team_one'] = df['team_one'].apply(team_mapper)
df['team_two'] = df['team_two'].apply(team_mapper)
df['winner'] = df['winner'].apply(team_mapper)

df['team_one'] = df['team_one'].apply(team_mapper)
df['team_two'] = df['team_two'].apply(team_mapper)
df['winner'] = df['winner'].apply(team_mapper)

for year in df['year'].unique():
    curr_year = df[df['year'] == year]

    teams = set(curr_year['team_one'].unique())
    teams = teams.union(set(curr_year['team_two'].unique()))

    teams_final = set(final_data[final_data['year'] == int(year)]['Team'].unique())
    # if int(year) >= 2000:
    #     print (year)
    #     # print (sorted(teams_final))
    #     print (sorted(teams - teams_final))
    #     print (sorted(teams_final - teams))

print (df.head(10))
print (df.shape)

df.to_csv('Results.csv')