import pandas as pd

# Load the CSV file
df = pd.read_csv(r'C:\Projects\pyCharm\archive\csv\NBA_draft_combine.csv', na_values='NA')

# Replace NA with -1
df.fillna(-1, inplace=True)

# Save the modified CSV
df.to_csv(r'C:\Projects\pyCharm\archive\csv\NBA_draft_combine_clean.csv', index=False)

