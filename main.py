import requests
import random
import time
import os
import dotenv
import openai


class planet_summary_generator:
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

    def make_openai_prompt(self):
        planet_data = self.random_planet()
        planet_name = planet_data["pl_name"]
        host_name = planet_data["hostname"]

        prompt = f"Write a summary about this exoplanet. Planet's name is {planet_name} and it's host star's name is {host_name}"
        return prompt

    def openai_test(self):
        dotenv.load_dotenv()
        api_key = os.getenv("OPENAI_API")
        organization = os.getenv("OPENAI_ORG")
        openai.api_key = api_key
        openai.organization = organization
        print("Keys", api_key, organization)
        prompt = self.make_openai_prompt()
        completion = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=500)
        return completion.choices[0].text


if __name__ == "__main__":
    print("Request Starting...")
    start_time = time.time()
    planet_gen = planet_summary_generator()
    planet_gen.openai_test()
    time_taken = time.time() - start_time
    print(f"This request took {round(time_taken, 2)} seconds")
