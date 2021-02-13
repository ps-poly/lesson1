weather = {
    "city": "Москва", 
    "temperature": "20"
    }
print(weather.get("city"))
weather["temperature"] = int(weather["temperature"]) - 5
print(weather)

print(weather.get("country"))
print(weather.get("country", "Россия"))
print(weather)


weather["date"] = "27.05.2019"
print(weather)
print(len(weather))

weather["street"] = "Lenina"
print(weather)
    