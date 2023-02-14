from flask import Flask
from main import planet_summary_generator
app = Flask(__name__)


@app.route("/")
def main():
    print("Starting")
    planet_gen = planet_summary_generator()
    output = planet_gen.openai_test()
    return f"<p>{output}</p>"

@app.route("/goodbye")
def goodbye():
    return "Goodbye"


if __name__ == "__main__":
    app.run()
