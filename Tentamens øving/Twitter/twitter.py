import json

with open("twitter.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)


flest_følgere = sorted(data, key=lambda bruker: bruker['followers'], reverse = True)


print(flest_følgere[0: 10])

for bruker in flest_følgere[0:10]:
    n = bruker["tweets"]/ bruker["followers"]
    print(n)


for bruker in flest_følgere[0:10]:
    if bruker["following"] == 0:
        n =  bruker["followers"]/ 1

    else:
        n = bruker["followers"]/ bruker["following"]
    print(n)

