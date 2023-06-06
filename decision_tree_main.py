import pickle

from fastapi import FastAPI
from joblib import dump, load
from sklearn import datasets, linear_model, svm
from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier

app = FastAPI()

DTC = load('decision_tree.ml')
print(DTC.predict([[2, 11]]))


@app.get("/")
async def root():
    return {"use /wine and two float numbers to get a prediction"}

@app.get("/wine")
async def root(alcohol,total_phenols):
    try:
          PC1=float(alcohol)
          PC2=float(total_phenols)
          prediction = int(DTC.predict([[alcohol, total_phenols]])[0])
          response = {"class": prediction}
    except ValueError:
          response = {"both variables need to float/integer"}   
   
    return response