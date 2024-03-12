top_30 = [
    {"name": "Cristiano Ronaldo", "account": "@cristiano", "followers": 617.16, "nationality": "Portugal"},
    {"name": "Leo Messi", "account": "@leomessi", "followers": 497.05, "nationality": "Argentina"},
    {"name": "Selena Gomez", "account": "@selenagomez", "followers": 429.66, "nationality": "United States"},
    {"name": "Kylie Jenner", "account": "@kyliejenner", "followers": 399.45, "nationality": "United States"},
    {"name": "Dwayne Johnson", "account": "@therock", "followers": 395.59, "nationality": "United States"},
    {"name": "Ariana Grande", "account": "@arianagrande", "followers": 380.78, "nationality": "United States"},
    {"name": "Kim Kardashian", "account": "@kimkardashian", "followers": 364, "nationality": "United States"},
    {"name": "Beyoncé", "account": "@beyonce", "followers": 319.6, "nationality": "United States"},
    {"name": "Khloé Kardashian", "account": "@khloekardashian", "followers": 311.3, "nationality": "United States"},
    {"name": "Nike", "account": "@nike", "followers": 306, "nationality": "United States"},
    {"name": "Justin Bieber", "account": "@justinbieber", "followers": 304.9, "nationality": "Canada"},
    {"name": "Taylor Swift", "account": "@taylorswift", "followers": 282.8, "nationality": "United States"},
    {"name": "Neymar Jr", "account": "@neymarjr", "followers": 282.7, "nationality": "Brazil"},
    {"name": "Kendall Jenner", "account": "@kendalljenner", "followers": 279.9, "nationality": "United States"},
    {"name": "Jennifer Lopez", "account": "@jlo", "followers": 277.2, "nationality": "United States"},
    {"name": "Nicki Minaj", "account": "@nickiminaj", "followers": 262.5, "nationality": "Trinidad and Tobago"},
    {"name": "National Geographic", "account": "@natgeo", "followers": 206.9, "nationality": "United States"},
    {"name": "Lionel Andrés Messi Cuccittini", "account": "@leomessi10", "followers": 201.8, "nationality": "Argentina"},
    {"name": "Miley Cyrus", "account": "@mileycyrus", "followers": 198.7, "nationality": "United States"},
    {"name": "Katy Perry", "account": "@katyperry", "followers": 198.4, "nationality": "United States"},
    {"name": "Kourtney Kardashian", "account": "@kourtneykardash", "followers": 196.8, "nationality": "United States"},
    {"name": "Kevin Hart", "account": "@kevinhart4real", "followers": 195.8, "nationality": "United States"},
    {"name": "Ellen DeGeneres", "account": "@theellenshow", "followers": 194.7, "nationality": "United States"},
    {"name": "Virat Kohli", "account": "@virat.kohli", "followers": 194.5, "nationality": "India"},
    {"name": "Billie Eilish", "account": "@billieeilish", "followers": 193.9, "nationality": "United States"},
    {"name": "Rihanna", "account": "@badgalriri", "followers": 191.5, "nationality": "Barbados"},
    {"name": "Zendaya", "account": "@zendaya", "followers": 190.9, "nationality": "United States"},
    {"name": "Drake", "account": "@champagnepapi", "followers": 190.8, "nationality": "Canada"},
    {"name": "Emma Watson", "account": "@emmawatson", "followers": 189.7, "nationality": "United Kingdom"},
    {"name": "LeBron James", "account": "@kingjames", "followers": 188.8, "nationality": "United States"}
]

total = 0

for personer in top_30:
    total += personer['followers']

print(total / 30)

ikke_fra_USA =0

for person in top_30:
    if person['nationality'] != "United States":
        ikke_fra_USA += 1
        
print(ikke_fra_USA)
