import pandas as pd
import numpy as np
import json

def is_match(row, keys, keys_match):
    for key in keys_match:
        if key not in keys:
            return False
    return len(keys) == len(keys_match)

def is_schooldata(row):
    keys = list(row.keys())
    keys_match = ['school_name', 'g', 'wins', 'losses', 'win_loss_pct', 'srs', 'sos', 'wins_conf', 'losses_conf', 'wins_home', 'losses_home', 'wins_visitor', 'losses_visitor', 'pts', 'opp_pts', 'pace', 'off_rtg', 'fta_per_fga_pct', 'fg3a_per_fga_pct', 'ts_pct', 'trb_pct', 'ast_pct', 'stl_pct', 'blk_pct', 'efg_pct', 'tov_pct', 'orb_pct', 'ft_rate', 'year']
    return is_match(row, keys, keys_match)

def is_playerbasicdata(row):
    keys = list(row.keys())
    keys_matches = []
    keys_matches.append(['number', 'year', 'type', 'class', 'pos', 'height', 'weight', 'hometown', 'summary', 'player'])
    keys_matches.append(['number', 'year', 'type', 'class', 'pos', 'height', 'weight', 'rsci', 'summary', 'player'])
    keys_matches.append(['number', 'year', 'type', 'class', 'pos', 'height', 'weight', 'summary', 'player'])
    keys_matches.append(['number', 'year', 'type', 'class', 'height', 'weight', 'hometown', 'summary', 'player'])
    keys_matches.append(['class', 'year', 'type', 'pos', 'height', 'weight', 'summary', 'player'])
    keys_matches.append(['number', 'year', 'type', 'class', 'weight', 'hometown', 'summary', 'player'])
    keys_matches.append(['class', 'year', 'type', 'pos', 'high_school', 'summary', 'player'])
    keys_matches.append(['number', 'year', 'type', 'pos', 'height', 'weight', 'hometown', 'high_school', 'summary', 'player'])
    keys_matches.append(['number', 'year', 'type', 'pos', 'height', 'weight', 'hometown', 'summary', 'player'])
    keys_matches.append(['number', 'year', 'type', 'class', 'pos', 'height', 'weight', 'hometown', 'rsci', 'summary', 'player'])
    keys_matches.append(['number', 'year', 'type', 'class', 'pos', 'weight', 'hometown', 'summary', 'player'])
    keys_matches.append(['number', 'year', 'type', 'class', 'pos', 'height', 'weight', 'hometown', 'high_school', 'summary', 'player'])
    for poss in keys_matches:
        res = is_match(row, keys, poss)
        if res:
            return res
    return False

def is_teamdata(row):
    keys = list(row.keys())
    keys_matches = []
    keys_match = ['g', 'year', 'type', 'fg', 'fga', 'fg_pct', 'fg2', 'fg2a', 'fg2_pct', 'fg3', 'fg3a', 'fg3_pct', 'ft', 'fta', 'ft_pct', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pts', 'pts_per_g']
    keys_matches.append(keys_match)
    keys_matches.append(['g', 'year', 'type', 'mp', 'fg', 'fga', 'fg_pct', 'fg2', 'fg2a', 'fg2_pct', 'fg3', 'fg3a', 'fg3_pct', 'ft', 'fta', 'ft_pct', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pts', 'pts_per_g'])
    keys_matches.append(['g', 'year', 'type', 'mp', 'opp_fg', 'opp_fga', 'opp_fg_pct', 'opp_trb', 'opp_pts', 'opp_pts_per_g'])
    keys_matches.append(['g', 'year', 'type', 'mp', 'fg', 'fga', 'fg_pct', 'fg2', 'fg2a', 'fg2_pct', 'fg3', 'fg3a', 'fg3_pct', 'ft', 'fta', 'ft_pct', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf', 'pts', 'pts_per_g'])
    keys_matches.append(['fg', 'year', 'type', 'fga', 'fg_pct', 'fg2', 'fg2a', 'fg2_pct', 'fg3', 'fg3a', 'fg3_pct', 'ft', 'fta', 'ft_pct', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf', 'pts', 'pts_per_g'])
    keys_matches.append(['g', 'year', 'type', 'mp', 'opp_fg', 'opp_fga', 'opp_fg_pct', 'opp_fg2', 'opp_fg2a', 'opp_fg2_pct', 'opp_fg3', 'opp_fg3a', 'opp_fg3_pct', 'opp_ft', 'opp_fta', 'opp_ft_pct', 'opp_orb', 'opp_drb', 'opp_trb', 'opp_ast', 'opp_stl', 'opp_blk', 'opp_tov', 'opp_pf', 'opp_pts', 'opp_pts_per_g'])
    for poss in keys_matches:
        res = is_match(row, keys, poss)
        if res:
            return res
    return False

def is_teamranks(row):
    keys = list(row.keys())
    keys_match = ['fg', 'year', 'type', 'fga', 'fg_pct', 'fg2', 'fg2a', 'fg2_pct', 'fg3', 'fg3a', 'fg3_pct', 'ft', 'fta', 'ft_pct', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pts', 'pts_per_g']
    keys_match_opp = ['opp_fg', 'year', 'type', 'opp_fga', 'opp_fg_pct', 'opp_trb', 'opp_pts', 'opp_pts_per_g']
    keys_match_opp2 = ['opp_fg', 'year', 'type', 'opp_fga', 'opp_fg_pct', 'opp_fg2', 'opp_fg2a', 'opp_fg2_pct', 'opp_fg3', 'opp_fg3a', 'opp_fg3_pct', 'opp_ft', 'opp_fta', 'opp_ft_pct', 'opp_orb', 'opp_drb', 'opp_trb', 'opp_ast', 'opp_stl', 'opp_blk', 'opp_tov', 'opp_pf', 'opp_pts', 'opp_pts_per_g']
    return is_match(row, keys, keys_match) or is_match(row, keys, keys_match_opp) or is_match(row, keys, keys_match_opp2)

def is_oppdatabasic(row):
    keys = list(row.keys())
    keys_match = ['g', 'year', 'type', 'opp_fg', 'opp_fga', 'opp_fg_pct', 'opp_trb', 'opp_pts', 'opp_pts_per_g']
    return is_match(row, keys, keys_match)

def is_pergamestats(row):
    keys = list(row.keys())
    keys_matches = []
    keys_matches.append(['player', 'year', 'type', 'g', 'gs', 'mp_per_g', 'fg_per_g', 'fga_per_g', 'fg_pct', 'fg2_per_g', 'fg2a_per_g', 'fg2_pct', 'fg3_per_g', 'fg3a_per_g', 'fg3_pct', 'ft_per_g', 'fta_per_g', 'ft_pct', 'orb_per_g', 'drb_per_g', 'trb_per_g', 'ast_per_g', 'stl_per_g', 'blk_per_g', 'tov_per_g', 'pf_per_g', 'pts_per_g'])
    keys_matches.append(['player', 'year', 'type', 'g', 'gs', 'mp_per_g', 'fg_per_g', 'fga_per_g', 'fg_pct', 'fg2_per_g', 'fg2a_per_g', 'fg2_pct', 'fg3_per_g', 'fg3a_per_g', 'ft_per_g', 'fta_per_g', 'ft_pct', 'orb_per_g', 'drb_per_g', 'trb_per_g', 'ast_per_g', 'stl_per_g', 'blk_per_g', 'tov_per_g', 'pf_per_g', 'pts_per_g'])
    keys_matches.append(['player', 'year', 'type', 'g', 'gs', 'mp_per_g', 'fg_per_g', 'fga_per_g', 'fg_pct', 'fg2_per_g', 'fg2a_per_g', 'fg2_pct', 'fg3_per_g', 'fg3a_per_g', 'fg3_pct', 'ft_per_g', 'fta_per_g', 'orb_per_g', 'drb_per_g', 'trb_per_g', 'ast_per_g', 'stl_per_g', 'blk_per_g', 'tov_per_g', 'pf_per_g', 'pts_per_g'])
    keys_matches.append(['player', 'year', 'type', 'g', 'gs', 'fg_per_g', 'fga_per_g', 'fg2_per_g', 'fg2a_per_g', 'fg3_per_g', 'fg3a_per_g', 'ft_per_g', 'fta_per_g', 'orb_per_g', 'drb_per_g', 'trb_per_g', 'ast_per_g', 'stl_per_g', 'blk_per_g', 'tov_per_g', 'pf_per_g', 'pts_per_g'])
    keys_matches.append(['player', 'year', 'type', 'g', 'fg_per_g', 'fga_per_g', 'fg_pct', 'fg2_per_g', 'fg2a_per_g', 'fg2_pct', 'fg3_per_g', 'fg3a_per_g', 'fg3_pct', 'ft_per_g', 'fta_per_g', 'ft_pct', 'trb_per_g', 'ast_per_g', 'stl_per_g', 'blk_per_g', 'pts_per_g'])
    keys_matches.append(['player', 'year', 'type', 'g', 'fg_per_g', 'fga_per_g', 'fg_pct', 'fg2_per_g', 'fg2a_per_g', 'fg2_pct', 'fg3_per_g', 'fg3a_per_g', 'fg3_pct', 'ft_per_g', 'fta_per_g', 'ft_pct', 'trb_per_g', 'ast_per_g', 'stl_per_g', 'blk_per_g', 'pts_per_g'])
    keys_matches.append(['player', 'year', 'type', 'g', 'fg_per_g', 'fga_per_g', 'fg_pct', 'fg2_per_g', 'fg2a_per_g', 'fg2_pct', 'fg3_per_g', 'fg3a_per_g', 'ft_per_g', 'fta_per_g', 'ft_pct', 'trb_per_g', 'ast_per_g', 'stl_per_g', 'blk_per_g', 'pts_per_g'])
    keys_matches.append(['player', 'schools', 'years', 'g', 'gs', 'mp', 'fg', 'fga', 'fg3', 'fg3a', 'ft', 'fta', 'orb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf', 'pts', 'trb_per_g', 'ast_per_g', 'pts_per_g', 'ws', 'season', 'type'])
    keys_matches.append(['player', 'year', 'type', 'g', 'gs', 'mp_per_g', 'fg_per_g', 'fga_per_g', 'fg_pct', 'fg2_per_g', 'fg2a_per_g', 'fg2_pct', 'fg3_per_g', 'fg3a_per_g', 'ft_per_g', 'fta_per_g', 'orb_per_g', 'drb_per_g', 'trb_per_g', 'ast_per_g', 'stl_per_g', 'blk_per_g', 'tov_per_g', 'pf_per_g', 'pts_per_g'])
    keys_matches.append(['player', 'year', 'type', 'g', 'gs', 'mp_per_g', 'fg_per_g', 'fga_per_g', 'fg_pct', 'fg2_per_g', 'fg2a_per_g', 'fg3_per_g', 'fg3a_per_g', 'fg3_pct', 'ft_per_g', 'fta_per_g', 'orb_per_g', 'drb_per_g', 'trb_per_g', 'ast_per_g', 'stl_per_g', 'blk_per_g', 'tov_per_g', 'pf_per_g', 'pts_per_g'])
    for poss in keys_matches:
        res = is_match(row, keys, poss)
        if res:
            return True
    return False

def is_playerdata(row):
    keys = list(row.keys())
    keys_matches = []
    keys_matches.append(['school_name', 'conf_abbr', 'g', 'gs', 'mp_per_g', 'fg_per_g', 'fga_per_g', 'fg_pct', 'fg2_per_g', 'fg2a_per_g', 'fg2_pct', 'fg3_per_g', 'fg3a_per_g', 'ft_per_g', 'fta_per_g', 'ft_pct', 'orb_per_g', 'drb_per_g', 'trb_per_g', 'ast_per_g', 'stl_per_g', 'blk_per_g', 'tov_per_g', 'pf_per_g', 'pts_per_g', 'sos', 'season', 'type', 'player'])
    keys_matches.append(['school_name', 'conf_abbr', 'g', 'gs', 'mp_per_g', 'fg_per_g', 'fga_per_g', 'fg2_per_g', 'fg2a_per_g', 'fg3_per_g', 'fg3a_per_g', 'ft_per_g', 'fta_per_g', 'orb_per_g', 'drb_per_g', 'trb_per_g', 'ast_per_g', 'stl_per_g', 'blk_per_g', 'tov_per_g', 'pf_per_g', 'pts_per_g', 'sos', 'season', 'type', 'player'])
    keys_matches.append(['player', 'schools', 'years', 'g', 'gs', 'mp', 'fg', 'fga', 'fg_pct', 'fg3', 'fg3a', 'fg3_pct', 'ft', 'fta', 'ft_pct', 'orb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf', 'pts', 'trb_per_g', 'ast_per_g', 'pts_per_g', 'efg_pct', 'ws', 'season', 'type'])
    keys_matches.append(['player', 'schools', 'years', 'g', 'gs', 'mp', 'fg', 'fga', 'fg_pct', 'fg3', 'fg3a', 'ft', 'fta', 'ft_pct', 'orb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf', 'pts', 'trb_per_g', 'ast_per_g', 'pts_per_g', 'efg_pct', 'ws', 'season', 'type'])
    keys_matches.append(['school_name', 'conf_abbr', 'g', 'gs', 'fg_per_g', 'fga_per_g', 'fg_pct', 'fg2_per_g', 'fg2a_per_g', 'fg2_pct', 'fg3_per_g', 'fg3a_per_g', 'ft_per_g', 'fta_per_g', 'orb_per_g', 'drb_per_g', 'trb_per_g', 'ast_per_g', 'stl_per_g', 'blk_per_g', 'tov_per_g', 'pf_per_g', 'pts_per_g', 'sos', 'season', 'type', 'player'])
    keys_matches.append(['school_name', 'conf_abbr', 'g', 'fg_per_g', 'fga_per_g', 'fg_pct', 'fg2_per_g', 'fg2a_per_g', 'fg2_pct', 'fg3_per_g', 'fg3a_per_g', 'fg3_pct', 'ft_per_g', 'fta_per_g', 'ft_pct', 'trb_per_g', 'ast_per_g', 'stl_per_g', 'blk_per_g', 'pts_per_g', 'sos', 'season', 'type', 'player'])
    keys_matches.append(['school_name', 'conf_abbr', 'g', 'gs', 'mp_per_g', 'fg_per_g', 'fga_per_g', 'fg_pct', 'fg2_per_g', 'fg2a_per_g', 'fg2_pct', 'fg3_per_g', 'fg3a_per_g', 'ft_per_g', 'fta_per_g', 'ft_pct', 'orb_per_g', 'drb_per_g', 'trb_per_g', 'ast_per_g', 'stl_per_g', 'blk_per_g', 'tov_per_g', 'pf_per_g', 'pts_per_g', 'season', 'type', 'player'])
    keys_matches.append(['school_name', 'conf_abbr', 'g', 'fg_per_g', 'fga_per_g', 'fg_pct', 'fg2_per_g', 'fg2a_per_g', 'fg2_pct', 'fg3_per_g', 'fg3a_per_g', 'fg3_pct', 'ft_per_g', 'fta_per_g', 'trb_per_g', 'ast_per_g', 'stl_per_g', 'blk_per_g', 'pts_per_g', 'sos', 'season', 'type', 'player'])
    keys_matches.append(['school_name', 'conf_abbr', 'g', 'gs', 'fg_per_g', 'fga_per_g', 'fg2_per_g', 'fg2a_per_g', 'fg3_per_g', 'fg3a_per_g', 'ft_per_g', 'fta_per_g', 'orb_per_g', 'drb_per_g', 'trb_per_g', 'ast_per_g', 'stl_per_g', 'blk_per_g', 'tov_per_g', 'pf_per_g', 'pts_per_g', 'sos', 'season', 'type', 'player'])
    keys_matches.append(['school_name', 'conf_abbr', 'g', 'mp_per_g', 'fg_per_g', 'fga_per_g', 'fg_pct', 'fg2_per_g', 'fg2a_per_g', 'fg2_pct', 'fg3_per_g', 'fg3a_per_g', 'ft_per_g', 'fta_per_g', 'ft_pct', 'trb_per_g', 'ast_per_g', 'stl_per_g', 'blk_per_g', 'tov_per_g', 'pf_per_g', 'pts_per_g', 'sos', 'season', 'type', 'player'])
    keys_matches.append(['player', 'year', 'type', 'g', 'gs', 'mp_per_g', 'fg_per_g', 'fga_per_g', 'fg2_per_g', 'fg2a_per_g', 'fg3_per_g', 'fg3a_per_g', 'ft_per_g', 'fta_per_g', 'orb_per_g', 'drb_per_g', 'trb_per_g', 'ast_per_g', 'stl_per_g', 'blk_per_g', 'tov_per_g', 'pf_per_g', 'pts_per_g'])
    for poss in keys_matches:
        res = is_match(row, keys, poss)
        if res:
            return True
    return False

def is_anomalous(row):
    keys = list(row.keys())
    keys_match = ['player', 'season', 'type']
    return len(keys) == len(keys_match) and is_match(row, keys, keys_match)

f = open('../sportsref/sportsref.json', 'r')
sportsref_data = json.load(f)

count = 0
for row in sportsref_data:
    count += 1
    if is_anomalous(row):
        continue
    if is_schooldata(row):
        # handle school data
        continue
    if is_playerbasicdata(row):
        # handle player basic data
        continue
    if is_teamdata(row):
        # handle team data
        continue
    if is_teamranks(row):
        # skip
        continue
    if is_oppdatabasic(row):
        continue
    if is_pergamestats(row):
        continue
    if is_playerdata(row):
        continue
    print (list(row.keys()))
    print (row.items())
    break
print ('Done!', count)