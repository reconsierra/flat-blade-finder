
# Wiper Blade Selector App

This Streamlit web app helps users quickly find the correct wiper blades for a vehicle based on make, model, year, and wiper type. It uses your supplied Excel data for vehicle fitment and product number lookup.

## Features

- **Dropdown selectors** for Manufacturer, Model, and Year.
- **Wiper type selection**: Always offers Euro flat blade; Metal wiper blade is only shown if the vehicle’s adaptor clip is 'A'.
- **Displays** driver and passenger wiper lengths, adaptor clip, and the correct product numbers for the selected wiper type.
- **No Metal Option**: If the adaptor clip is not 'A', the Metal wiper blade option is hidden.

## How to Use

1. **Clone or download** this repository.
2. Ensure the following files are in the same directory:
    - `app.py`
    - `Car application data 2.xlsx`
3. Install the required Python packages:
    ```bash
    pip install streamlit pandas openpyxl
    ```
4. Run the app locally:
    ```bash
    streamlit run app.py
    ```
5. Or deploy directly to [Streamlit Cloud](https://share.streamlit.iour GitHub repo.

## File Structure

- `app.py` — The Streamlit app code.
- `Car application data 2.xlsx` — Your vehicle and product data.

## Customisation

- To add branding, colours, or extra features, edit `app.py` as needed.
- For help or feature requests, please contact the project maintainer.

---

**Enjoy your wiper blade selector app!**
