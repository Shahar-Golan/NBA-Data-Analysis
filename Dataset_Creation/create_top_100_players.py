import pandas as pd
import os

def top_100_players(advanced_path, playoffs_teams_path, player_logs_path, season, save_path=""):

    player_adv = pd.read_csv(advanced_path)
    playoff_teams = pd.read_csv(playoffs_teams_path)
    player_logs = pd.read_csv(player_logs_path)


    teams_ids = playoff_teams['TEAM_ID'].tolist()


    # filter the data set
    filtered_players_by_min = (
        player_adv[player_adv['GP'] >= 20]
        .sort_values(by='MIN', ascending=False)
        .head(100)['PLAYER_ID']
        .tolist()
    )


    top_100_players_info_regular_season = player_logs[
        player_logs['Player_ID'].isin(filtered_players_by_min) &
        player_logs['TEAM_ID'].isin(teams_ids)
    ]

    os.makedirs(save_path, exist_ok=True)
    output_path = os.path.join(save_path, f'top_100_players_info_regular_season_{season}.csv')

    # Save the filtered data to CSV
    top_100_players_info_regular_season.to_csv(output_path, index=False)
    print(f"Top 100 players data saved to {output_path}")

    return output_path