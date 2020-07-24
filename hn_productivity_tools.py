import requests

ix = 23468193
dct = {}
data = requests.get(
    "https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty".format(ix)
).json()
dct[ix] = data
for ix in dct[ix]["kids"]:
    data = requests.get(
        "https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty".format(ix)
    ).json()
    dct[ix] = data
