import os
from datetime import datetime
from .player_logs import fetch_and_save_game_logs
from .team_logs import fetch_and_save_team_game_logs
from .player_profile import fetch_and_save_player_profiles
from .advanced_stats import fetch_and_save_advanced_player_stats
from .awards import fetch_and_save_player_awards
from .add_teamID_col import add_team_id_to_players
from .tier_selection import adjust_tiers
from .create_top_100_players import top_100_players


def validate_season_format(season):
    # Check if season matches the format "20##-##"
    if not (len(season) == 7 and season[:2] == "20" and season[4] == "-"):
        raise ValueError("Season must be in the format '20##-##'")

    start_year = int(season[:4])
    end_year = int(season[5:])
    current_year = datetime.now().year

    # Check if start and end years are logical
    if start_year < 2000 or start_year > current_year or end_year != (start_year + 1) % 100:
        raise ValueError("Invalid season years")


def dataset_creation(season, directory_path):
    # Validate season format
    validate_season_format(season)

    # Create a season-specific directory
    season_dir = os.path.join(directory_path, season)
    os.makedirs(season_dir, exist_ok=True)

    # Fetch and save game logs for regular season and playoffs
    path_to_player_logs_regular_season = fetch_and_save_game_logs(season, "Regular Season", season_dir)
    path_to_player_logs_playoffs = fetch_and_save_game_logs(season, "Playoffs", season_dir)
    path_to_team_logs_regular_season = fetch_and_save_team_game_logs(season, "Regular Season", season_dir)
    path_to_team_logs_playoffs = fetch_and_save_team_game_logs(season, "Playoffs", season_dir)
    path_to_player_profile = fetch_and_save_player_profiles(season, season_dir)
    path_to_advanced_stats = fetch_and_save_advanced_player_stats(season, season_dir)
    path_to_awards = fetch_and_save_player_awards(season, season_dir)

    # Perform data modifications
    add_team_id_to_players(path_to_player_logs_regular_season, path_to_team_logs_regular_season)
    adjust_tiers(path_to_team_logs_regular_season)

    # Save top 100 players data
    path_to_top_100_players = top_100_players(
        path_to_advanced_stats,
        path_to_team_logs_playoffs,
        path_to_player_logs_regular_season,
        season,
        season_dir
    )

    print(f"Data for season {season} has been successfully created in {season_dir}")