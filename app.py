import streamlit as st

def convert_units(value, from_unit, to_unit, category):
    conversions = {
        "Length": {
            "meters": 1,
            "kilometers": 0.001,
            "miles": 0.000621371,
            "feet": 3.28084,
            "inches": 39.3701,
            "centimeters": 100,
            "millimeters": 1000,
            "yards": 1.09361,
        },
        "Weight": {
            "kilograms": 1,
            "grams": 1000,
            "pounds": 2.20462,
            "ounces": 35.274,
            "stones": 0.157473,
        },
        "Temperature": "special"
    }
    
    if category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value
    else:
        return value * (conversions[category][to_unit] / conversions[category][from_unit])

st.title("Unit Converter")

category = st.selectbox("Choose a category", ["Length", "Weight", "Temperature"])

units = {
    "Length": ["meters", "kilometers", "miles", "feet", "inches", "centimeters", "millimeters", "yards"],
    "Weight": ["kilograms", "grams", "pounds", "ounces", "stones"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
}

from_unit = st.selectbox("From", units[category])
to_unit = st.selectbox("To", units[category])
value = st.number_input("Enter value", min_value=0.0, format="%.2f")

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, category)
    st.success(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")
