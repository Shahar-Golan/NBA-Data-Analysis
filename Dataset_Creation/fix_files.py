
from .add_teamID_col import add_team_id_to_players
from .tier_selection import adjust_tiers
from .create_top_100_players import top_100_players

# Perform data modifications
add_team_id_to_players(r"C:\Users\Shahar Golan\PycharmProjects\NBA\All_Seasons\2002-03\player_game_logs_2002-03_regular_season.csv",
                       r"C:\Users\Shahar Golan\PycharmProjects\NBA\All_Seasons\2002-03\team_game_logs_2002-03_regular_season.csv")
adjust_tiers(r"C:\Users\Shahar Golan\PycharmProjects\NBA\All_Seasons\2002-03\team_game_logs_2002-03_regular_season.csv")

# Save top 100 players data
path_to_top_100_players = top_100_players(
    r"C:\Users\Shahar Golan\PycharmProjects\NBA\All_Seasons\2002-03\advanced_player_stats_2002-03.csv",
    r"C:\Users\Shahar Golan\PycharmProjects\NBA\All_Seasons\2002-03\team_game_logs_2002-03_playoffs.csv",
    r"C:\Users\Shahar Golan\PycharmProjects\NBA\All_Seasons\2002-03\player_game_logs_2002-03_regular_season.csv",
    "2002-03",
    r"C:\Users\Shahar Golan\PycharmProjects\NBA\All_Seasons\2002-03"
)