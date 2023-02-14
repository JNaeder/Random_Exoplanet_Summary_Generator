import requests
import random
import time


class planet_poem_generator:
    def __init__(self):
        self._nasa_base_url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+"
        self._nasa_query_format = "&format=json"
        self._nasa_query_table = "+from+ps+"
        self._nasa_query_columns = ["pl_name", "hostname"]
        self._all_planets = self.set_all_planets()

    def get_all_planets(self):
        return self._all_planets

    def set_all_planets(self):
        url = self._nasa_base_url + ",".join(
            self._nasa_query_columns) + self._nasa_query_table + self._nasa_query_format
        # print(url)
        response = requests.get(url)
        return response.json()

    def random_planet(self):
        planet_length = len(self._all_planets)
        random_index = random.randint(0, planet_length)
        return self._all_planets[random_index]

    def make_openai_prompt(self, planet_data):
        planet_name = planet_data["pl_name"]
        host_name = planet_data["hostname"]

        prompt = f"Write a summary about this exoplanet. Planet's name is {planet_name} and it's host star's name is " \
                 f"{host_name}"
        print(prompt)



if __name__ == "__main__":
    start_time = time.time()
    planet_gen = planet_poem_generator()
    # planet_gen.set_all_planets()
    random_planet = planet_gen.random_planet()
    planet_gen.make_openai_prompt(random_planet)
    print(time.time() - start_time)
