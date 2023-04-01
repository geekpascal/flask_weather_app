import os
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

SECRET_KEY = os.getenv("MY_SECRET")
API_KEY = os.getenv("API_KEY")

def get_weather_results(zip_code, api_key):
    api_url = f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code}&units=metric&appid={api_key}"
    r = requests.get(api_url)
    return r.json()
    

@app.route('/')
def wth_homepage():
    return render_template('home.html')

@app.route('/results', methods=['POST'])
def wth_results():
    zip_code = request.form['zipCode']
    data = get_weather_results(zip_code, API_KEY)
    # return data
    temp = "{0:.2f}".format(data["main"]["temp"])
    feels_like = "{0:.2f}".format(data["main"]["feels_like"])
    weather = data["weather"][0]["main"]
    location = data["name"]
    return render_template("results.html", temp=temp,
                           location=location, weather=weather,
                           feels_like=feels_like)


  
if __name__ == "__main__":
    app.run()