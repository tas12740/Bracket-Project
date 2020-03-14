import pandas as pd
from team_map import map_team_names
from sys import maxsize, exit as sys_exit

start = 2002
end = 2020


def capitalize_and_split(name: str) -> str:
    split = name.split('-')
    split = [s.capitalize() for s in split]
    return ' '.join(split)


def drop_unnamed(df: pd.DataFrame):
    cols_to_drop = []
    for col in df.columns:
        if 'Unnamed' in col:
            cols_to_drop.append(col)
    return df.drop(columns=cols_to_drop)


def convert_height(val):
    if isinstance(val, str):
        vals = val.split('-')
        return int(vals[0])*12+int(vals[1])
    else:
        return val*12


for year in range(start, end+1):
    kenpom_data = pd.read_csv('../kenpomdata/KenPomData' + str(year) + '.csv')
    kenpom_data['Team'] = kenpom_data['Team'].apply(map_team_names)
    kenpom_data['W'] = kenpom_data['W-L'].apply(lambda s: s.split('-')[0])
    kenpom_data['L'] = kenpom_data['W-L'].apply(lambda s: s.split('-')[1])
    kenpom_data.drop(columns=['W-L'], inplace=True)

    kenpom_teams = set(kenpom_data['Team'].unique())

    sports_ref_prefix = '../sportsrefdata/data/' + str(year) + '/'

    sports_ref_team_data = pd.read_csv(
        sports_ref_prefix + 'SportsRefTeamData' + str(year) + '.csv')
    sports_ref_team_data['school_name'] = sports_ref_team_data['school_name'].apply(
        map_team_names)
    sports_ref_team_data = drop_unnamed(sports_ref_team_data)

    sports_ref_teams = set(sports_ref_team_data['school_name'].unique())

    # print(sorted(kenpom_teams - sports_ref_teams))
    # print(sorted(sports_ref_teams - kenpom_teams))

    sports_ref_player_data = pd.read_csv(
        sports_ref_prefix + 'SportsRefPlayerData' + str(year) + '.csv')
    sports_ref_player_data['team_name'] = sports_ref_player_data['team_name'].apply(
        capitalize_and_split)
    sports_ref_player_data['team_name'] = sports_ref_player_data['team_name'].apply(
        map_team_names)
    sports_ref_player_data = drop_unnamed(sports_ref_player_data)

    sports_ref_player_teams = set(sports_ref_player_data['team_name'].unique())

    # print(sorted(kenpom_teams - sports_ref_player_teams))
    # print(sorted(sports_ref_player_teams - kenpom_teams))
    # print(sorted(sports_ref_teams - sports_ref_player_teams))
    # print(sorted(sports_ref_player_teams - sports_ref_teams))

    sports_ref_opp_data = pd.read_csv(
        '../sportsrefoppdata/' + str(year) + 'sportsrefoppadvanced.csv')
    sports_ref_opp_data['school_name'] = sports_ref_opp_data['school_name'].apply(
        map_team_names)
    sports_ref_opp_data = drop_unnamed(sports_ref_opp_data)

    sports_ref_opp_teams = set(sports_ref_opp_data['school_name'].unique())

    # print(sorted(kenpom_teams - sports_ref_opp_teams))
    # print(sorted(sports_ref_opp_teams - kenpom_teams))
    # print(sorted(sports_ref_teams - sports_ref_opp_teams))
    # print(sorted(sports_ref_opp_teams - sports_ref_teams))
    # print(sorted(sports_ref_player_teams - sports_ref_opp_teams))
    # print(sorted(sports_ref_opp_teams - sports_ref_player_teams))

    joined = pd.merge(kenpom_data, sports_ref_team_data,
                      left_on='Team', right_on='school_name')
    columns_to_drop = ['losses', 'g', 'school_name', 'wins', 'Rank']
    joined = joined.drop(columns=columns_to_drop)

    print(joined.shape)

    sports_ref_opp_data.drop(columns=['g', 'wins', 'losses', 'srs', 'sos', 'wins_conf', 'losses_conf',
                                      'wins_home', 'losses_home', 'wins_visitor', 'losses_visitor', 'pts', 'opp_pts', 'year'], inplace=True)
    joined = pd.merge(joined, sports_ref_opp_data,
                      left_on='Team', right_on='school_name')
    columns_to_drop = ['school_name']
    joined = joined.drop(columns=columns_to_drop)

    print(joined.shape)

    columns_to_drop = ['g', 'gs', 'hometown',
                       'number', 'player', 'summary', 'type', 'rsci']
    sports_ref_player_data = sports_ref_player_data.drop(
        columns=columns_to_drop)

    teams = sports_ref_player_data['team_name'].unique()
    teams_data = []
    for team in teams:
        curr_team = sports_ref_player_data[sports_ref_player_data['team_name'] == team]
        curr_data = {}
        by_class = curr_team['class'].value_counts()
        for cla, val in by_class.iteritems():
            curr_data['num_' + cla] = val
        by_pos = curr_team['pos'].value_counts()
        for pos, val in by_pos.iteritems():
            curr_data['num_' + pos] = val

        curr_team = curr_team.drop(columns=['pos', 'class', 'team_name'])
        curr_team['height'] = curr_team['height'].apply(convert_height)

        for col in curr_team.columns:
            # find the tops for each stat - should we limit (say, to 7?)?
            try:
                curr_stat = curr_team.sort_values(by=col, ascending=False)[col]
            except TypeError:
                continue
            i = 1
            for _, val in curr_stat.iteritems():
                curr_data[col + '_' + str(i)] = val
                i += 1

        curr_data['team'] = team

        teams_data.append(curr_data)

    players_df = pd.DataFrame(teams_data)

    joined = pd.merge(joined, players_df, left_on='Team', right_on='team')
    columns_to_drop = ['team', 'win_loss_pct_y', 'win_loss_pct_x']
    joined = joined.drop(columns=columns_to_drop)

    polls = pd.read_csv(f'../pollsdata/{year}Polls.csv', index_col=0)
    polls['school_name'] = polls['school_name'].apply(map_team_names)

    # joined_teams = set(joined['Team'].unique())
    # polls_teams = set(polls['school_name'].unique())
    # print(sorted(joined_teams - polls_teams))
    # print(sorted(polls_teams - joined_teams))

    joined = pd.merge(joined, polls, how='left',
                      left_on='Team', right_on='school_name')
    columns_to_drop = ['school_name', 'Unnamed: 0']
    joined = joined.drop(columns=columns_to_drop)
    # print (joined)

    joined['year'] = year

    joined = joined.fillna(0)
    joined.to_csv(f'joined-data/{year}JoinedData.csv')
    print(f'{year} Done! {joined.shape}')
