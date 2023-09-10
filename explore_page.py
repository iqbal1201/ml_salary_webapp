import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def shorten_country(country, cut_off):
    country_map = {}
    for i in range(len(country)):
        if country.values[i] >= cut_off:
            country_map[country.index[i]] = country.index[i]
        else:
            country_map[country.index[i]] = 'Other'
    return country_map

def clean_experience(x):
    if x == "Less than 1 year":
        return 0.5
    if x == "More than 50 years":
        return 50
    return float(x)

def clean_education(x):
    if "Bachelor" in x:
        return "Bachelor's degree"
    if "Master" in x:
        return "Master's degree"
    if "Professional" in x or "doctoral" in x:
        return "Advanced degree"
    
    return "Less than a Bachelor"

@st.cache_data
def load_data():
    df = pd.read_csv("data/survey_results_public.csv")
    df = df[["Country", "EdLevel", "YearsCodePro", "ConvertedCompYearly"]]
    df = df.rename({"ConvertedCompYearly": "Salary"}, axis = 1)
    df = df[df["Salary"].notnull()]
    df = df.dropna()

    country_change = shorten_country(df.Country.value_counts(), 400)
    df['Country'] = df['Country'].map(country_change)
    df = df[df["Salary"] <= 200000]
    df = df[df['Country'] != "Other"]

    df["YearsCodePro"] = df["YearsCodePro"].apply(clean_experience)
    df["EdLevel"] = df["EdLevel"].apply(clean_education)
    return df


df = load_data()

def show_explore_page():
    st.title('Explore Salary for Software Engineer')

    st.write(
        """
    ### Stack Overflow Developer Survey 2022
        """
    )

    data = df['Country'].value_counts()

    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow = True, startangle=90)
    ax1.axis("equal")

    st.write("""### Number of data from difference countries""")

    st.pyplot(fig1)


### Create chart to show the mean of salary in each country
    st.write("""
             ### Mean Salary Based on Country
             """)
    data_salary = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data_salary)

### Create chart to show the mean of years of experience in each country
    st.write("""
        ### Mean of Years of Experience
             """)
    data_yoe = df.groupby(["Country"])["YearsCodePro"].mean()
    st.bar_chart(data_yoe)

### Create chart to show the mean of years of experience in each country
    st.write("""
        ### Mean Salary Based on Years of Experience
             """)
    data_salary_yoe = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(data = data_salary_yoe)