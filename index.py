from dotenv import load_dotenv
from flask import Flask
from flask import render_template
import requests
import os

load_dotenv()


app = Flask(__name__)

api_key = os.getenv("API_KEY")

@app.route('/market')
def main():
    url = f"http://api.coinlayer.com/live?access_key={api_key}&target=USD"
    response = requests.get(url)
    response_json = response.json()
    rates = response_json['rates']
    

    # url2 = "http://api.coinlayer.com/list?access_key=74a0e1a778ba10d0e20349b28f9fcbae"
    # response2 = requests.get(url2)
    # response_json2 = response2.json()
    # # icon_url = response_json2['crypto'][rates]
    
    #return rates.keys()
    return render_template('market.html',rates=rates)

@app.route('/')
def home():
    url = f"http://api.coinlayer.com/live?access_key={api_key}&target=USD"
    response = requests.get(url)
    response_json = response.json()
    rates = response_json['rates']
    btc_value = rates["BTC"]
    eth_value = rates["ETH"]
    mkr_value = rates["MKR"]
    return render_template("home.html", btc=btc_value,eth=eth_value,mkr=mkr_value )

@app.route('/about')
def aboutUs():
    return render_template("aboutus.html")

@app.route('/contact')
def contactUs():
    return render_template("contact.html")



if __name__ == "__main__":
    app.debug = True
    app.run(host='127.0.0.1', port=8000)