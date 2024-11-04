from nba_api.stats.endpoints import leaguedashplayerstats
import pandas as pd
import os

def fetch_and_save_advanced_player_stats(season, save_path=""):
    try:
        # Fetch advanced player stats for the season
        advanced_stats = leaguedashplayerstats.LeagueDashPlayerStats(season=season, measure_type_detailed_defense="Advanced")
        advanced_stats_df = advanced_stats.get_data_frames()[0]

        advanced_stats_df['season'] = season  # Add season column for clarity

        # Ensure the save path exists
        os.makedirs(save_path, exist_ok=True)
        output_path = os.path.join(save_path, f'advanced_player_stats_{season}.csv')
        advanced_stats_df.to_csv(output_path, index=False)

        print(f"Saved advanced player stats for season {season}.")
    except Exception as e:
        print(f"Error fetching advanced player stats for season {season}: {e}")
        output_path = None

    return output_path
