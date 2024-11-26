#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
import pickle as pkl


import app as ap
import notebookFunction as nf
# from app import global_variable

# print(global_variable) 

# In[3]:


df = pd.read_csv(r"E:/DataScientist/DS-Used-Car-Price-Prediction/data/Cardetails.csv")
# df
print("FILE : research.py ")


# In[4]:


# df.shape
# df.head(3)


# In[5]:


# df.info()


# In[6]:


# df.describe()


# In[7]:


# df.isnull().sum()


# In[8]:


df.dropna(inplace=True)


# In[9]:


df.duplicated().sum()


# In[10]:


df.drop_duplicates(inplace=True)


# In[11]:


# df.shape


# In[12]:


# df.head(3)


# In[13]:


df1 = df.drop(columns=["max_power","torque"])


# In[14]:


# df1.head()


# In[15]:


# df1.info()


# In[16]:


# for col in df1.columns:
#     print(col)
#     print(df1[col].unique())
#     print("========================================")


# In[17]:


def get_carBrandNames(carName):
    carName = carName.strip(' ')
    carName = carName.split(' ')[0]
    return carName

def get_first(inp):
    inp = inp.strip(' ')
    inp = inp.split(' ')[0]
    return inp


# In[18]:


df1['name'] = df1['name'].apply(get_carBrandNames)
# df1


# In[19]:


df1['mileage'] = df1['mileage'].apply(get_first)
df1['engine'] = df1['engine'].apply(get_first)


# In[ ]:





# In[ ]:





# In[ ]:





# In[20]:


# for col in df1.columns:
#     print(col)
#     print(df1[col].unique())
#     print("========================================")


# In[21]:


df1['mileage'] = df1['mileage'].astype(float)
df1['engine'] = df1['engine'].astype(float)


# In[22]:


# df1.info()
df2 = df1.copy().reset_index(drop = True)
# print(df2.columns)
# df2.head(3)


# In[ ]:





# In[ ]:





# In[23]:


df2['year'] = df2['year'].astype('int64')
df2['selling_price'] = df2['selling_price'].astype('float64')
df2['km_driven'] = df2['km_driven'].astype('float64')


# In[24]:


# df2.info()


# In[25]:


df2.head(3)


# In[26]:


df2.columns


# 

# In[71]:


dummyDataFrame = df2.copy()
# query = df2['km_driven'].unique().tolist()
# print(query.sort())
# query



# In[ ]:





# In[ ]:





# ### Enconding

# In[28]:


categoriesCol = df2.select_dtypes(include=['object']).columns.tolist()
# print(categoriesCol)


# In[29]:


from sklearn.preprocessing import OneHotEncoder


# In[30]:


ohe = OneHotEncoder(sparse_output=False)


# In[31]:


encodedOHEArr = ohe.fit_transform(df2[categoriesCol])
encodedOHEDf = pd.DataFrame(encodedOHEArr,columns= ohe.get_feature_names_out(categoriesCol))


# In[32]:


df3 = pd.concat([df2,encodedOHEDf],axis=1)
df4 = df3.drop(columns=categoriesCol)

# df4


# In[ ]:





# In[33]:


# len(df4.select_dtypes(include=['float','int']).columns.tolist())


# In[34]:


col = ['year',	'selling_price',	'km_driven',	'mileage'	,'engine'	,'seats']
# sns.pairplot(data=df[col])
# sns.histplot(data=df['seats'],kde=True)


# In[35]:


# df4.columns


# In[ ]:





# ### Scaling - Standardization 

# In[36]:


df5 = df4.copy()

scalingIndependentVar = ['year','km_driven','mileage','engine','seats']
scalingDF = df5[scalingIndependentVar]  ## Extracted Scaling coloumns  only needed so take it 
# scalingDF
df6 = df5.drop(columns=scalingIndependentVar) ## 

from sklearn.preprocessing import StandardScaler

ss = StandardScaler()
scalerArr = ss.fit_transform(scalingDF[scalingIndependentVar])
scaledDF = pd.DataFrame(scalerArr,columns=ss.get_feature_names_out(scalingIndependentVar))

df7 = pd.concat([scaledDF,df6],axis=1)
historicalData = df7.copy()
# df7


# In[37]:


input_data = df7.drop(columns=['selling_price'])
output_data = df7['selling_price']
# print(input_data.shape)
# print(output_data.shape)

import warnings
warnings.filterwarnings('ignore')
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LogisticRegression,Lasso,Ridge
from sklearn.tree import DecisionTreeRegressor 
from sklearn.neighbors import KNeighborsRegressor  # 87+
from sklearn.ensemble import RandomForestRegressor  # 89+
from sklearn.svm import SVR 
from sklearn.ensemble import GradientBoostingRegressor #87+


# In[38]:


# print(input_data.columns)

x_train, x_test, y_train, y_test = train_test_split(input_data,output_data,test_size=0.2,random_state=42,shuffle=True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[39]:


model = KNeighborsRegressor(n_neighbors=4)
model.fit(x_train, y_train)

# model = GradientBoostingRegressor(random_state=0)
# model.fit(x_train, y_train)

# model =  RandomForestRegressor(random_state=0)
# model.fit(x_train,y_train)

print(model.score(x_train,y_train))
print(model.score(x_test,y_test))


# In[40]:


for i in range(10):
    index = i
    data = x_test.iloc[index, :].values.tolist()
    # print(data)
    # print()
    
    
    testing_data = pd.DataFrame([data],columns=['year', 'km_driven', 'mileage', 'engine', 'seats', 'name_Ambassador',
        'name_Ashok', 'name_Audi', 'name_BMW', 'name_Chevrolet', 'name_Daewoo',
        'name_Datsun', 'name_Fiat', 'name_Force', 'name_Ford', 'name_Honda',
        'name_Hyundai', 'name_Isuzu', 'name_Jaguar', 'name_Jeep', 'name_Kia',
        'name_Land', 'name_Lexus', 'name_MG', 'name_Mahindra', 'name_Maruti',
        'name_Mercedes-Benz', 'name_Mitsubishi', 'name_Nissan', 'name_Opel',
        'name_Renault', 'name_Skoda', 'name_Tata', 'name_Toyota',
        'name_Volkswagen', 'name_Volvo', 'fuel_CNG', 'fuel_Diesel', 'fuel_LPG',
        'fuel_Petrol', 'seller_type_Dealer', 'seller_type_Individual',
        'seller_type_Trustmark Dealer', 'transmission_Automatic',
        'transmission_Manual', 'owner_First Owner',
        'owner_Fourth & Above Owner', 'owner_Second Owner',
        'owner_Test Drive Car', 'owner_Third Owner'])

    predicted_value = model.predict(testing_data)
    # print("Predicted : ",predicted_value)


    actual_data_result = y_test.iloc[index]
    # print("Actual : ",actual_data_result)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## HyperParameter Tunning

# In[41]:


#GridSearchCV
# from sklearn.model_selection import GridSearchCV


# In[42]:


# param_dist = {
#     'n_neighbors':[i for i in range(8)],
#      'weights':['distance'],
#       'algorithm':['ball_tree'],
#        'leaf_size':[i for i in range(5)], 
#        'p':[i for i in range(4)]
# }

# cv = GridSearchCV(KNeighborsRegressor(), param_dist, cv=5)
# cv.fit(x_train, y_train)

# print("Tuned Decision Tree Parameters: {}".format(cv.best_params_))
# print("Best score is {}".format(cv.best_score_))


# In[43]:


# param_dist = {
#     'n_estimators':[i for i in range(5)],
#     'criterion':['squared_error', 'absolute_error', 'friedman_mse', 'poisson'],
#      'max_depth':[i for i in range(8)],
#       'min_samples_split':[i for i in range(8)],
#        'min_samples_leaf':[i for i in range(4)],
#         'max_features':['sqrt', 'log2'], 
#         'max_leaf_nodes':[i for i in range(4)]
# }

# cv = GridSearchCV(RandomForestRegressor(), param_dist, cv=5)
# cv.fit(x_train, y_train)

# print("Tuned Decision Tree Parameters: {}".format(cv.best_params_))
# print("Best score is {}".format(cv.best_score_))


# In[ ]:





# ## Model Export

# In[44]:


# import pickle as pkl

# pkl.dump(model,open("Model.pkl",'wb'))


# In[45]:


dataFrame = df
# dataFrame.head(2)


# In[46]:


# dataFrame['']


# In[47]:


# dataFrame['fuel'].unique()


# In[48]:


# dataFrame['seller_type'].unique()


# In[49]:


# dataFrame['transmission'].unique()


# In[50]:

##########################################################################################
# carName = "BMW"
# fuelType = "Disel"
# sellerType = 'Indudial'
# transmissionType = "Manaul"
# manufactureYear = 2011
# carOwner = 'First'
# kmsDriven = 25000
# carEngineCC = 1200
# carMileage = 25
# noOfSeats = 5

# SELLING_PRICE = 0
# InputDataDF = pd.DataFrame([[carName, manufactureYear, SELLING_PRICE, kmsDriven, fuelType, sellerType,transmissionType, carOwner, carMileage, carEngineCC, noOfSeats]],columns=['name', 'year', 'selling_price', 'km_driven', 'fuel', 'seller_type','transmission', 'owner', 'mileage', 'engine', 'seats'])


# In[51]:


# df2.head(1).info()


# In[ ]:





# In[52]:


# In[ ]:





# In[ ]:




