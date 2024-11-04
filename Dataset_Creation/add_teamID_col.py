import pandas as pd


def add_team_id_to_players(players_path, teams_path):
    player_logs = pd.read_csv(players_path)
    team_logs = pd.read_csv(teams_path)
    # create another column in player_logs
    player_logs['TEAM_ABBREVIATION'] = player_logs['MATCHUP'].str.split().str[0]

    # create a dict with key=team_abb , val=team_id
    team_id_dict = dict(zip(team_logs['TEAM_ABBREVIATION'], team_logs['TEAM_ID']))

    # match the value to the key
    player_logs['TEAM_ID'] = player_logs['TEAM_ABBREVIATION'].map(team_id_dict)

    player_logs.to_csv(players_path, index=False)
