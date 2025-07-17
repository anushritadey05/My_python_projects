import streamlit as st # type: ignore
st.title("UNIT CONVERTOR APP🏋️📏🕐")
st.markdown("### Converts length,breadth and time instantly!!")
st.write("Welcome! Select a category, enter a value and get the converted result in real time")

category = st.selectbox("Choose a category", ["Length","Weight","Time"])

def convert_units(category,value,unit):
    if category == "Length":
        if unit== "Kilometres to Miles":
            return value * 0.621371
        elif unit== "Miles to Kilometres":
            return value/0.621371
    
    elif category == "Weight":
        if unit== "Kilograms to Pounds":
            return value * 2.20462
        elif unit== "Pounds to Kilograms":
            return value/2.20642
        
    elif category == "Time":
        if unit== "Seconds to Minutes":
            return value/60
        elif unit== "Minutes to Seconds":
            return value*60
        elif unit== "Minutes to Hours":
            return value/60
        elif unit== "Hours to Minutes":
            return value*60
        elif unit== "Hours to Days":
            return value/24
        elif unit== "Days to Hours":
            return value * 24
        
    
    
if category == "Length":
    unit = st.selectbox("Select Convertion", ["Kilometres to Miles","Miles to Kilometres"])

if category == "Weight":
    unit = st.selectbox("Select Convertion", ["Kilograms to Pounds","Pounds to Kilograms"])

if category == "Time":
    unit = st.selectbox("Select Convertion", ["Seconds to Minutes","Minutes to Seconds","Minutes to Hours","Hours to Minutes","Hours to Days","Days to Hours"])

value = st.number_input("Enter the value to convert:")

if st.button("Convert"):
     result = convert_units(category,value,unit) 
     st.success(f"The result is {result:.2f}")