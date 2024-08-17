from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the model
model = joblib.load("./models/plane_model.lb")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/data_form')
def data_form():
    return render_template('data_form.html')

@app.route('/data', methods=["POST"])
def data():
    if request.method == "POST":
        try:
            # Retrieve form data with default values
            gender = request.form.get("gender", type=int, default=0)
            customerType = request.form.get("customerType", type=int, default=0)
            typeOfTravel = request.form.get("typeOfTravel", type=int, default=0)
            classOfTravel = request.form.get("classOfTravel", type=int, default=0)
            age = request.form.get("age", type=int, default=0)
            flightDistance = request.form.get("flightDistance", type=int, default=0)
            inflightEntertainment = request.form.get("inflightEntertainment", type=int, default=0)
            baggageHandling = request.form.get("baggageHandling", type=int, default=0)
            cleanliness = request.form.get("cleanliness", type=int, default=0)
            departureDelay = request.form.get("departureDelay", type=int, default=0)
            arrivalDelay = request.form.get("arrivalDelay", type=int, default=0)

            # Prepare data for prediction
            data_for_predict = [[
                gender, customerType, typeOfTravel, classOfTravel, age,
                flightDistance, inflightEntertainment, baggageHandling,
                cleanliness, departureDelay, arrivalDelay
            ]]

            # Predict satisfaction
            satisfaction_prediction = model.predict(data_for_predict)[0]

            # Print prediction for debugging
            print(f"Prediction: {satisfaction_prediction}")

            # Convert numerical labels to descriptive labels
            gender = "Male" if gender == 1 else "Female"
            customerType = "Loyal Customer" if customerType == 1 else "Disloyal Customer"
            typeOfTravel = "Business Travel" if typeOfTravel == 1 else "Personal Travel"
            classOfTravel = "Business" if classOfTravel == 1 else "Economy" if classOfTravel == 2 else "Economy Plus"

            # Render appropriate page based on prediction
            if satisfaction_prediction == 1:
                return render_template('satisfied_page.html',
                                       gender=gender, customerType=customerType,
                                       typeOfTravel=typeOfTravel, classOfTravel=classOfTravel,
                                       age=age, flightDistance=flightDistance,
                                       inflightEntertainment=inflightEntertainment,
                                       baggageHandling=baggageHandling,
                                       cleanliness=cleanliness,
                                       departureDelay=departureDelay,
                                       arrivalDelay=arrivalDelay)
            else:
                return render_template('unsatisfied_page.html',
                                       gender=gender, customerType=customerType,
                                       typeOfTravel=typeOfTravel, classOfTravel=classOfTravel,
                                       age=age, flightDistance=flightDistance,
                                       inflightEntertainment=inflightEntertainment,
                                       baggageHandling=baggageHandling,
                                       cleanliness=cleanliness,
                                       departureDelay=departureDelay,
                                       arrivalDelay=arrivalDelay)

        except Exception as e:
            return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)
