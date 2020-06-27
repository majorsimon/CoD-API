
from cod import CallOfDutyAPIClient
import json
import os


DEFAULT_BASE_URL = "https://my.callofduty.com/api/papi-client/"
COD_ENDPOINTS = {
    'playerInfo': {
        'host': DEFAULT_BASE_URL,
        'path': 'stats/cod/v1/title/{title}/platform/{platform}/gamer/{userid}/profile/type/{gametype}',
        'method': 'GET'
    },
    'playerInfoFriends': {
        'host': DEFAULT_BASE_URL,
        'path': 'stats/cod/v1/title/{title}/platform/{platform}/gamer/{userid}/profile/friends/type/{gametype}',
        'method': 'GET'
    },
    'playerRecentMatchesDetail': {
        'host': DEFAULT_BASE_URL,
        'path': 'crm/cod/v2/title/{title}/platform/{platform}/gamer/{userid}/matches/{gametype}/start/{startdate}/end/{enddate}/details',
        'method': 'GET'
    },
    'playerRecentMatches': {
        'host': DEFAULT_BASE_URL,
        'path': 'crm/cod/v2/title/{title}/platform/{platform}/gamer/{userid}/matches/{gametype}/start/{startdate}/end/{enddate}',
        'method': 'GET'
    },
    'playerAnalysis': {
        'host': DEFAULT_BASE_URL,
        'path': 'ce/v2/title/{title}/platform/{platform}/gametype/all/gamer/{userid}/summary/match_analysis/contentType/full/end/0/matchAnalysis/mobile/en',
        'method': 'GET'
    },
    'playerLoot': {
        'host': DEFAULT_BASE_URL,
        'path': 'loot/title/{title}/platform/{platform}/gamer/{userid}/status/en',
        'method': 'GET'
    },
    'playerCodPoints': {
        'host': DEFAULT_BASE_URL, 
        'path': 'inventory/v1/title/{title}/platform/{platform}/gamer/{userid}/currency',
        'method': 'GET'
    }
}

username = os.environ.get('COD_USER')
password = os.environ.get('COD_PASS')
client = CallOfDutyAPIClient()
client.login(username, password)

title = 'mw'
platform = 'battle'
gametype = 'mp'
userid = 'majorsimon%2321870'
startdate = 0
enddate = 0

results = {}
for name, endpoint in COD_ENDPOINTS.items():
    results[name] = client.sendRequest(endpoint['host'], endpoint['path'].format(**globals()), endpoint['method'])

with open('results.json', 'w') as f:
    json.dump(results, f, indent=4)
