import pandas as pd
from find_path import get_team_regular_season_path, get_top_players_regular_season_path

def analyze_player_performance(season, player_name):
    # Retrieve paths
    player_logs_path = get_top_players_regular_season_path(season)
    team_logs_path = get_team_regular_season_path(season)

    # Load the regular season data
    try:
        player_logs = pd.read_csv(player_logs_path)
        team_logs = pd.read_csv(team_logs_path)
    except FileNotFoundError as e:
        print(f"Data for season {season} not found: {e}")
        return

    # Filter player-specific data
    player_data = player_logs[player_logs['player_name'] == player_name]

    # Merge with team logs to get the VS_TIER based on GAME_ID and TEAM_ID
    merged_data = pd.merge(
        player_data,
        team_logs[['GAME_ID', 'TEAM_ID', 'VS_TIER']],
        left_on=['Game_ID', 'TEAM_ID'],
        right_on=['GAME_ID', 'TEAM_ID'],
        how='left'
    )

    # Calculate average points per tier
    tier_avg = merged_data.groupby('VS_TIER')['PTS'].mean().sort_index()

    # Display results (for now, print to verify)
    print(f"Averages for {player_name} in season {season}:\n{tier_avg}")

# Example usage:
season = "2002-03"
player_name = "Kobe Bryant"
analyze_player_performance(season, player_name)
