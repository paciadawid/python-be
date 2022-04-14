destinations = {
    "Nicosia": 1980,
    "Reykjavik": 2900,
    "Chartum": None,
    "Gdansk": 485
}

for destination in destinations:
    print(destination)

for distances in destinations.values():
    print(distances)

for key, value in destinations.items():
    print(key, value)

for i in range(10):
    print(i)

for i in range(1, 11):
    print(i)

a = 0
while a < 10:
    print(a)
    a += 1  # a = a + 1

for i in range(10, 100):
    if not i % 2:  # if i % 2 == 0
        print(i)

for i in range(10, 100, 2):
    print(i)

a = 10

while a < 100:
    print(a)
    a += 2  # a = a + 2
