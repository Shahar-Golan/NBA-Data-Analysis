from Dataset_Creation.season_create import dataset_creation, validate_season_format

path = r"/All_Seasons"
season = "2005-06"

print(repr(season))
validate_season_format(season)

dataset_creation(season, path)
# the process took 20+ minutes