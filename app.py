from flask import Flask, render_template, request, url_for, redirect
import pandas as pd
import pickle as pkl
import numpy as np
import notebookFunction as nf

logo_url = './static/logo.ico'
model = pkl.load(open('./model/Model.pkl','rb'))
dataFrame = pd.read_csv('./data/Cardetails.csv')
app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def homepage():
    car_company_names =  dataFrame['name'].apply(nf.get_carBrandNames).unique().tolist()
    car_company_names.sort()
    # varibles
    carName = request.form.get("carcompany")
    fuelType = request.form.get("fueltype")
    sellerType = request.form.get("sellertype")
    transmissionType = request.form.get("transmissiontype")
    manufactureYear = request.form.get("manufacturedyear")
    carOwner = request.form.get("carowner")
    kmsDriven = request.form.get("kmsdriven")
    carEngineCC = request.form.get("carenginecc")
    carMileage = request.form.get("carmileage")
    noOfSeats = request.form.get("noofseats")
    
    SELLING_PRICE = 0
    
    
    # Fetch Form Inputted Data
    if request.method == "POST":
        fromData = {
            "carName": request.form.get("carcompany"),
            "fuelType": request.form.get("fueltype"),
            "sellerType": request.form.get("sellertype"),
            "transmissionType": request.form.get("transmissiontype"),
            "carOwner" : request.form.get("carowner"),
            "manufactureYear": request.form.get("manufacturedyear"),
            "kmsDriven": request.form.get("kmsdriven"),
            "carEngineCC": request.form.get("carenginecc"),
            "carMileage": request.form.get("carmileage"),
            "noOfSeats": request.form.get("noofseats")
        }
    else:
        fromData = {}
        
        
        
    # DataFrameMaking
    InputDataDF = pd.DataFrame([[carName, manufactureYear, SELLING_PRICE, kmsDriven, fuelType, sellerType,transmissionType, carOwner, carMileage, carEngineCC, noOfSeats]],columns=['name', 'year', 'selling_price', 'km_driven', 'fuel', 'seller_type','transmission', 'owner', 'mileage', 'engine', 'seats'])
    
    # df_reordered = InputDataDF.iloc[:, [0,4,10,6,1,2,3]]
    
    
    
    
    
    
    
    
        
# name year selling_price km_driven fuel seller_type    transmission owner mileage engine seats

# BMW  500   0             500      Diesel Trustmark Dealer Manual     500    500     500   500

        
        
    return render_template('./base.html', **fromData, car_company_names=car_company_names,InputDataDF=InputDataDF)

    
    
    
    
if __name__ == "__main__" : 
    app.run(debug=True)