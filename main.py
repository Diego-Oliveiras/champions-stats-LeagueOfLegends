import pandas as pd

import db
import extract

print('Extracting list of names of champions..')
listChampionsNames = extract.extract_name_champs()

print('creating profiles..')
profiles_champions = extract.extract_profiles_champs(listChampionsNames)

print('Exctracting skins of champions..')
skins_champions = extract.extract_skins_champs(listChampionsNames)

print('Applying dataframe formatting')
profiles_champions = pd.DataFrame(profiles_champions)
skins_champions = pd.DataFrame(skins_champions)


#make sure the database is configured with your settings
db.insert_in_LeagueOflegends(profiles_champions,'profiles_champions')
db.insert_in_LeagueOflegends(skins_champions,'skins_champions')