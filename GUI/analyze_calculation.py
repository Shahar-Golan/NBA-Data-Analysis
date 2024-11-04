from data_processing import get_player_data

def calculate_stat_vs_tier(player_data, stat):
    if stat not in player_data.columns:
        print(f"Statistic {stat} not found in player data.")
        return None
    # attention to the [stat], it will return the mean
    return player_data.groupby('VS_TIER')[stat].mean().sort_index()

# Wrapper functions for each specific stat
def analyze_ppg(season, player_name):
    # create the df of a specific player
    player_data = get_player_data(season, player_name)
    # activate the function that calculate the mean
    return calculate_stat_vs_tier(player_data, 'PTS')


def analyze_ast(season, player_name):
    player_data = get_player_data(season, player_name)
    return calculate_stat_vs_tier(player_data, 'AST')


def analyze_reb(season, player_name):
    player_data = get_player_data(season, player_name)
    return calculate_stat_vs_tier(player_data, 'REB')


def analyze_wins(season, player_name):
    player_data = get_player_data(season, player_name)
    wins_by_tier = player_data[player_data['WL'] == 'W'].groupby('VS_TIER').size()
    total_games_by_tier = player_data.groupby('VS_TIER').size()
    win_pct_by_tier = (wins_by_tier / total_games_by_tier).fillna(0).sort_index()
    return win_pct_by_tier