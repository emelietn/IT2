import json

with open("Vedlegg_REA3049_IT2_Datasett/Global YouTube Statistics.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)



antall_youtubere_per_land = {}


for youtuber in data:
    country = youtuber['Country']
    if country in antall_youtubere_per_land:
        antall_youtubere_per_land[country] += 1
    else:
        antall_youtubere_per_land[country] = 1


print(antall_youtubere_per_land)


flest_youtubere= sorted(antall_youtubere_per_land, key=lambda land: land, reverse = True)

for youtuber in flest_youtubere[0:10]:
    print(youtuber)








