"""from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "bdf353a99889428ea43160329261405"
    
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/getweather",methods=["POST"])
def weather():
    location = request.form.get("city", "").strip() # strip eliminates the space in between

    if not location:
        return render_template(
            "index.html",
            error = "Please enter a city name"
        )
    try:
        weather_url = (
            f"https://api.weatherapi.com/v1/current.json"
            f"?key={API_KEY}&q={location}"
        )

        # SSL-safe request
        response = request.get(weather.url)
        weather_data = response.json()

        # check API error
        if "error" in weather_data:

            return render_template(
                "index.html",
                error = weather_data["error"]["message"]
            )
        
        data = {

            "location":
            weather_data["location"]["name"],

            "country":
            weather_data["location"]["country"],

            "temp":
            weather_data["current"]["temp_c"],

            "condition":
            weather_data["current"]["condition"]["text"],

            "icon":
            weather_data["current"]["condition"]["icon"]
        }

        return render_template(
            "index.html",
            data = data
        )
    
    except Exception as e:

        return render_template(
            "index.html",
            error = str(e)
        )
    
if __name__ == "__main__":

    app.run(debug=True, host="0.0.0.0",port=8080) """

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "HELLO FLASK"

if __name__ == "__main__":
    app.run(debug=True, port=8080)