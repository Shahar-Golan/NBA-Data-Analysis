import pandas as pd

def calculate_offensive_rolling_stats(df, columns, window=10):
    # Sort the dataframe by team and date
    df = df.sort_values(by=['TEAM_ID', 'GAME_DATE'])

    # Group by each team and apply rolling window to calculate rolling mean of offensive stats
    for col in columns:
        df[f'OFF_{col}_last_{window}'] = df.groupby('TEAM_ID')[col].transform(
            # the min period allows the calculation to work even if there are less than 10 games.
            lambda x: x.rolling(window, min_periods=1).mean())
    return df


def calculate_defensive_stats(df, columns, rolling_window=10):
    # Step 1: Identify home and away games
    df['HOME_GAME'] = df['MATCHUP'].apply(lambda x: 1 if 'vs.' in x else 0)

    # Step 2: Convert offensive stats of the opponent to defensive perspective for each team
    defensive_df = df.copy()
    defensive_df[columns] = df.groupby('OPPONENT')[columns].shift(1)

    # Step 3: Calculate rolling defensive stats over the last `rolling_window` games
    for col in columns:
        df[f'DEF_{col}_last_{rolling_window}'] = (
            defensive_df.groupby('TEAM_ID')[col]
            .transform(lambda x: x.rolling(window=rolling_window, min_periods=1).mean())
        )

    return df


def calculate_rolling_win_percentage(df, window=10):
    # Create a new column 'WIN' where 1 represents a win, and 0 represents a loss
    df['WIN'] = df['WL'].apply(lambda x: 1 if x == 'W' else 0)

    # Group by 'TEAM_ID' and calculate rolling win percentage
    df['ROLLING_WIN_PCT'] = df.groupby('TEAM_ID')['WIN'].transform(
        lambda x: x.rolling(window, min_periods=1).mean()
    )
    return df


def calculate_win_pct_vs_tier(df):
    # Calculate cumulative wins and games played against each tier for each team
    win_counts = df.groupby(['TEAM_ID', 'VS_TIER'])['WIN'].cumsum()
    game_counts = df.groupby(['TEAM_ID', 'VS_TIER']).cumcount() + 1  # +1 to avoid division by zero

    # Calculate win percentage against each tier
    df['WIN_PCT_VS_TIER'] = win_counts / game_counts
    del df['WIN']
    return df


def calculate_rest_days(df):
    # Ensure GAME_DATE is in datetime format
    df['GAME_DATE'] = pd.to_datetime(df['GAME_DATE'])

    # Sort by TEAM_ID and GAME_DATE to calculate rest days within each team
    df = df.sort_values(by=['TEAM_ID', 'GAME_DATE']).reset_index(drop=True)

    # Calculate rest days by finding the difference in GAME_DATE for consecutive games within each team
    df['REST_DAYS'] = df.groupby('TEAM_ID')['GAME_DATE'].diff().dt.days

    # filling the first game with 3 rest days.
    df['REST_DAYS'].fillna(3, inplace=True)  # or set to a default, e.g., 3 days

    return df


def delete_present_features(df):
    # Dropping unnecessary columns
    columns_to_drop = ['MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM',
                        'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV',
                       'PF', 'PTS', 'PLUS_MINUS']
    df = df.drop(columns=columns_to_drop)
    df['TARGET'] = df['WL'].map({'W': 1, 'L': 0})
    del df['WL']
    return df


def activate_rolling_data(df):
    # Define the features we want to calculate rolling averages for
    stats_to_average = ['PTS', 'FG_PCT', 'FG3_PCT', 'FT_PCT', 'OREB', 'DREB', 'AST', 'STL', 'BLK', 'TOV']
    # running all the functions
    df = calculate_offensive_rolling_stats(df, stats_to_average)
    df = calculate_defensive_stats(df, stats_to_average)
    df = calculate_rolling_win_percentage(df, window=10)
    df = calculate_win_pct_vs_tier(df)
    df = calculate_rest_days(df)
    df = delete_present_features(df)
    return df










