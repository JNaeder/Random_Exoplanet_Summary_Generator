from flask import Flask
from main import PlanetSummaryGenerator

app = Flask(__name__)


@app.route("/")
def main():
    print("Starting")
    planet_generator = PlanetSummaryGenerator()
    output = planet_generator.make_summary()
    return output

