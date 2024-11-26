from flask import Flask, render_template, request, url_for, redirect
import pandas as pd
import pickle as pkl
import numpy as np
from sklearn.preprocessing import OneHotEncoder

import app as ap
import research as rs

print("FILE : notebookFunction.py ")
dataFrame = pd.read_csv('./data/Cardetails.csv')


def get_carBrandNames(carName):
    carName = carName.strip(' ')
    carName = carName.split(' ')[0]
    return carName

def get_first(inp):
    inp = inp.strip(' ') 
    inp = inp.split(' ')[0]
    return inp

car_company_names =  dataFrame['name'].apply(get_carBrandNames).unique().tolist()
car_company_names.sort()






if __name__ == "__main__":
    pass




