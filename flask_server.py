from flask import Flask
from main import planet_summary_generator
from multiprocessing import Process
import time

app = Flask(__name__)


def get_planet_info():
    start_time = time.time()
    print(f"Starting at {start_time}")
    planet_generator = planet_summary_generator()
    output = planet_generator.openai_test()
    print(output)
    print(f"Finished in {round(time.time() - start_time, 2)} seconds")
    app.redirect("/goodbye")


get_planet_process = Process(target=get_planet_info, daemon=False)


@app.route("/")
def main():
    get_planet_process.start()
    return "Hello"


@app.route("/goodbye")
def goodbye():
    return "Goodbye"


if __name__ == "__main__":
    app.run()
