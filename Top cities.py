cities = {
    "Lagos": 15000000,
    "Cairo": 20000000,
    "Nairobi": 4500000,
    "Johannesburg": 5500000
}

sorted_cities = sorted(cities.items(), key=lambda x: x[1], reverse=True)

for city in sorted_cities[:3]:
    print(city)