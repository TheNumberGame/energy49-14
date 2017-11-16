from flask import Flask, url_for, render_template, request, Markup, flash
import os, json, random

app = Flask(__name__)

with open('energy.json') as energy_data:
       energy = json.load(energy_data)

@app.route("/")
def render_main():
    return render_template('Home.html')

@app.route("/importEnergy")
def render_import():
       us_imp = request.args["year"]
       return rendr_template('importEnergy.html', year = get_year_options(us_imp))

def get_year_options(default = None):
    
    options = ""
    state = ""
    for c in energy:
        if not c["year"] == state:
            if c["year"] == default:  
              options += Markup("<option selected value=\"" + c["year"] + "\">" + c["year"] + "</option>")
            else:
              options += Markup("<option value=\"" + c["year"] + "\">" + c["year"] + "</option>")
            state = c["year"]
            #print(options)
    
    return options

def us_importEngery(year):
       imprts = energy[1949-year]["imports"]
       randKey = random.choice(list(imprts.keys()))
       
       return randKey + ": " + imprts[randKey] + " Quadrillion BTUs" 
       

if __name__=="__main__":
    app.run(debug=False, port=54321)
