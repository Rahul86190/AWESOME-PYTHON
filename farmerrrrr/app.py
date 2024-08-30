# app.py
from flask import Flask, render_template, request
import joblib,pandas as pd
std_scaler=joblib.load("./models/std_scaler.lb")
kmeans_model=joblib.load("./models/kmeans_model.lb")
df=pd.read_csv("./models/filter_crops.csv")
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
    nitrogen = int(request.form.get('nitrogen'))
    phosphorus = int(request.form.get('phosphorus'))
    potassium = int(request.form.get('potassium'))
    temperature = float(request.form.get('temperature'))
    humidity =float( request.form.get('humidity'))
    ph = float(request.form.get('ph'))
    rainfall = float(request.form.get('rainfall'))
    
    # You can now use these variables to process or store the data
    print(f"N: {nitrogen}, K: {potassium}, P: {phosphorus}, Temp: {temperature}, Humidity: {humidity}, pH: {ph}, Rainfall: {rainfall}")
    
    unseen_data= [[nitrogen,phosphorus,potassium,temperature,humidity,ph,rainfall]]
    # return unseen_data

    trasnformer_data= std_scaler.transform(unseen_data)
    cluster=kmeans_model.predict(trasnformer_data)[0]
    # return f" your cluster no is{cluster}"
    suggestion_crops=list(df[df["cluster_no"]==cluster]["label"].unique())
    return f"suggestedd crops :{suggestion_crops}"


if __name__ == '__main__':
    app.run(debug=True)
