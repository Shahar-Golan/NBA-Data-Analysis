import os
import pandas as pd
from find_path import (get_top_players_regular_season_path,
                       get_team_regular_season_path)

def load_player_names(season):
    # get the path to the top 100 players
    regular_season_path = get_top_players_regular_season_path(season)

    if os.path.exists(regular_season_path):
        # convert to pd
        player_df = pd.read_csv(regular_season_path)
        # Calculate PPG and sort players by descending PPG
        player_ppg = player_df.groupby('player_name')['PTS'].mean().sort_values(ascending=False).reset_index()
        return player_ppg['player_name'].tolist()
    else:
        print(f"File not found for season: {season}")
        return []

def get_player_data(season, player_name):
    # get the neccesery files
    player_logs_path = get_top_players_regular_season_path(season)
    team_logs_path = get_team_regular_season_path(season)

    try:
        player_logs = pd.read_csv(player_logs_path)
        team_logs = pd.read_csv(team_logs_path)
    except FileNotFoundError:
        print(f"Data for season {season} not found.")
        return None, None

    # Filter player data
    player_data = player_logs[player_logs['player_name'] == player_name]
    # Merge to get opponent's tier based on TEAM_ID and GAME_ID
    player_data = player_data.merge(
        team_logs[['GAME_ID', 'TEAM_ID', 'VS_TIER']],
        left_on=['Game_ID', 'TEAM_ID'],
        right_on=['GAME_ID', 'TEAM_ID'],
        how='left'
    )
    # return a df of the primary key
    return player_data

