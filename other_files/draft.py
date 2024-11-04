import pandas as pd
from nba_api.stats.endpoints import drafthistory, draftcombinestats


def fetch_and_save_draft_history(season="2000"):
    try:
        # Fetch draft history data
        draft_data = drafthistory.DraftHistory()
        draft_df = draft_data.get_data_frames()[0]

        # Filter by the specific draft year
        draft_df = draft_df[draft_df['DRAFT_YEAR'] == season]

        # Save to CSV
        draft_df.to_csv(f'draft_history_{season}.csv', index=False)
        print(f"Saved draft history data for {season}.")
    except Exception as e:
        print(f"Error fetching draft history data for {season}: {e}")


def fetch_and_save_draft_combine_stats(season="2000-01"):
    try:
        # Fetch draft combine stats
        combine_data = draftcombinestats.DraftCombineStats()
        combine_df = combine_data.get_data_frames()[0]

        # Filter by season if applicable
        combine_df = combine_df[combine_df['SEASON'] == season]

        # Save to CSV
        combine_df.to_csv(f'draft_combine_stats_{season}.csv', index=False)
        print(f"Saved draft combine stats data for {season}.")
    except Exception as e:
        print(f"Error fetching draft combine stats data for {season}: {e}")


# Fetch and save draft data for 2000 season
fetch_and_save_draft_history("2000")
fetch_and_save_draft_combine_stats("2000-01")


