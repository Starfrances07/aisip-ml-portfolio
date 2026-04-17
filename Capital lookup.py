capitals = {
    "Nigeria": "Abuja",
    "Kenya": "Nairobi",
    "Ghana": "Accra"
}

country = input("Enter country: ")

if country in capitals:
    print(capitals[country])
else:
    print("Country not found")