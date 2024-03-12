import json
data = json.load(open("representanter.json"))
import matplotlib.pyplot as plt

# Lag en for-løkke som printer navn og tilhørnde parti på alle politikerne
# Hvilket parti har flest representanter på Stortinget og hvor mange har de?
# Lag en ordbok som teller antall representanter hvert parti har
# Lag et plott som viser en oversikt over partier og antall representanter
# Hvor mange representanter har hvert parti i gjennomsnitt?
    
for representant in data['representanter_liste']:
    print(representant['fornavn']+ "   " + representant['etternavn']+ "  " +  representant['fylke']['navn'])




parti_antall = {}         

for representant in data ['representanter_liste']:
    if representant['parti']['navn'] in parti_antall:
        parti_antall [representant['parti']['navn']] += 1
    else:
        parti_antall [representant['parti']['navn']] = 1
     
parti_antall_sortert = sorted(parti_antall.items(), key=lambda parti: parti[1], reverse = True)

#print(parti_antall_sortert)


parti_antall_sortert_ordbok = dict(sorted(parti_antall.items(), key=lambda parti: parti[1], reverse = True))


print(parti_antall_sortert_ordbok)





plt.bar(parti_antall_sortert_ordbok.keys(), parti_antall_sortert_ordbok.values())
plt.show()


print(sum(parti_antall_sortert_ordbok.values())/ len(parti_antall_sortert_ordbok.values()))





