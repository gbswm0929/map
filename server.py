from flask import Flask, render_template, request, Response
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

@app.route("/")
def get_index():
    return render_template("maincopy.html")
    # return render_template("main.html")
@app.route("/apis/map")
def apimap():
    try:
        response = requests.get(f"https://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey={os.getenv("key")}&libraries=services")
        response.raise_for_status()
        if response.ok:
            return Response(response.text, mimetype="application/javascripts")
        else:
            return ''
    except requests.exceptions.RequestException as e:
        print("/apis/map error : ", e)
        return ''
@app.route("/hi")
def hello():
    return "hii"
        

if __name__ == "__main__":
    app.run()