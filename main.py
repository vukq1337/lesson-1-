import requests
from bs4 import BeautifulSoup


def get_weather_data(city):
    url = f'https://www.google.com/search?q=weather+{city}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        forecast = []

        # Пошук елементів з прогнозом на тиждень
        forecast_elements = soup.find_all(class_='tAd8D')

        # Вивід температури та дня тижня
        for element in forecast_elements:
            day = element.find(class_='QrNVmd Z1VzSb CBTHCw').get_text()
            temperature = element.find(class_='wob_t').get_text()
            forecast.append((day, temperature))

        return forecast
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None


def main():
    city = input("Введіть місто: ")
    weather_data = get_weather_data(city)

    if weather_data:
        print(f"\nПрогноз погоди для міста {city} на тиждень:\n")
        for day, temperature in weather_data:
            print(f"{day}: {temperature}")


if __name__ == "__main__":
    main()