import streamlit as st
import pandas as pd
import pickle
import numpy as np

st.title("Prediction of Price of Used cars")

st.header("Year Of Registration")
Reg_year = st.number_input('Year',value=1980)
Reg_month = st.number_input('month',value=1)

Age = (2021 - Reg_year)
month = abs(1-Reg_month)

if st.checkbox("Age of the vehicle"):
    st.write("{} **Years** {} **months**".format(Age,month))

st.header("Vehicle Type")
vehicle_type = st.selectbox('Type',("SUV","limousine","bus",
                                            "small car","station wagon",
                                            'cabrio','coupe','other'))
st.header("Fuel Type")
fuel_type = st.selectbox('Type',("Petrol","Diesel","LPG",
                                            "Hybrid","Electro",'CNG','other'))

st.header("Gearbox")
gearbox = st.selectbox('Type',("Automatic","Manual"))

st.header("Power PS")
powerps = st.number_input('Power PS of Vehicle',value=1)

st.header("Kilometer")
km = st.number_input('Kilometer',value=1)

st.header("Brand of the Vehicle")
brand = st.selectbox('Brand of the Vehicle',("BMW","Volvo","Volkswagen",
                                             "Seat","Mercedez Benz","Opel",
                                             "Skoda","Toyota","Nissan","Mazda",
                                             "Mistibushi","Audi","Fiat",
                                             "Land Rover","Subaru","Mini",
                                             "Jeep","Ford","Chervolet",
                                             "Hyundai","Honda","Jaguar",
                                             "Suzuki","Porsche",'Renault','Sonstige_autos'))

st.header("Condition of Vehicle")
Repair = st.selectbox('Repaired or not',('Yes','No'))


#powerps
power = pd.DataFrame([powerps],columns=['powerps'])

#KM
kilo = pd.DataFrame([km],columns=['km'])

#Age Variable
A = Age+(Reg_month/12)
Age1 = pd.DataFrame([A],columns=['Age'])

#gearbox one hot encoding
if (gearbox=='Manual'):
    gear=[[0]]
else:
    gear=[[1]]
gear = pd.DataFrame(gear,columns=['Gear'])

#Vehicle type one hot encoding
if (vehicle_type=='SUV'):
    vehicle = [[0,0,0,0,0,0,1]]
elif(vehicle_type=='cabrio'):
    vehicle = [[1,0,0,0,0,0,0]]
elif(vehicle_type=='coupe'):
    vehicle = [[0,1,0,0,0,0,0]]
elif(vehicle_type=='limousine'):
    vehicle = [[0,0,1,0,0,0,0]]
elif(vehicle_type=='others'):
    vehicle = [[0,0,0,1,0,0,0]] 
elif(vehicle_type=='small car'):
    vehicle = [[0,0,0,0,1,0,0]]  
elif(vehicle_type=='station wagon'):
    vehicle = [[0,0,0,0,0,1,0]] 
elif(vehicle_type=='bus'):
    vehicle = [[0,0,0,0,0,0,0]]
vehicle_cols=['cabrio','coupe','limousine','others','small car','station wagon','SUV']
vehicle = pd.DataFrame(vehicle,columns=vehicle_cols)

#Fuel Type one hot encoding
if (fuel_type=='Diesel'):
    fuel = [[1,0,0,0,0,0]]
elif(fuel_type=='Electro'):
    fuel = [[0,1,0,0,0,0]]
elif(fuel_type=='Hybrid'):
    fuel = [[0,0,1,0,0,0]]
elif(fuel_type=='LPG'):
    fuel = [[0,0,0,1,0,0]]
elif(fuel_type=='other'):
    fuel = [[0,0,0,0,1,0]] 
elif(fuel_type=='Petrol'):
    fuel = [[0,0,0,0,0,1]]  
elif(fuel_type=='CNG'):
    fuel = [[0,0,0,0,0,0]] 
fuel_cols=['Diesel','Electro','Hybrid','LPG','other','Petrol']
fuel = pd.DataFrame(fuel,columns=fuel_cols)

#Brand one hot encoding
if (brand=='Audi'):
    bran = [[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
elif (brand=='BMW'):
    bran = [[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
elif (brand=='Chervolet'):
    bran = [[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
elif (brand=='Fiat'):
    bran = [[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
elif (brand=='Ford'):
    bran = [[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
elif (brand=='Honda'):
    bran = [[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
elif (brand=='Hyndai'):
    bran = [[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
elif (brand=='Jaguar'):
    bran = [[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
elif (brand=='Jeep'):
    bran = [[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
elif (brand=='Kia'):
    bran = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
elif (brand=='Land Rover'):
    bran = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
elif (brand=='Mazda'):
    bran = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
elif (brand=='Mercedez Benz'):
    bran = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
elif (brand=='Mini'):
    bran = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
elif (brand=='Mistibushi'):
    bran = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
elif (brand=='Nissan'):
    bran = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
elif (brand=='Opel'):
    bran = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
elif (brand=='Porsche'):
    bran = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]]
elif (brand=='Renault'):
    bran = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]]
elif (brand=='Seat'):
    bran = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]]
elif (brand=='Skoda'):
    bran = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]]
elif (brand=='Sonstige_autos'):
    bran = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]]
elif (brand=='Subaru'):
    bran = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]]
elif (brand=='Suzuki'):
    bran = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]]
elif (brand=='Tayota'):
    bran = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]]
elif (brand=='Volkswagen'):
    bran = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]]
elif (brand=='Volvo'):
    bran = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]

bran = pd.DataFrame(bran)

#condition of vehicle one hot encoding
if(Repair=='Yes'):
    repair=[[1]]
else:
    repair=[[0]]

repair = pd.DataFrame(repair)
#creating Dataframe of given Data
d = pd.DataFrame(pd.concat([power,kilo,Age1,vehicle,gear,fuel,bran,repair],axis=1))

#Showing given data
data = [[Age,fuel_type,vehicle_type,powerps,km,gearbox]]
col = [['Age','Fuel Type','Vehicle Type','Power PS','KM','Gearbox']]
df = pd.DataFrame(data,columns=col)
if st.checkbox("Given data"):
    st.dataframe(df)

pickle_in = open("model.pkl","rb")
model=pickle.load(pickle_in)

Prediction = np.round(np.exp(model.predict(d)),2)

if st.checkbox('Predict'):
    st.header('Predicted Price of the Vehicle is {}'.format(Prediction))
if st.button('About'):
   st.write('Created by SUMANTHA.NTS dated 03/01/2021')