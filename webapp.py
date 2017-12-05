from flask import Flask, url_for, render_template, request, Markup, flash
import os, json, random

app = Flask(__name__)

with open('energy.json') as energy_data:
       energy = json.load(energy_data)

@app.route("/")
def render_main():
    return render_template('Home.html')

@app.route("/UsImprt")
def render_usprts():
	try:   
	    us_imp = request.args["year"]
	    return render_template('importEnergy.html', year = get_year_options(us_imp), response = us_importEngery(us_imp))
	except:
	    return render_template('importEnergy.html', year = get_year_options())

@app.route("/UsXprt")
def render_usprts2():
	try:   
	    us_xmp = request.args["year"]
	    return render_template('exportEnergy.html', year = get_year_options(us_xmp), response = us_xportEngery(us_xmp))
	except:
	    return render_template('exportEnergy.html', year = get_year_options())

@app.route("/UsPrCn")
def render_usprts3():
	try:   
	    us_pc = request.args["year"]
	    return render_template('prCnEnergy.html', year = get_year_options(us_pc), response = us_xportEngery(us_pc))
	except:
	    return render_template('prCnEnergy.html', year = get_year_options())
	
def get_year_options(default = None):
    options = ""
    state = ""
    for c in energy:
        if not str(c["year"]) == state:
            if str(c["year"]) == default:
              options += Markup("<option selected value=\"" + default + "\">" + default + "</option>")
              print('true')
            else:
              options += Markup("<option value=\"" + str(c["year"]) + "\">" + str(c["year"]) + "</option>")
            state = str(c["year"])

    return options

def us_importEngery(year):
       imprts = energy[1949-int(year)]["data"]["imports"]
       randKey = random.choice(list(imprts.keys()))

       return randKey + ": " + str(imprts[randKey]) + " Quadrillion BTUs"

def us_xportEngery(year):
       imprts = energy[1949-int(year)]["data"]["exports"]
       randKey = random.choice(list(imprts.keys()))

       return randKey + ": " + str(imprts[randKey]) + " Quadrillion BTUs"

def us_prCnEnergy(year)
	imprts = energy[1949-int(year)]["data"]["production"]
	randKey = random.choice(list(imprts.keys()))
	
	try:
	    imprts2 = energy[1949-int(year)]["data"]["consumption"][randKey]
	except:
	    imprts2 = "None"
	
	return "US Production: " +  randKey + ": " + str(imprts[randKey]) + " Quadrillion BTUs" + " US Consumtion" + randkey + imprts2
	return None

if __name__=="__main__":
    app.run(debug=False, port=54321)
