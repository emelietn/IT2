import json

with open("Vedlegg_REA3049_IT2_Datasett/Global YouTube Statistics.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)

youtuber_land = {}

for youtuber in data:
    country = youtuber['Country']
    subscribers = youtuber['subscribers']
    viewers = youtuber['video views']
    if country in youtuber_land:
        youtuber_land[country]['antall'] += 1
        youtuber_land[country]['subscribers'] += subscribers
        youtuber_land[country]['video views'] += viewers
    else:
        land = {}
        land['antall'] = 1
        land['subscribers'] = subscribers
        land['video views'] = viewers
        youtuber_land[country] = land

# Sorter landene etter antall kanaler i synkende rekkefølge
youtuber_land_sortert = sorted(youtuber_land.items(), key=lambda x: x[1]['antall'], reverse=True)

# Begrens til de ti landene med flest kanaler
top_10_land = youtuber_land_sortert[:10]

# Gå gjennom de ti landene og beregn gjennomsnittlig antall abonnenter og videovisninger per kanal
for land, info in top_10_land:
    gjennomsnitt_abonnenter = info['subscribers'] / info['antall']
    gjennomsnitt_videovisninger = info['video views'] / info['antall']
    print(f"Land: {land}")
    print(f"Gjennomsnittlig antall abonnenter per kanal: {gjennomsnitt_abonnenter}")
    print(f"Gjennomsnittlig antall videovisninger per kanal: {gjennomsnitt_videovisninger}")
    print("-------------")

