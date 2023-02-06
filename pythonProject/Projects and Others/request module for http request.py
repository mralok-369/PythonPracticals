import requests
# r = requests.get("https://financialmodelingprep.com/api/company/price/AAPL")
# r = requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population")
r = requests.get("http://universities.hipolabs.com/search?country=United+States")
print(r.text)
print(r.status_code)

# url = "www.something.com"
# data = {
#     "p1":4,
#     "p2":8
# }
# r2 = requests.post(url=url,data=data)


#   free api keys
# 1 - Public APIs -> (https://api.publicapis.org/entries)
# 2 - Cat Facts -> (https://catfact.ninja/fact)
# 3 - CoinDesk -> (https://api.coindesk.com/v1/bpi/currentprice.json)
# 4 - Bored -> (https://www.boredapi.com/api/activity)
# 5 - Agify.io -> (https://api.agify.io?name=meelad)
# 6 - Genderize.io -> (https://api.genderize.io?name=luc)
# 7 - Nationalize.io -> (https://api.nationalize.io?name=nathaniel)
# 8 - Data USA -> (https://datausa.io/api/data?drilldowns=Nation&measures=Population)
# 9 - Dogs -> (https://dog.ceo/api/breeds/image/random)
# 10 - IPify -> (https://api.ipify.org?format=json)
# 11 - IPinfo -> (https://ipinfo.io/161.185.160.93/geo)
# 12 - Jokes -> (https://official-joke-api.appspot.com/random_joke)
# 13 - RandomUser -> (https://randomuser.me/api/)
# 14 - Universities List -> (http://universities.hipolabs.com/search?country=United+States)
# 15 - Zippopotam -> (https://api.zippopotam.us/us/33162)
