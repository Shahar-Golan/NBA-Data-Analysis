import  pandas as pd

def adjust_tiers(teams_path):

    team_logs = pd.read_csv(teams_path)

    wins_dict = team_logs[team_logs['WL'] == 'W'].groupby('TEAM_ID').size().to_dict()

    sorted_by_wins = sorted(wins_dict.items(), key=lambda x: x[1], reverse=True)

    tiers = {}

    tier_size = 10 if len(sorted_by_wins) == 30 else 9

    for i, (team_id, wins) in enumerate(sorted_by_wins):
        # select the 9 best teams
        if i < tier_size:
            tiers[team_id] = 1
        elif i < tier_size + 10:
            tiers[team_id] = 2
        else:
            tiers[team_id] = 3

    # Create a mapping of TEAM_ABBREVIATION to TEAM_ID and TIER
    team_abbr_to_tier = {row['TEAM_ABBREVIATION']: tiers[row['TEAM_ID']] for _, row in team_logs.iterrows()}

    # Extract the opponent abbreviation and map it to the tier
    team_logs['OPPONENT'] = team_logs['MATCHUP'].str.split().str[-1]

    team_logs = team_logs.rename(columns={'VIDEO_AVAILABLE': 'VS_TIER'})
    team_logs['VS_TIER'] = team_logs['OPPONENT'].map(team_abbr_to_tier)

    team_logs.to_csv(teams_path, index=False)

