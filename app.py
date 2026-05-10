import streamlit as st
import pandas as pd

# --- UI Header ---
st.set_page_config(page_title="Mechanical Unit Converter", layout="centered")
st.title("Mechanical Unit Converter & Material Density Checker")

# Student Information Display
st.sidebar.markdown("### Developer Details")
st.sidebar.info(f"**Name:** Malik Ashhad Nadeem\n\n**Roll Number:** 25-me-120")

# --- Section 1: Unit Converter ---
st.header("⚙️ Mechanical Unit Converter")
col1, col2 = st.columns(2)

with col1:
    value = st.number_input("Enter Value:", value=1.0)
    conversion_type = st.selectbox("Select Dimension:", ["Length", "Mass", "Pressure"])

with col2:
    if conversion_type == "Length":
        unit = st.selectbox("Convert From:", ["Meters to Feet", "Feet to Meters", "Inches to mm", "mm to Inches"])
        if unit == "Meters to Feet": result = value * 3.28084
        elif unit == "Feet to Meters": result = value / 3.28084
        elif unit == "Inches to mm": result = value * 25.4
        else: result = value / 25.4

    elif conversion_type == "Mass":
        unit = st.selectbox("Convert From:", ["kg to lbs", "lbs to kg"])
        if unit == "kg to lbs": result = value * 2.20462
        else: result = value / 2.20462

    elif conversion_type == "Pressure":
        unit = st.selectbox("Convert From:", ["Bar to PSI", "PSI to Bar", "Pa to kPa"])
        if unit == "Bar to PSI": result = value * 14.5038
        elif unit == "PSI to Bar": result = value / 14.5038
        elif unit == "Pa to kPa": result = value / 1000

st.success(f"**Result:** {result:.4f}")

---

# --- Section 2: Material Density Checker ---
st.header("⚖️ Material Density Checker")

# Dictionary of common engineering materials (Density in kg/m³)
materials = {
    "Steel": 7850,
    "Aluminum": 2700,
    "Copper": 8960,
    "Brass": 8500,
    "Titanium": 4500,
    "Concrete": 2400,
    "PVC": 1380,
    "Water": 1000
}

selected_material = st.selectbox("Select a Material:", list(materials.keys()))
density = materials[selected_material]

st.write(f"The density of **{selected_material}** is approximately **{density} kg/m³**.")

# Optional: Volume to Mass Calculator
st.subheader("Mass Calculator")
volume = st.number_input("Enter Volume (m³):", value=1.0, min_value=0.0)
calculated_mass = volume * density
st.info(f"Calculated Mass: **{calculated_mass:,.2f} kg**")
