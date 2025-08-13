import streamlit as st

# set page config
st.set_page_config(page_title="BMI Calculator", page_icon = "💪", layout = "centered")

# Title and Description
st.title("🧮BMI Calculator")
st.markdown('''
Welcome to BMI Calculator App! 
This Tool helps you understand you BMI and health status based on weight and height.
''')

# User Input
st.markdown("## ℹ️Enter Your Information")
col1,col2 = st.columns(2, gap = "large")
with col1:
    height_unit=st.radio("**Select height unit:**", ["Meter", "Feet"])
    height=st.number_input("**Height**", min_value = 1.0, format = "%.2f", key = "height_input")
with col2:
    weight_unit=st.radio("**Select weight unit:**", ["Pound", "Kilogram"])
    weight=st.number_input("**Weight**", min_value = 1.0, format = "%.2f", key = "weight_input")

# Calculation
def calc_bmi(height_unit,height,weight_unit,weight):
    if height_unit == "Feet":
        height_m = height / 3.28084
    else:
        height_m = height
    if weight_unit == "Pound":
        weight_m = weight * 0.4354
    else:
        weight_m = weight
    return weight_m / (height_m ** 2)

# Button to show
if st.button("Click to calculate"):
    if height <= 0 or weight <= 0:
        st.error("Please enter values greater than zero")
    else:
        bmi=calc_bmi(height_unit,height,weight_unit,weight)
        st.success(f"Your BMI is {bmi:.2f}")

# Interpretation
    if bmi < 16:
        st.error("🚨Extremly underweight")
    elif 16 <= bmi < 18.5:
        st.warning("⚠️Underweight")
    elif 18.5 <= bmi < 25:
        st.success("✅Healthy")
    elif 25 <= bmi < 30:
        st.warning("⚠️Overweight")
    else:
        st.error("🚨Extremly overweight")


# Footer
st.markdown("---")
st.caption("💡Tip: Maintain a healthy BMI to support overall well-being")

