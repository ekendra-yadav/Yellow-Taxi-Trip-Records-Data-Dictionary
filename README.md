# 🚖 NYC Taxi Fare Prediction using Machine Learning

## 📖 Project Overview
Taxi fare prediction is an important problem in modern urban transportation systems. Accurate fare estimation improves pricing transparency, helps passengers estimate travel costs, and allows transportation companies to optimize pricing strategies.

This project builds a machine learning pipeline to predict taxi trip fares using features such as trip distance, passenger count, and trip duration. The dataset used in this project comes from the official records of the New York City Taxi and Limousine Commission.

The project follows a complete data science workflow including data cleaning, exploratory data analysis, feature engineering, model training, and model evaluation.

---

## 🎯 Problem Statement
Taxi fares depend on multiple factors such as travel distance, trip duration, passenger count, and time of travel. Without a predictive system, estimating fares before a trip begins becomes difficult.

This leads to several challenges:

- Passengers cannot accurately estimate travel costs beforehand  
- Ride hailing platforms struggle with dynamic pricing optimization  
- Taxi companies miss insights about travel demand patterns  
- Raw trip data contains noise, missing values, and outliers that reduce prediction accuracy  

The objective of this project is to develop a machine learning model capable of predicting taxi fares based on trip characteristics.

---

## 🧠 Solution Approach
To address the problem, a structured data science pipeline was implemented:

1. Data Loading  
2. Data Cleaning and Handling Missing Values  
3. Exploratory Data Analysis (EDA)  
4. Feature Engineering  
5. Outlier Detection and Removal  
6. Feature Scaling and Preprocessing  
7. Model Training  
8. Model Evaluation and Comparison  

This pipeline ensures that the data is properly prepared before applying machine learning models.

---

## 📊 Dataset Description
The dataset contains detailed taxi trip records including:

- Pickup and dropoff timestamps  
- Passenger count  
- Trip distance  
- Rate code  
- Store and forward flag  
- Total trip amount  

Each row represents one taxi trip along with the associated ride information.

The dataset was obtained from the open data portal maintained by the New York City Taxi and Limousine Commission.

Because the dataset contains millions of records, efficient preprocessing techniques were required to handle large scale data.

---

## 🛠 Tools and Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

These tools were used for data manipulation, visualization, machine learning model development, and evaluation.

---

## 📈 Exploratory Data Analysis (EDA)

Exploratory Data Analysis was performed to better understand the dataset and detect patterns.

Key steps included:

- Inspecting dataset structure and data types  
- Identifying missing values  
- Analyzing statistical distributions of numerical features  
- Detecting outliers and abnormal records  
- Visualizing relationships between features  

Various visualizations such as histograms, distribution plots, and correlation heatmaps were used to explore the data.

---

## ⚙ Feature Engineering

Feature engineering was applied to extract meaningful information from the raw dataset.

The following features were created:

- **Trip Duration** calculated from pickup and dropoff timestamps  
- **Pickup Hour** to capture hourly travel patterns  
- **Pickup Day of Week** to analyze weekday and weekend behavior  

These engineered features help the machine learning model better understand travel patterns.

---

## 🧹 Data Preprocessing

The following preprocessing techniques were applied to improve model performance:

- Handling missing values using median and mode imputation  
- Removing duplicate records  
- Detecting and removing outliers using the IQR method  
- Dropping columns that cause data leakage  
- Scaling numerical features using StandardScaler  

These steps ensure that the dataset is clean and suitable for machine learning.

---

## 🤖 Machine Learning Models

Two regression models were used in this project.

### Linear Regression
Linear Regression was used as a baseline model to establish a simple relationship between trip features and fare amount.

### Random Forest Regressor
Random Forest is an ensemble learning algorithm that builds multiple decision trees and combines their predictions. It can capture nonlinear relationships within the data.

Both models were trained and evaluated to compare their performance.

---

## 📉 Model Evaluation

The models were evaluated using standard regression metrics:

- **Mean Absolute Error (MAE)**
- **Mean Squared Error (MSE)**
- **R² Score**

These metrics measure how accurately the model predicts taxi fares compared to the actual values.

The Random Forest model achieved better performance by capturing complex relationships between features such as trip distance and trip duration.

---

## 🔍 Key Insights

Important findings from the analysis include:

- Trip distance is the most important factor influencing taxi fare  
- Trip duration also plays a significant role in determining the final amount  
- Passenger count has a smaller influence on fare prediction  
- Outliers and abnormal trip records significantly affect model accuracy if not properly handled  

These insights can help transportation services better understand pricing patterns.

---

## ▶ How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/ekendra-yadav/Yellow-Taxi-Trip-Records-Data-Dictionary.git
```

## ▶ How to Test the Project

```bash
https://huggingface.co/spaces/ekendra001/taxi-fare-prediction
```
