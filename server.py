from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route("/")
def get_index():
    # return render_template("main.html")
    return "asdf"

if __name__ == "__main__":
    app.run(host="0.0.0.0")