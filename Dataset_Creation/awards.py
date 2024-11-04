import pandas as pd
import time
import os

from nba_api.stats.endpoints import  playerawards
from player_logs import fetch_active_players


def fetch_and_save_player_awards(season="", save_path=""):
    # Get players active in the specified season
    active_players = fetch_active_players(season)
    awards_data = []

    for index, row in active_players.iterrows():
        player_id = row['PERSON_ID']
        player_name = row['DISPLAY_FIRST_LAST']

        try:
            # Fetch awards for each player
            awards = playerawards.PlayerAwards(player_id=player_id)
            awards_df = awards.get_data_frames()[0]
            if not awards_df.empty:
                awards_df['player_id'] = player_id
                awards_df['player_name'] = player_name
                awards_df['season'] = season
                awards_data.append(awards_df)

            # Print progress
            print(f"Fetched awards data for player {index + 1}/{len(active_players)}: {player_name}")

            # Pause to avoid rate limits
            time.sleep(0.1)
        except Exception as e:
            print(f"Error fetching awards for player {player_name}: {e}")

    # Combine all awards data and save to CSV
    if awards_data:
        awards_df = pd.concat(awards_data, ignore_index=True)
        os.makedirs(save_path, exist_ok=True)  # Ensure save_path exists
        output_path = os.path.join(save_path, f'player_awards_{season}.csv')
        awards_df.to_csv(output_path, index=False)
        print(f"Saved player awards data for season {season} to {output_path}.")
    else:
        print("No awards data found for players in the specified season.")
        output_path = None

    return output_path