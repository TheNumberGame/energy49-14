from flask import Flask, url_for, render_template, request, Markup, flash
import os, json, random

app = Flask(__name__)

with open('energy.json') as energy_data:
       energy = json.load(energy_data)

@app.route("/")
def render_main():
    return render_template('Home.html')

def us_importEngery():
       imprts = energy['u\'imports']
       randKey = random.choice(list(imprts.keys()))
       
       return randKey + ": " imprts[randKey]
       

if __name__=="__main__":
    app.run(debug=False, port=54321)
