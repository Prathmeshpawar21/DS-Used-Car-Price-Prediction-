from flask import Flask, render_template, request, url_for, redirect, jsonify
import pandas as pd
import pickle as pkl
import numpy as np

import notebookFunction as nf
import research as rs

# from research import historicalData
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler


logo_url = "./static/logo.ico"
model = pkl.load(open("./model/Model.pkl", "rb"))
dataFrame = pd.read_csv("./data/Cardetails.csv")
app = Flask(__name__)


form_data = {}

@app.route('/', methods=['POST','GET'])
def base():
    FinalPredictedOutput=0

    print("FILE : app.py ")
    car_company_names = dataFrame["name"].apply(nf.get_carBrandNames).unique().tolist()
    car_company_names.sort()
    # Fetch Form Inputted Data
    if request.method == "POST":
        name = request.form.get("carcompany")
        fuel = request.form.get("fueltype")
        seller_type = request.form.get("sellertype")
        transmission = request.form.get("transmissiontype")
        year = request.form.get("manufacturedyear")
        owner = request.form.get("carowner")
        km_driven = request.form.get("kmsdriven")
        engine = request.form.get("carenginecc")
        mileage = request.form.get("carmileage")
        seats = request.form.get("noofseats")
        SELLING_PRICE = 0
    # DataFrameMaking
    # InputDataDF = pd.DataFrame([[name, year, SELLING_PRICE, km_driven, fuel, seller_type,transmission, owner, mileage, engine, seats]],columns=['name', 'year', 'selling_price', 'km_driven', 'fuel', 'seller_type','transmission', 'owner', 'mileage', 'engine', 'seats'])

    if request.method == "POST":
        fromDataDict = {
            "name": request.form.get("carcompany"),
            "fuel": request.form.get("fueltype"),
            "seller_type": request.form.get("sellertype"),
            "transmission": request.form.get("transmissiontype"),
            "owner": request.form.get("carowner"),
            "year": request.form.get("manufacturedyear"),
            "km_driven": request.form.get("kmsdriven"),
            "engine": request.form.get("carenginecc"),
            "mileage": request.form.get("carmileage"),
            "seats": request.form.get("noofseats"),
        }
        form_data = fromDataDict
    else:
        fromDataDict = {}

    form_data = fromDataDict

    test_columns = [
        "year",
        "km_driven",
        "mileage",
        "engine",
        "seats",
        "name_Ambassador",
        "name_Ashok",
        "name_Audi",
        "name_BMW",
        "name_Chevrolet",
        "name_Daewoo",
        "name_Datsun",
        "name_Fiat",
        "name_Force",
        "name_Ford",
        "name_Honda",
        "name_Hyundai",
        "name_Isuzu",
        "name_Jaguar",
        "name_Jeep",
        "name_Kia",
        "name_Land",
        "name_Lexus",
        "name_MG",
        "name_Mahindra",
        "name_Maruti",
        "name_Mercedes-Benz",
        "name_Mitsubishi",
        "name_Nissan",
        "name_Opel",
        "name_Renault",
        "name_Skoda",
        "name_Tata",
        "name_Toyota",
        "name_Volkswagen",
        "name_Volvo",
        "fuel_CNG",
        "fuel_Diesel",
        "fuel_LPG",
        "fuel_Petrol",
        "seller_type_Dealer",
        "seller_type_Individual",
        "seller_type_Trustmark Dealer",
        "transmission_Automatic",
        "transmission_Manual",
        "owner_First Owner",
        "owner_Fourth & Above Owner",
        "owner_Second Owner",
        "owner_Test Drive Car",
        "owner_Third Owner",
    ]
    
    if request.method == "POST":
        input_data = pd.DataFrame(
            {
                "name": [fromDataDict["name"]],
                "fuel": [fromDataDict["fuel"]],
                "seller_type": [fromDataDict["seller_type"]],
                "transmission": [fromDataDict["transmission"]],
                "owner": [fromDataDict["owner"]],
                "year": [fromDataDict["year"]],
                "km_driven": [fromDataDict["km_driven"]],
                "engine": [fromDataDict["engine"]],
                "mileage": [fromDataDict["mileage"]],
                "seats": [fromDataDict["seats"]],
            }
        )

        categorical_columns = ["name", "fuel", "seller_type", "transmission", "owner"]

        ohe = OneHotEncoder(sparse_output=False)
        encodedOHEArr = ohe.fit_transform(input_data[categorical_columns])
        encodedOHEDf = pd.DataFrame(
            encodedOHEArr, columns=ohe.get_feature_names_out(categorical_columns)
        )

        print(encodedOHEDf)

        # Add missing columns and set their values to 0
        for col in test_columns:
            if col not in encodedOHEDf.columns:
                encodedOHEDf[col] = 0

        # Ensure the column order matches the test data

        encodedOHEDf = encodedOHEDf[test_columns]

        encodedOHEDf.drop(
            columns=["year", "km_driven", "mileage", "engine", "seats"], inplace=True
        )

        # print(encodedOHEDf)

        nonEncodedData = input_data = pd.DataFrame(
            {
                "year": [fromDataDict["year"]],
                "km_driven": [fromDataDict["km_driven"]],
                "mileage": [fromDataDict["mileage"]],
                "engine": [fromDataDict["engine"]],
                "seats": [fromDataDict["seats"]],
            }
        )

        print("Print Here")

        # Scaling Data from formula var get from notebook like mean, std of historical Data
        records = [
            float(fromDataDict["year"]),
            float(fromDataDict["km_driven"]),
            float(fromDataDict["mileage"]),
            float(fromDataDict["engine"]),
            float(fromDataDict["seats"]),
        ]

        means = [
            float(2013.61114),
            float(73398.3377),
            float(19.4665848),
            float(1430.98586),
            float(5.43427125),
        ]
        stds = [
            float(3.89711144),
            float(58698.9054),
            float(4.04780053),
            float(493.432463),
            float(0.983731806),
        ]
        # Example inputted form data (ensure the order matches training data columns)
        # year, km_driven, engine, mileage, seats
        # print(records)
        # Scale the form data
        scaled_form_data = [
            (value - mean) / std for value, mean, std in zip(records, means, stds)
        ]

        print("Scaled Form Data:", scaled_form_data)

        inputScaledDataFrame = pd.DataFrame(
            {
                "year": [scaled_form_data[0]],
                "km_driven": [scaled_form_data[1]],
                "mileage": [scaled_form_data[2]],
                "engine": [scaled_form_data[3]],
                "seats": [scaled_form_data[4]],
            }
        )

        test_input_Data_for_model = pd.concat([inputScaledDataFrame, encodedOHEDf], axis=1)
        print(test_input_Data_for_model)

        if test_input_Data_for_model.columns.tolist() == test_columns:
            print("SIMILLAR COLOUMS")

        #################################################################################
        FinalPredictedOutput = model.predict(test_input_Data_for_model)
        FinalPredictedOutput = FinalPredictedOutput[0]
        print("Predicted Value : ", FinalPredictedOutput)
    #################################################################################

    # return render_template('./base.html', **fromDataDict, car_company_names=car_company_names,InputDataDF=InputDataDF,FinalPredictedOutput=FinalPredictedOutput)

    return render_template(
        "./base.html",
        car_company_names=car_company_names,
        FinalPredictedOutput=FinalPredictedOutput,
    )
    return


if __name__ == "__main__":
    app.run(debug=True)

# name year selling_price km_driven fuel seller_type    transmission owner mileage engine seats

# BMW  500   0             500      Diesel Trustmark Dealer Manual     500    500     500   500
