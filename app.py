import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Mechanical Engineering Toolkit", layout="wide")

# --- Header & Student Credentials ---
st.title("🛠️ Mechanical Unit Converter & Material Density Checker")

# This section was causing the error. I've simplified it to work perfectly.
st.markdown("---")
st.subheader("Developer Details")
st.write(f"**Name:** Malik Ashhad Nadeem")
st.write(f"**Roll Number:** 25-me-120")
st.markdown("---")

# Create two main tabs for organization
tab1, tab2 = st.tabs(["Unit Converter", "Material Density Checker"])

with tab1:
    st.header("📏 Mechanical Unit Converter")
    
    col1, col2 = st.columns(2)
    
    with col1:
        category = st.selectbox("Select Category", ["Length", "Mass", "Pressure", "Temperature"])
        input_value = st.number_input("Enter Value to Convert:", value=1.0, format="%.4f")

    with col2:
        result = 0.0
        unit = ""
        
        if category == "Length":
            mode = st.selectbox("Conversion Type", ["Meters to Feet", "Feet to Meters", "Inches to mm", "mm to Inches"])
            if mode == "Meters to Feet": result, unit = input_value * 3.28084, "ft"
            elif mode == "Feet to Meters": result, unit = input_value / 3.28084, "m"
            elif mode == "Inches to mm": result, unit = input_value * 25.4, "mm"
            else: result, unit = input_value / 25.4, "in"

        elif category == "Mass":
            mode = st.selectbox("Conversion Type", ["kg to lbs", "lbs to kg", "Gram to Ounce", "Ounce to Gram"])
            if mode == "kg to lbs": result, unit = input_value * 2.20462, "lbs"
            elif mode == "lbs to kg": result, unit = input_value / 2.20462, "kg"
            elif mode == "Gram to Ounce": result, unit = input_value * 0.035274, "oz"
            else: result, unit = input_value / 0.035274, "g"

        elif category == "Pressure":
            mode = st.selectbox("Conversion Type", ["Bar to PSI", "PSI to Bar", "Pascal to kPa", "MPa to PSI"])
            if mode == "Bar to PSI": result, unit = input_value * 14.5038, "psi"
            elif mode == "PSI to Bar": result, unit = input_value / 14.5038, "bar"
            elif mode == "Pascal to kPa": result, unit = input_value / 1000, "kPa"
            else: result, unit = input_value * 145.038, "psi"

        elif category == "Temperature":
            mode = st.selectbox("Conversion Type", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])
            if mode == "Celsius to Fahrenheit": result, unit = (input_value * 9/5) + 32, "°F"
            else: result, unit = (input_value - 32) * 5/9, "°C"

    st.metric(label="Converted Result", value=f"{result:.4f} {unit}")

with tab2:
    st.header("⚖️ Material Density Checker")
    
    # Standard Engineering Materials Data (kg/m^3)
    material_db = {
        "Steel (Mild)": 7850,
        "Aluminum (6061)": 2700,
        "Copper": 8960,
        "Brass": 8500,
        "Titanium": 4500,
        "Cast Iron": 7200,
        "Stainless Steel (304)": 8000,
        "Nylon": 1150,
        "ABS Plastic": 1040
    }
    
    selected_material = st.selectbox("Select Engineering Material:", list(material_db.keys()))
    density = material_db[selected_material]
    
    st.write(f"The standard density for **{selected_material}** is **{density} kg/m³**.")
    
    st.subheader("Quick Mass Calculator")
    vol = st.number_input("Enter Volume of Component (m³):", min_value=0.0, value=0.1, step=0.01)
    mass = vol * density
    st.success(f"Total Mass: **{mass:.2f} kg**")

# --- Footer ---
st.sidebar.markdown("---")
st.sidebar.write("Project for GitHub & Streamlit Cloud Deployment")
