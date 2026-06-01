import streamlit as st
import pickle
import numpy as np

# Load model and dataframe
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

# Page Config
st.set_page_config(
    page_title="Laptop Price Predictor",
    page_icon="💻",
    layout="centered"
)

# Title
st.title("💻 Laptop Price Predictor")
st.markdown("Predict the price of a laptop based on its specifications.")

# Brand
company = st.selectbox(
    "Brand",
    options=df['Company'].unique(),
    index=None,
    placeholder="Select Brand"
)

# Type
type_name = st.selectbox(
    "Type",
    options=df['TypeName'].unique(),
    index=None,
    placeholder="Select Laptop Type"
)

# RAM
ram = st.selectbox(
    "RAM (in GB)",
    options=sorted(df['Ram'].unique()),
    index=None,
    placeholder="Select RAM"
)

# Weight
weight = st.number_input('Weight of the Laptop')

# Touchscreen
touchscreen = st.selectbox(
    "Touchscreen",
    ["No", "Yes"]
)

# IPS
ips = st.selectbox(
    "IPS Display",
    ["No", "Yes"]
)

# screen size 
screen_size = st.number_input('Screen Size')

# Resolution
resolution = st.selectbox(
    "Screen Resolution",
    options=[
        '1920x1080',
        '1366x768',
        '1600x900',
        '3840x2160',
        '3200x1800',
        '2880x1800',
        '2560x1600',
        '2560x1440',
        '2304x1440'
    ],
    index=None,
    placeholder="Select Screen Resolution"
)

# CPU
cpu = st.selectbox(
    "CPU",
    options=df['Cpu brand'].unique(),
    index=None,
    placeholder="Select CPU"
)

# HDD
hdd = st.selectbox(
    "HDD (in GB)",
    [0, 128, 256, 512, 1024, 2048]
)

# SSD
ssd = st.selectbox(
    "SSD (in GB)",
    [0, 8, 128, 256, 512, 1024]
)

# GPU
gpu = st.selectbox(
    "GPU",
    options=df['Gpu brand'].unique(),
    index=None,
    placeholder="Select GPU"
)

# OS
os = st.selectbox(
    "Operating System",
    options=df['os'].unique(),
    index=None,
    placeholder="Select Operating System"
)

# Predict Button
if st.button("Predict Price"):

    # Validation
    if company is None:
        st.error("⚠️ Please select a Brand.")
        st.stop()

    if type_name is None:
        st.error("⚠️ Please select a Laptop Type.")
        st.stop()

    if ram is None:
        st.error("⚠️ Please select RAM.")
        st.stop()

    if weight <= 0:
        st.error("⚠️ Please enter a valid laptop weight.")
        st.stop()

    if screen_size <= 0: 
        st.error("⚠️ Please enter a valid screen size.") 
        st.stop()

    if cpu is None:
        st.error("⚠️ Please select a CPU.")
        st.stop()

    if gpu is None:
        st.error("⚠️ Please select a GPU.")
        st.stop()

    if os is None:
        st.error("⚠️ Please select an Operating System.")
        st.stop()

    # Convert categorical values
    touchscreen = 1 if touchscreen == "Yes" else 0
    ips = 1 if ips == "Yes" else 0

    # Calculate PPI
    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])

    ppi = (((X_res ** 2) + (Y_res ** 2)) ** 0.5) / screen_size

    # Prepare query
    query = np.array([
        company,
        type_name,
        ram,
        weight,
        touchscreen,
        ips,
        ppi,
        cpu,
        hdd,
        ssd,
        gpu,
        os
    ]).reshape(1, 12)

    # Predict
    prediction = np.exp(pipe.predict(query)[0])

    st.success(
        f" Estimated Laptop Price: ₹ {prediction:,.2f}"
    )
