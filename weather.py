import requests

city = input("City (in English): ")
url = f"https://wttr.in/{city}?format=j1"

try:
    data = requests.get(url, timeout=10).json()
    now = data["current_condition"][0]
    print("\nWeather in", city)
    print("Temp:", now["temp_C"], "C")
    print("Feels like:", now["FeelsLikeC"], "C")
    print("Humidity:", now["humidity"], "%")
    print("Status:", now["weatherDesc"][0]["value"])
except Exception:
    print("Could not get weather. Check the city name or your internet.")
