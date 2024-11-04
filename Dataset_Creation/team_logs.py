from nba_api.stats.endpoints import leaguegamelog
import pandas as pd
import os


def fetch_and_save_team_game_logs(season, season_type, save_path):
    try:
        # Fetch team game logs based on season type
        team_logs = leaguegamelog.LeagueGameLog(season=season, season_type_all_star=season_type)
        team_logs_df = team_logs.get_data_frames()[0]

        # Generate filename and save the CSV
        filename = f'team_game_logs_{season}_{season_type.replace(" ", "_").lower()}.csv'
        output_path = os.path.join(save_path, filename)
        os.makedirs(save_path, exist_ok=True)  # Ensure save_path exists
        team_logs_df.to_csv(output_path, index=False)
        print(f"Saved team game logs for {season_type} {season} to {output_path}.")
    except Exception as e:
        print(f"Error fetching team game logs for {season_type} in season {season}: {e}")
        output_path = None

    return output_path
