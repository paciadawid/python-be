a = False

if not a:  # if a == False
    print("False")

b = [1, 2, 3]
c = 3

if c in b and c > 0:
    print("3 in list")

destination = "Nicosia"
destinations = {
    "Nicosia": 1980,
    "Reykjavik": 2900,
    "Chartum": None,
    "Gdansk": 485
}

if destination not in destinations.keys():
    print("No such destination")
elif destinations[destination]:
    if (distance := destinations[destination]) >= 2000:
        total_cost = 2 * distance
    else:
        total_cost = 2 * distance + 100
    print(f"Total cost for {destination} is {total_cost}")
else:
    print("No such destination")
