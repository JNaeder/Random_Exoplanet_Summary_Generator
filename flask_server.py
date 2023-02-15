from flask import Flask
from main import planet_summary_generator

app = Flask(__name__)


@app.route("/")
def main():
    print("Starting")
    planet_generator = planet_summary_generator()
    output = planet_generator.openai_test()
    return output

