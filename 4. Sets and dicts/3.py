n = int(input())
all_cities = []
for i in range(n):
    city = str(input())
    if city not in all_cities:
        all_cities.append(city)
        print("OK")
    else:
        print("REPEAT")
