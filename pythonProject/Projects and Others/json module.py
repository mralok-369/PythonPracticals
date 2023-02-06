import json
#  JSON -> java script object notation

data = '{"var1":"harry","var2":56}'
print(data)

parsed = json.loads(data)
print(type(parsed))
print(parsed['var1'])

# task 1 - json.load()

data2 = {
    "channel_list": "codeWithHarry",
    "cars": ["bmw","audi a8","ferrari"],
    "fridge":('roti',540),
    "isbad": False
}
jscomp = json.dumps(data2)
print(jscomp)

# task 2 -> what is sort_keys parameter in dumps
