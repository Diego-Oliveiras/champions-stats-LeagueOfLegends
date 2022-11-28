import pandas as pd
import requests


def extract_name_champs():
    url = 'http://ddragon.leagueoflegends.com/cdn/12.22.1/data/en_US/champion.json'
    response = requests.get(url).json()
    champions = []
    for championName in response['data']:
        champions.append(championName)
    return champions

def extract_response_champs_lol(champion):
    url = f'http://ddragon.leagueoflegends.com/cdn/12.22.1/data/en_US/champion/{champion}.json'
    championResponse = requests.get(url).json()
    return championResponse

#sorry it's so sore for the eyes but I wanted to pick just a few interesting columns
def extract_profile(championResponses,champion):
    championKey= championResponses['data'][champion]['key']
    championName = championResponses['data'][champion]['name']
    championTitle = championResponses['data'][champion]['title']
    championListTags = championResponses['data'][champion]['tags']
    championInfoAttack = championResponses['data'][champion]['info']['attack']
    championInfoDefense = championResponses['data'][champion]['info']['defense']
    championInfoMagic = championResponses['data'][champion]['info']['magic']
    championInfodifficulty = championResponses['data'][champion]['info']['difficulty']
    championStatsHp = championResponses['data'][champion]['stats']['hp']
    championStatsHpperlevel = championResponses['data'][champion]['stats']['hpperlevel']
    championStatsMp = championResponses['data'][champion]['stats']['mp']
    championStatsMpperlevel = championResponses['data'][champion]['stats']['mpperlevel']
    championStatsMovespeed = championResponses['data'][champion]['stats']['movespeed']
    championStatsArmor = championResponses['data'][champion]['stats']['armor']
    championStatsArmorPerLevel = championResponses['data'][champion]['stats']['armorperlevel']
    championStatsSpellblock = championResponses['data'][champion]['stats']['spellblock']
    championStatsSpellblockperlevel = championResponses['data'][champion]['stats']['spellblockperlevel']
    championStatsAttackrange = championResponses['data'][champion]['stats']['attackrange']
    championStatsHpregen = championResponses['data'][champion]['stats']['hpregen']
    championStatsHpregenperlevel = championResponses['data'][champion]['stats']['hpregenperlevel']
    championStatsMpregen = championResponses['data'][champion]['stats']['mpregen']
    championStatsMpregenperlevel = championResponses['data'][champion]['stats']['mpregenperlevel']
    championStatsCrit = championResponses['data'][champion]['stats']['crit']
    championStatsCritperlevel = championResponses['data'][champion]['stats']['critperlevel']
    championStatsAttackdamage = championResponses['data'][champion]['stats']['attackdamage']
    championStatsAttackdamageperlevel= championResponses['data'][champion]['stats']['attackdamageperlevel']
    championStatsAttackspeedperlevel = championResponses['data'][champion]['stats']['attackspeedperlevel']
    championStatsAttackspeed = championResponses['data'][champion]['stats']['attackspeed']
    championStats = {'id':championKey,'name':championName,'title':championTitle,'tags':championListTags,'attack':championInfoAttack,
    'defense':championInfoDefense,'magic':championInfoMagic,'difficulty':championInfodifficulty,
        'hp':championStatsHp,'hpperlevel':championStatsHpperlevel,'mp':championStatsMp,'mpperlevel':championStatsMpperlevel,
        'movespeed':championStatsMovespeed,'armor':championStatsArmor,'armorperlevel':championStatsArmorPerLevel,'spellblock':championStatsSpellblock,
        'spellblockperlevel':championStatsSpellblockperlevel,'attackrange':championStatsAttackrange,'hpregen':championStatsHpregen,'hpregenperlevel':championStatsHpregenperlevel,
        'mpregen':championStatsMpregen,'mpregenperlevel':championStatsMpregenperlevel,'crit':championStatsCrit,'critperlevel':championStatsCritperlevel,'attackdamage':championStatsAttackdamage,
        'attackdamageperlevel':championStatsAttackdamageperlevel,'attackspeedperlevel':championStatsAttackspeedperlevel,'attackspeed':championStatsAttackspeed
    }
    return championStats


def extract_profiles_champs(listChampionsNames):
    championsProfiles = []
    for champion in listChampionsNames:
        responseChampion= extract_response_champs_lol(champion)
        championProfile = extract_profile(responseChampion,champion)
        championsProfiles.append(championProfile)
    return championsProfiles

def extract_skins_champs(listChampionsNames):
    allChampions_Skins = pd.DataFrame(columns=['id','num','chromas','key'])
    for champion in listChampionsNames:
        responseChampion= extract_response_champs_lol(champion)
        championSkins = extract_skins(champion,responseChampion)
        allChampions_Skins = allChampions_Skins.merge(championSkins, how='outer')
    return allChampions_Skins

def extract_skins(champion,championResponses):
    skins = pd.json_normalize(championResponses['data'][champion], record_path=['skins'])
    key = championResponses['data'][champion]['key']
    skins['key'] = key
    skins = url_skin(champion,skins)
    return skins

def url_skin(champion,skins):
    nums_skins = skins['num']
    urlsGroup = []
    for num in nums_skins:
        urlsGroup.append(f'http://ddragon.leagueoflegends.com/cdn/img/champion/splash/{champion}_{num}.jpg')
    skins['url'] = urlsGroup
    return skins