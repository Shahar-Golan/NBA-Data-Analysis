import pandas as pd
import os

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from Dataset_Creation.season_create import validate_season_format
from Machine_Learning.feature_selection import activate_rolling_data
from Machine_Learning.kinds_of_ML_models import return_model


def get_data_for_season(season, base_path=r"C:\Users\Shahar Golan\PycharmProjects\NBA\All_Seasons"):
    # Validate the season format
    validate_season_format(season)

    # Define file paths for regular season and playoff data
    regular_season_file = os.path.join(base_path, season, f"team_game_logs_{season}_regular_season.csv")
    playoff_file = os.path.join(base_path, season, f"team_game_logs_{season}_playoffs.csv")

    # Load the datasets
    regular_season_df = pd.read_csv(regular_season_file)
    playoff_df = pd.read_csv(playoff_file)

    return regular_season_df, playoff_df

def merge_regular_season_and_playoffs(regular_season_df, playoff_df):
    # Ensure GAME_DATE is in datetime format
    regular_season_df['GAME_DATE'] = pd.to_datetime(regular_season_df['GAME_DATE'])
    playoff_df['GAME_DATE'] = pd.to_datetime(playoff_df['GAME_DATE'])

    # Add the "Playoff" column: 0 for regular season, 1 for playoffs
    regular_season_df['PLAYOFF'] = 0
    playoff_df['PLAYOFF'] = 1

    # Concatenate the dataframes
    merged_df = pd.concat([regular_season_df, playoff_df], ignore_index=True)

    # Sort by GAME_DATE to maintain chronological order
    merged_df = merged_df.sort_values(by='GAME_DATE').reset_index(drop=True)

    return merged_df

def delete_non_essential_columns(df):
    df = df.select_dtypes(include=['float64', 'int64'])
    df = df.fillna(df.mean())
    columns_to_drop = ['SEASON_ID', 'TEAM_ID', 'GAME_ID', 'VIDEO_AVAILABLE']
    # Drop the specified columns from df
    df = df.drop(columns=columns_to_drop, errors='ignore')
    return df

def split_train_test(df, target_column="TARGET"):
    # Split into training (regular season) and test (playoffs) sets
    train_df = df[df['PLAYOFF'] == 0].drop(columns=['PLAYOFF'])
    test_df = df[df['PLAYOFF'] == 1].drop(columns=['PLAYOFF', target_column])
    return train_df, test_df

def get_train_test_df(regular_season_df, playoff_df):
    # get two different df's
    df = merge_regular_season_and_playoffs(regular_season_df, playoff_df)
    df = activate_rolling_data(df)

    essential_columns = ['TEAM_NAME', 'MATCHUP', 'TARGET', 'GAME_ID']
    predictions_df = df[essential_columns]
    # Filter predictions_df to retain only playoff data
    predictions_df = predictions_df[df['PLAYOFF'] == 1].reset_index(drop=True)

    df = delete_non_essential_columns(df)

    # Split into train and test sets
    train_df, final_test_df = split_train_test(df)

    return train_df, final_test_df, predictions_df

def run_machine_learning_model(season, model_function=""):
    regular_season_df, playoff_df = get_data_for_season(season)
    train_df, final_test_df, prediction_df = get_train_test_df(regular_season_df, playoff_df)
    # split train_df into train-val
    X_train, X_val, y_train, y_val = train_test_split(
        train_df.drop(columns=['TARGET']), train_df['TARGET'], test_size=0.2, random_state=42
    )

    model = return_model(model_function)

    if model:
        model, val_accuracy = model(X_train, X_val, y_train, y_val)
    else:
        model, val_accuracy= None, None
    # Train and evaluate on validation data


    # Train the model on the full training set before testing on the playoff data
    X_full_train = train_df.drop(columns=['TARGET'])
    y_full_train = train_df['TARGET']
    model.fit(X_full_train, y_full_train)

    final_predictions = model.predict(final_test_df)


    # Combine predictions with essential columns for final display
    prediction_df['PREDICTED_WIN'] = final_predictions
    # Calculate and print the test accuracy
    test_accuracy = accuracy_score(prediction_df['TARGET'], prediction_df['PREDICTED_WIN'])
    print("\nPlayoff Predictions:")
    print(prediction_df[['TEAM_NAME', 'MATCHUP', 'PREDICTED_WIN', 'TARGET']].head(30))

    return val_accuracy, test_accuracy


# 3. represent and connect it to my GUI application
# 4. upload to git_hub


