from nba_api.stats.endpoints import commonallplayers, playergamelog
import pandas as pd
import time
import os

def fetch_active_players(season):
    active_players = commonallplayers.CommonAllPlayers(is_only_current_season=0, league_id='00', season=season)
    player_data = active_players.get_data_frames()[0]
    player_ids = player_data[player_data['ROSTERSTATUS'] == 1][['PERSON_ID', 'DISPLAY_FIRST_LAST']]
    return player_ids

def fetch_and_save_game_logs(season, season_type, save_path):
    # Fetch regular season game logs
    player_ids = fetch_active_players(season)
    game_data = []

    for index, row in player_ids.iterrows():
        player_id = row['PERSON_ID']
        player_name = row['DISPLAY_FIRST_LAST']

        try:
            # Fetch game logs for each active player in the specified season (Regular Season)
            gamelog = playergamelog.PlayerGameLog(player_id=player_id, season=season, season_type_all_star=season_type)
            df = gamelog.get_data_frames()[0]
            if not df.empty:
                df['player_id'] = player_id
                df['player_name'] = player_name
                df['season_type'] = season_type
                game_data.append(df)

            print(f"Fetched {season_type} data for player {index + 1}/{len(player_ids)}: {player_name}")
            time.sleep(0.1)
        except Exception as e:
            print(f"Error fetching {season_type} data for player {player_name} in season {season}: {e}")

    game_data = [df for df in game_data if not df.empty]
    if game_data:
        season_df = pd.concat(game_data, ignore_index=True)

        filename = f'player_game_logs_{season}_{season_type.replace(" ", "_").lower()}.csv'
        output_path = os.path.join(save_path, filename)

        season_df.to_csv(output_path, index=False)
        print(f"Saved {season_type} game logs for season {season}.")
    else:
        print(f"No data was retrieved for the {season_type} {season}.")
        output_path = None

    return output_path

