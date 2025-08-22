import streamlit as st
import pandas as pd

# Load data
data = pd.read_csv("vehicle_data.csv")

st.title("Vehicle Selector App")

# Dropdowns
make = st.selectbox("Select Make", sorted(data["Make"].unique()))
model = st.selectbox("Select Model", sorted(data[data["Make"] == make]["Model"].unique()))
year = st.selectbox("Select Year", sorted(data[(data["Make"] == make) & (data["Model"] == model)]["Year"].unique()))

# Filter and display
vehicle = data[(data["Make"] == make) & (data["Model"] == model) & (data["Year"] == year)]
if not vehicle.empty:
    row = vehicle.iloc[0]
    st.subheader("Vehicle Details")
    st.write(f"**Fuel Type:** {row['Fuel Type']}")
    st.write(f"**Transmission:** {row['Transmission']}")
    st.write(f"**Length (mm):** {row['Length (mm)']}")
    st.write(f"**Product Number:** {row['Product Number']}")
else:
    st.warning("No matching vehicle found.")
