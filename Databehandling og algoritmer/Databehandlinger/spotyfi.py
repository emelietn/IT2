import json 
Data = json.load(open("spotify-weekly-top-songs-global-uke2-2023 (1).json"))

flest_uker = sorted(Data, key=lambda sang: sang['uker_paa_listen'], reverse = True)

print(flest_uker[0])

taylor_swift_streams = 0

for sang in Data:
    if sang['artist'] == "Taylor Swift":
        taylor_swift_streams += sang['antall_streams']

print(taylor_swift_streams)
        
største = 0
største_sang = 0
for sang in Data:
    diferanse = sang["forrige_plassering"] - sang["plassering"]
    if diferanse > største:
        største = diferanse
        største_sang = sang



print(største, største_sang)
