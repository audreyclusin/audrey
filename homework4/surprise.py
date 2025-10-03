# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
# 4) Look up another target, add all the necessary information to the targets list. 
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
# 6) What is your favorite constellation?

def star_name(dictionary):
    for item in dictionary:
        print(item)

def star_type(dictionary):
    for item in dictionary:
        print(item)
        print(dictionary[item]["Spectral Type"])

def greater_than_tenth(dictionary):
    stars = []
    for item in dictionary:
        if dictionary[item]["Magnitude"] > .1:
            stars.append(item)
    return stars

targets["Gacrux"] = {}
targets["Gacrux"]["RA"] = "12h 31m 09.9s"
targets["Gacrux"]["Dec"] = "-57 6' 48″"
targets["Gacrux"]["Magnitude"] = 1.63
targets["Gacrux"]["Spectral Type"] = "M3.5 III"


close_to_20 = []
for item in targets:
    decl = int(targets[item]["Dec"][1:3])
    print(decl)
    diff_in_decl = decl - 20
    if diff_in_decl < 0: 
        diff_in_decl *= -1
    close_to_20.append(diff_in_decl)


def brightest_and_closest_declination(dictionary):
    closest_to_20 = min(close_to_20)
    star_mag = dictionary[next(iter(dictionary))]["Magnitude"]
    for item in dictionary:
        if dictionary[item]["Magnitude"] < star_mag:
            star_mag = dictionary[item]["Magnitude"]
    for key in dictionary:
        if ((int(dictionary[key]["Dec"][1:3]) - 20)) < 0: 
            decl = (int(dictionary[key]["Dec"][1:3]) - 20) * -1
        else: 
            decl = (int(dictionary[key]["Dec"][1:3]) - 20)
        if dictionary[key]["Magnitude"] == star_mag and decl == closest_to_20:
            return key
        
print(brightest_and_closest_declination(targets))
        
#6: Scorpius!


