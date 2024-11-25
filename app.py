from flask import Flask, render_template, request, url_for, redirect
import pandas as pd
import pickle as pkl
import numpy as np
import notebookFunction as nf

model = pkl.load(open('./model/Model.pkl','rb'))
dataFrame = pd.read_csv('./data/Cardetails.csv')

app = Flask(__name__)

logo_url = './static/logo.png'
@app.route("/")
def homepage():
    car_company_names =  dataFrame['name'].apply(nf.get_carBrandNames).unique().tolist()
    car_company_names.sort()

    return render_template('./base.html',car_company_names = car_company_names)
    
    
    
    # print(car_company_names)
    
if __name__ == "__main__" : 
    app.run(debug=True)