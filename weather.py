import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"


def get_weather_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch weather data.")
        return None


def get_temperature(date):
    data = get_weather_data()
    if data:
        for entry in data["list"]:
            if entry["dt_txt"].startswith(date):
                return entry["main"]["temp"]
        print("Data not available for the given date.")
    return None


def get_wind_speed(date):
    data = get_weather_data()
    if data:
        for entry in data["list"]:
            if entry["dt_txt"].startswith(date):
                return entry["wind"]["speed"]
        print("Data not available for the given date.")
    return None


def get_pressure(date):
    data = get_weather_data()
    if data:
        for entry in data["list"]:
            if entry["dt_txt"].startswith(date):
                return entry["main"]["pressure"]
        print("Data not available for the given date.")
    return None


def main():
    while True:
        print("Options:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            temp = get_temperature(date)
            if temp is not None:
                print(f"Temperature on {date}: {temp}°C")

        elif choice == "2":
            date = input("Enter date (YYYY-MM-DD): ")
            wind_speed = get_wind_speed(date)
            if wind_speed is not None:
                print(f"Wind Speed on {date}: {wind_speed} m/s")

        elif choice == "3":
            date = input("Enter date (YYYY-MM-DD): ")
            pressure = get_pressure(date)
            if pressure is not None:
                print(f"Pressure on {date}: {pressure} hPa")

        elif choice == "0":
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
