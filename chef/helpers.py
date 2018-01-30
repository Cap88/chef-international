import requests

YOUR_APP_ID = '0216fa0a'
YOUR_APP_KEY = 'e0b5b72adaff004caf7f9f0d92885691'

def lookup(country, results_from, results_to):
    r = requests.get('https://api.edamam.com/search?q=' + country + '&app_id=' + YOUR_APP_ID + '&app_key=' + YOUR_APP_KEY + '&from=' + str(results_from) + '&to=' + str(results_to))
    return r.json()
#	'https://api.edamam.com/search?q=' + country + '&app_id=$' + YOUR_APP_ID + '&app_key=$' + YOUR_APP_KEY
		
#	payload = {'q': country}
#    r = requests.get('http://httpbin.org/get', params=payload)