import os

def get_top_players_regular_season_path(season):
    regular_season_path = os.path.join(
        r"C:\Users\Shahar Golan\PycharmProjects\NBA\All_Seasons",
        season,
        f"top_100_players_info_regular_season_{season}.csv"
    )
    return regular_season_path

def get_team_regular_season_path(season):
    regular_season_path = os.path.join(
        r"C:\Users\Shahar Golan\PycharmProjects\NBA\All_Seasons",
        season,
        f"team_game_logs_{season}_regular_season.csv"
    )
    return regular_season_path
