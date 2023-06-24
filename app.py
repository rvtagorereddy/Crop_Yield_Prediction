import streamlit as st
import pandas as pd
import pickle

# Load the trained model
model = pickle.load(open('RandomForest.pkl', 'rb'))

def predict_crop_yield(parameters):
    # Prepare the input data for prediction
    data = pd.DataFrame(parameters, index=[0])

    # Make the prediction
    prediction = model.predict(data)

    return prediction[0]

def main():
    st.title("Crop Yield Prediction")
    st.write("Enter the following parameters to predict the crop yield:")

    # Get user input for parameters
    temperature = st.number_input("Temperature (in Celsius)")
    rainfall = st.number_input("Rainfall (in mm)")
    humidity = st.number_input("Humidity (in %)")
    ph = st.number_input("pH level")
    crop = st.text_input("Crop")

    parameters = {
        'Temperature': temperature,
        'Rainfall': rainfall,
        'Humidity': humidity,
        'pH': ph,
        'Crop': crop
    }

    if st.button("Predict"):
        # Call the prediction function
        prediction = predict_crop_yield(parameters)

        # Display the prediction
        st.write(f"Predicted crop yield for {crop}: {prediction} tons/ha")

if __name__ == '__main__':
    main()
