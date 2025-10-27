from flask import Flask, render_template
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

@app.route("/")
def get_index():
    return render_template("main.html", key=os.getenv("key"))

if __name__ == "__main__":
    app.run()