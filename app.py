from flask import Flask, render_template      

import requests

url = 'https://api.chucknorris.io/jokes/random'

response = requests.get(url).text

start = response.index('value":') + 7
end = response.index('}')

quote = response[start:end]
file = open('static/css/test2.txt','w')
file.write(quote)
file.close()
x

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")    
    
@app.route("/nihal")
def nihal():
    return "Hello, Nihal"
    
@app.route("/norris")
def norris():
    return render_template("dailyquotes.html")
    
if __name__ == "__main__":
    app.run(debug=True) 