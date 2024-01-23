sortert_personer = sorted(Personer, key = lambda person : person ["alder"], reverse = True)
topp_2 = sortert_personer [:2]
print(topp_2)
