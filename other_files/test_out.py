from nba_api.stats.endpoints import draftcombinestats

# Try fetching draft combine stats data
combine_data = draftcombinestats.DraftCombineStats()
combine_df = combine_data.get_data_frames()[0]

# Print out unique seasons available in the data
print("Available Seasons in Draft Combine Stats:", combine_df['SEASON'].unique())
