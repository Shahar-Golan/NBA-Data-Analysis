from nba_api.stats.endpoints import commonplayerinfo
import pandas as pd
import time
import os

from .player_logs import fetch_active_players


def fetch_and_save_player_profiles(season, save_path=""):
    # Fetch players active in the specified season
    active_players = fetch_active_players(season)
    profile_data = []

    for index, row in active_players.iterrows():
        player_id = row['PERSON_ID']
        player_name = row['DISPLAY_FIRST_LAST']

        try:
            # Fetch player profile information
            player_profile = commonplayerinfo.CommonPlayerInfo(player_id=player_id)
            df = player_profile.get_data_frames()[0]
            df['player_id'] = player_id
            profile_data.append(df)

            print(f"Fetched profile for player {index + 1}/{len(active_players)}: {player_name}")
            time.sleep(0.1)
        except Exception as e:
            print(f"Error fetching profile for player {player_name}: {e}")

    # Save profiles to CSV if data is available
    if profile_data:
        profile_df = pd.concat(profile_data, ignore_index=True)
        os.makedirs(save_path, exist_ok=True)  # Ensure save_path exists
        output_path = os.path.join(save_path, f'player_profiles_{season}.csv')
        profile_df.to_csv(output_path, index=False)
        print(f"Saved player profiles for season {season} to {output_path}.")
    else:
        print(f"No profile data retrieved for season {season}.")
        output_path = None

    return output_path


