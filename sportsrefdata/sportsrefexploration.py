from json import load
import pandas as pd

with open('sportsref.json') as fp:
    json_data = load(fp)

if json_data is None:
    quit()

different_structures_player = set()
different_structures_team_stats = set()
different_structures_team_player = set()

for row in json_data:
    keys = tuple(sorted(row.keys()))
    if 'is_team_stats' in keys:
        different_structures_team_stats.add(keys)
    elif 'is_player' in keys:
        if row['is_player']:
            different_structures_player.add(keys)
        else:
            different_structures_team_player.add(keys)

print(f'There are {len(different_structures_player)}, {len(different_structures_team_stats)}, {len(different_structures_team_player)} different structures')

unique_player_keys = set()
for struct in different_structures_player:
    for key in struct:
        unique_player_keys.add(key)

print('Player keys: {}'.format(sorted(unique_player_keys)))

unique_team_player_keys = set()
for struct in different_structures_team_player:
    for key in struct:
        unique_team_player_keys.add(key)

print('Player team keys: {}'.format(sorted(unique_team_player_keys)))

unique_team_keys = set()
for struct in different_structures_team_stats:
    for key in struct:
        unique_team_keys.add(key)

print('Team keys: {}'.format(sorted(unique_team_keys)))

player_dict = dict()
team_stats_dict = dict()
team_stats_player_dict = dict()


def is_player(row):
    keys = row.keys()
    return len(list(filter(lambda k: k in unique_player_keys, keys))) == len(keys)


def is_team_stats(row):
    keys = row.keys()
    return len(list(filter(lambda k: k in unique_team_keys, keys))) == len(keys)


def is_team_player_stats(row):
    keys = row.keys()
    return len(list(filter(lambda k: k in unique_team_player_keys, keys))) == len(keys)


for row in json_data:
    if is_team_player_stats(row):
        year = row['year']
        del row['year']
        del row['is_player']
        if year not in team_stats_player_dict:
            team_stats_player_dict[year] = dict()
        team_stats_player_dict[year][row['team_name']] = row
        del team_stats_player_dict[year][row['team_name']]['team_name']
    elif is_player(row):
        year = row['year']
        del row['year']
        del row['is_player']
        if year not in player_dict:
            player_dict[year] = dict()
        player_name = row['player']
        del row['player']
        if player_name not in player_dict[year]:
            player_dict[year][player_name] = row
        else:
            for key, val in row.items():
                player_dict[year][player_name][key] = val
    elif is_team_stats(row):
        year = row['year']
        school_name = row['school_name']
        del row['year']
        del row['school_name']
        del row['is_team_stats']
        if year not in team_stats_dict:
            team_stats_dict[year] = dict()
        if school_name not in team_stats_dict[year]:
            team_stats_dict[year][school_name] = row
        else:
            for key, val in row.items():
                team_stats_dict[year][school_name][key] = val

dicts = [player_dict, team_stats_dict, team_stats_player_dict]

# for d in dicts:
#     for year in sorted(d.keys()):
#         print (f'Year {year}: {len(d[year].values())}')

player_cols = sorted(list(unique_player_keys))
player_cols.remove('year')
player_cols.remove('is_player')

for year, players in player_dict.items():
    new_player_list = []
    for player_name, info in players.items():
        new_player = dict()
        new_player['player'] = player_name
        for k, v in info.items():
            new_player[k] = v
        new_player_list.append(new_player)
    player_df = pd.DataFrame(new_player_list, columns=player_cols)
    player_df.dropna(axis=1, how='all', inplace=True)
    # print(player_df.shape)
    # print (player_df.head())
    player_df.to_csv('SportsRefPlayerData{}.csv'.format(year))

team_cols = sorted(list(unique_team_keys))
team_cols.remove('year')
team_cols.remove('is_team_stats')

for year, team in team_stats_dict.items():
    new_team_list = []
    for team_name, info in team.items():
        new_team = dict()
        new_team['school_name'] = team_name
        for k, v in info.items():
            new_team[k] = v
        new_team_list.append(new_team)
    team_df = pd.DataFrame(new_team_list, columns=team_cols)
    team_df.dropna(axis=1, how='all', inplace=True)
    # print (team_df.shape)
    # print (team_df.head())
    team_df.to_csv('SportsRefTeamData{}.csv'.format(year))

team_player_cols = sorted(list(unique_team_player_keys))
team_player_cols.remove('year')
team_player_cols.remove('is_player')

for year, team in team_stats_player_dict.items():
    new_list = []
    for team_name, info in team.items():
        new_team = dict()
        new_team['team_name'] = team_name
        for k, v in info.items():
            new_team[k] = v
        new_list.append(new_team)
    team_df = pd.DataFrame(new_list, columns=team_player_cols)
    team_df.dropna(axis=1, how='all', inplace=True)
    # print (year, team_df.shape)
    # print (team_df.head())
    team_df.to_csv('SportsRefTeamDataFromPlayerPage{}.csv'.format(year))
