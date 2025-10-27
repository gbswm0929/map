from flask import Flask, render_template
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

@app.route("/")
def get_index():
    return render_template("main.html", key=os.getenv("key"))
@app.route("/hi")
def get_hi():
    return "hi, hello"

if __name__ == "__main__":
    app.run()