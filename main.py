import requests
import random
import time
import os
import dotenv
import openai


class PlanetSummaryGenerator:
    def __init__(self):
        """
        Initialize class parameters
        """
        self._nasa_base_url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+"
        self._nasa_query_end = "+from+ps&format=json"
        self._nasa_query_columns = ["pl_name"]
        self._all_planets = self.set_planets()

    def set_planets(self):
        """
        Returns a list of planet names back from NASA Exoplanet API.
        """
        start_time = time.time()
        url = f"{self._nasa_base_url}{','.join(self._nasa_query_columns)}{self._nasa_query_end}"
        response = requests.get(url).json()
        print(f"Get Planet data in {round(time.time() - start_time, 2)} seconds.")
        return response

    def random_planet(self):
        """
        Returns a random planet from the array of all planets.
        """
        planet_length = len(self._all_planets)
        random_index = random.randint(0, planet_length)
        return self._all_planets[random_index]

    def make_openai_prompt(self):
        """
        Returns a generated prompt from the planet data to give to the Openai API.
        """
        planet_data = self.random_planet()
        planet_name = planet_data["pl_name"]
        prompt = f"Write a summary about the exoplanet {planet_name}."
        return prompt

    def make_summary(self):
        """
        Main function. Gets API keys, creates a prompt and feeds it to the OpenAI API.
        Returns the Generated Text from OpenAI.
        """
        start_time = time.time()
        dotenv.load_dotenv()
        api_key = os.getenv("OPENAI_API")
        organization = os.getenv("OPENAI_ORG")
        openai.api_key = api_key
        openai.organization = organization
        prompt = self.make_openai_prompt()
        completion = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=500)
        print(f"Finished making summary in {round(time.time() - start_time, 2)} seconds")
        return completion.choices[0].text


if __name__ == "__main__":
    print("Request Starting...")
    process_start_time = time.time()
    planet_gen = PlanetSummaryGenerator()
    print(planet_gen.make_summary())
    time_taken = time.time() - process_start_time
    print(f"This request took {round(time_taken, 2)} seconds")
