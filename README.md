# 💻 Laptop Price Predictor App

An end-to-end Machine Learning project that predicts laptop prices based on hardware and software specifications. The project covers data preprocessing, feature engineering, exploratory data analysis (EDA), model training, evaluation, and deployment using Streamlit.

---

## 🚀 Live Demo

🔗 Demo App: https://laptoppricepredictorapp-mobim53z7zzsfhbq5h5toq.streamlit.app/


---

## 📌 Project Overview

The objective of this project is to predict laptop prices using specifications such as:

* Brand
* Laptop Type
* RAM
* Processor
* Storage
* GPU
* Operating System
* Display Features
* Weight

Users can select laptop specifications through an interactive Streamlit interface and instantly receive an estimated laptop price.

---


## 🔍 Exploratory Data Analysis (EDA)

Performed extensive EDA to understand relationships between laptop specifications and prices.

### Key Insights

* Gaming and Workstation laptops are generally more expensive.
* Premium brands such as Apple, MSI, LG, and Razer have higher average prices.
* RAM has a strong positive relationship with laptop prices.
* SSD storage significantly increases laptop prices.
* High-resolution displays and higher PPI values are associated with premium laptops.
* Touchscreen and IPS displays positively impact laptop prices.

---

## ⚙️ Feature Engineering

### Display Features

Extracted:

* Touchscreen
* IPS Display
* Resolution Width
* Resolution Height
* PPI (Pixels Per Inch)

### CPU Features

Categorized processors into:

* Intel Core i3
* Intel Core i5
* Intel Core i7
* Other Intel Processor
* AMD Processor

### Storage Features

Converted Memory column into:

* HDD
* SSD
* Hybrid Storage
* Flash Storage

### GPU Features

Extracted GPU Brand from raw GPU information.

---

## 🤖 Machine Learning Models Evaluated

Multiple regression algorithms were trained and compared.

| Model | R² Score (%) |
|--------|-------------:|
| Linear Regression | 80.73 |
| Ridge Regression | 81.27 |
| Lasso Regression | 80.71 |
| K-Nearest Neighbors Regressor | 80.26 |
| Decision Tree Regressor | 84.05 |
| Support Vector Regressor (SVR) | 80.83 |
| Random Forest Regressor | **88.73** ✅ |
| Extra Trees Regressor | 87.53 |
| AdaBoost Regressor | 80.10 |
| Gradient Boosting Regressor | 88.41 |
| XGBoost Regressor | 87.71 |

### 🏆 Best Performing Model

**Random Forest Regressor** achieved the highest R² Score of **88.73%** and was selected as the final model for deployment.


Reasons:

* Strong predictive performance
* Handles non-linear relationships effectively
* Robust against overfitting
* Works well on mixed categorical and numerical features

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn
* Streamlit
* Pickle

### Deployment

* GitHub
* Streamlit Community Cloud

---


## ▶️ Installation & Setup

### Clone Repository

```bash
git clone https://github.com/Parasmani-yogi/Laptop_Price_Predictor_APP.git
```

### Move Into Project Directory

```bash
cd Laptop_Price_Predictor_APP
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 📈 Project Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Data Preprocessing
6. Model Training
7. Model Evaluation
8. Model Selection
9. Streamlit Deployment


If you found this project useful, consider giving this repository a ⭐ on GitHub.
