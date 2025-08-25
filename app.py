import streamlit as st
import pandas as pd

# Load Excel file
excel_file = 'Car application data 2.xlsx'
app_data = pd.read_excel(excel_file, sheet_name='Application list', engine='openpyxl')
data_lists = pd.read_excel(excel_file, sheet_name='data lists', engine='openpyxl', header=None)

# Clean up Manufacturer, Model, Year columns (remove NaN, convert to string)
app_data['Manufacturer'] = app_data['Manufacturer'].astype(str).str.strip()
app_data['Model'] = app_data['Model'].astype(str).str.strip()
app_data['Year'] = app_data['Year'].astype(str).str.strip()

# Extract Euro flat blade and Metal wiper blade product mappings
euro_start = data_lists[data_lists[0] == 'Euro flat blade'].index[0] + 2
metal_start = data_lists[data_lists[0] == 'Metal wiper blade'].index[0] + 2

euro_blades = data_lists.iloc[euro_start:metal_start-2].dropna()
euro_blades.columns = ['Length (mm)', 'Product Number']
euro_blades.set_index('Length (mm)', inplace=True)

metal_blades = data_lists.iloc[metal_start:].dropna()
metal_blades.columns = ['Length (mm)', 'Product Number']
metal_blades.set_index('Length (mm)', inplace=True)

st.title("Wiper Blade Selector")

# Dropdowns for Manufacturer, Model, Year
manufacturer = st.selectbox("Select Manufacturer", sorted(app_data['Manufacturer'].unique()))
filtered_models = app_data[app_data['Manufacturer'] == manufacturer]
model = st.selectbox("Select Model", sorted(filtered_models['Model'].unique()))
filtered_years = filtered_models[filtered_models['Model'] == model]
year = st.selectbox("Select Year", sorted(filtered_years['Year'].unique()))

# Get selected vehicle row
vehicle_row = filtered_years[filtered_years['Year'] == year].iloc[0]
driver_length = vehicle_row['Driver']
passenger_length = vehicle_row['passenger']
adaptor_clip = str(vehicle_row['adaptor clip']).strip()

# Display vehicle info
st.subheader("Vehicle Information")
st.write(f"**Driver Wiper Length:** {driver_length}")
st.write(f"**Passenger Wiper Length:** {passenger_length}")
st.write(f"**Adaptor Clip:** {adaptor_clip}")

# Determine available wiper types
wiper_types = ['Euro flat blade']
if adaptor_clip == 'A':
    wiper_types.append('Metal wiper blade')

selected_type = st.selectbox("Select Wiper Type", wiper_types)

# Function to get product number
def get_product_number(length_str, blade_df):
    try:
        length = int(str(length_str).replace('mm', '').strip())
        return blade_df.loc[length, 'Product Number']
    except:
        return "Not available"

# Display product numbers
st.subheader("Product Numbers")
if selected_type == 'Euro flat blade':
    driver_product = get_product_number(driver_length, euro_blades)
    passenger_product = get_product_number(passenger_length, euro_blades)
elif selected_type == 'Metal wiper blade':
    driver_product = get_product_number(driver_length, metal_blades)
    passenger_product = get_product_number(passenger_length, metal_blades)

st.write(f"**Driver Side Product Number ({selected_type}):** {driver_product}")
st.write(f"**Passenger Side Product Number ({selected_type}):** {passenger_product}")
