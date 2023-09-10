import streamlit as st
import streamlit.web.cli as stcli
import pickle
import numpy as np



def loaded_model():
    with open("model/saved_model_latest.pkl", "rb") as file:
        model = pickle.load(file)
    return model

model = loaded_model()
model_regressor = model["model"]
le_country_model = model["le_country"]
le_education_model = model["le_education"]

def show_predict_page():
    st.title("Software Developer Salary Prediction")

    st.write("""### Please put your information or profile to predict your salary""")

    countries = (
        "United States of America",
        "India",
        "United Kingdom of Great Britain and Northern Ireland",
        "Germany",
        "Canada",
        "Brazil",
        "France",
        "Spain",
        "Australia",
        "Netherland",
        "Poland",
        "Italy",
        "Russian Federation",
        "Sweden"
    )

    education = (
        "Less than a Bachelor",
        "Bachelor's degree",
        "Master's degree",
        "Advanced degree"
    )

    country = st.selectbox("Country", countries)
    education = st.selectbox('Education Level', education)
    yoe = st.slider("Years of Experience", 0, 50, 5)

    selected_profile = st.button("Calculate Salary")

    if selected_profile:
        x_selected = np.array([[country, education, yoe]])
        x_selected[:, 0] = le_country_model.transform(x_selected[:, 0])
        x_selected[:, 1] = le_education_model.transform(x_selected[:, 1])
        x_selected = x_selected.astype(float)

        salary = model_regressor.predict(x_selected)

        st.subheader(f"The estimated salary is ${salary[0]:.2f}")