import json
from math import sqrt

with open("sykkelturer.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)

# 1. 
    
sykkeltur = {}

for sykkel in data:
    start_stasjon = sykkel['start_station_name']
    if start_stasjon in sykkeltur:
        sykkeltur[start_stasjon] += 1
    else:
        sykkeltur[start_stasjon] = 1


populaere_stasjoner = sorted(sykkeltur.items(), key=lambda x: x[1], reverse=True)[:5]


print("De fem mest populære startstasjonene:")
for stasjon, antall_turer in populaere_stasjoner:
    print(f"{stasjon}: {antall_turer} turer")


# 2. de tre lengste turene målt i tid
    
lengste_turer = sorted(data, key=lambda x: x['duration'], reverse=True)[:3]


print("\nDe tre lengste turene:")
for tur in lengste_turer:
    start_stasjon = tur['start_station_name']
    end_stasjon = tur['end_station_name']
    varighet = int(tur['duration']) // 60  
    print(f"Start: {start_stasjon}, Slutt: {end_stasjon}, Varighet: {varighet} minutter")


# 3. de tre lengste turene målt i distanse
    

def beregn_avstand(lat1, lon1, lat2, lon2):
    bredde_avstand = abs(lat2 - lat1)
    lengde_avstand = abs(lon2 - lon1)
    avstand = (bredde_avstand**2 + lengde_avstand**2)**0.5
    return avstand

sykkeltur_distanse = {}

for sykkeltur in data:
    start_lat = float(sykkeltur['start_station_latitude'])
    start_lon = float(sykkeltur['start_station_longitude'])
    end_lat = float(sykkeltur['end_station_latitude'])
    end_lon = float(sykkeltur['end_station_longitude'])
    
 
    avstand = beregn_avstand(start_lat, start_lon, end_lat, end_lon)
    sykkeltur_distanse[(start_lat, start_lon), (end_lat, end_lon)] = avstand

sorterte_turer = sorted(sykkeltur_distanse.items(), key=lambda x: x[1], reverse=True)[:3]

print("\nDe tre lengste turene målt i distanse:")
for tur in sorterte_turer:
    startpunkt = tur[0] 
    sluttpunkt = tur[1]
    print(f"Startpunkt: {startpunkt}, Sluttpunkt: {sluttpunkt}")


# Fikk ikke til denne siste oppgaven som jeg skulle, velger å gå videre til neste oppgave



