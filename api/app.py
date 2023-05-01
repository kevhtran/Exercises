from flask import Flask, render_template, request
import requests
from secrets_1 import key

app = Flask(__name__)

API_BASE_URL = "https://www.mapquestapi.com/geocoding/v1"

res = requests.get('https://www.mapquestapi.com/geocoding/v1/address', params={'key': key, 'location': 'Denver, CO'})

@app.route("/")
def show_address_form():
    return render_template('address_form.html')

@app.route("/geocode")
def get_location():
    address = request.args["address"]
    res = requests.get(f"{API_BASE_URL}/address", params={'key': key, 'location': address})

    data = res.json()
    lat = data["results"][0]['locations'][0]['latLng']['lat']
    lng = data["results"][0]['locations'][0]['latLng']['lng']
    print('***')
    print(lat, lng)
