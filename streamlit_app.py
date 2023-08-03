
import requests

def get_population_data(country):
    base_url = "https://api.population.io/1.0/population/"
    url = f"{base_url}{country}/today-and-tomorrow/"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def show_population_data(country_data):
    if country_data is not None:
        country_name = country_data['country']
        population_today = country_data['total_population'][0]['population']
        population_tomorrow = country_data['total_population'][1]['population']

        print(f"Population data for {country_name}:")
        print(f"Today's population: {population_today}")
        print(f"Tomorrow's projected population: {population_tomorrow}")
    else:
        print("No data available.")

if __name__ == "__main__":
    # Replace 'your_country_code' with the desired country code (e.g., 'us', 'in', 'gb', etc.)
    country_code = 'your_country_code'

    population_data = get_population_data(country_code)
    show_population_data(population_data)
