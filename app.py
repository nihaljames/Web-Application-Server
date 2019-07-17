from flask import Flask, render_template
import functions
  
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

@app.route("/template")
def template():
    return render_template("template.html")

@app.route("/newquote")
def newquote():
    return functions.getquote()
    
if __name__ == "__main__":
    app.run(debug=True) 

