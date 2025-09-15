\# House Price Prediction using Linear Regression



\## Project Overview

This project predicts house prices using \*\*Linear Regression\*\*. It demonstrates data preprocessing, exploratory data analysis (EDA), model training, and evaluation of predictions using common regression metrics. The project is implemented in \*\*Python\*\* with Jupyter Notebook and can also be displayed interactively using \*\*Streamlit\*\*.



\## Dataset

\- The dataset contains house features and their corresponding sale prices.

\- Format: CSV (`data.csv`)

\- Example features:

&nbsp; - `LotArea` – Lot size in square feet

&nbsp; - `OverallQual` – Overall material and finish quality

&nbsp; - `YearBuilt` – Year the house was built

&nbsp; - `TotalBsmtSF` – Total basement area

&nbsp; - `GrLivArea` – Above ground living area

&nbsp; - `SalePrice` – Target variable (house price)



\## Project Structure

houseprice\_prediction/

│

├─ HousePricePrediction.ipynb # Jupyter Notebook with full workflow

├─ calc\_metrics.py # Script to calculate evaluation metrics

├─ data.csv # Dataset file

├─ README.md # Project documentation

└─ requirements.txt # Python dependencies



\## Features

\- \*\*Data Cleaning \& Preprocessing\*\*: Handle missing values and encode categorical variables.

\- \*\*Exploratory Data Analysis (EDA)\*\*: Visualizations including correlation heatmaps to identify important features.

\- \*\*Model Training\*\*: Linear Regression to predict house prices.

\- \*\*Metrics Evaluation\*\*: Calculated using `calc\_metrics.py`:

&nbsp; - Mean Absolute Error (MAE)

&nbsp; - Mean Squared Error (MSE)

&nbsp; - Root Mean Squared Error (RMSE)

&nbsp; - R² Score

\- \*\*Interactive Visualization\*\*: Deploy with Streamlit for live predictions.



\## Installation

1\. Clone the repository:

&nbsp;  ```bash

&nbsp;  git clone https://github.com/Darshanns7/houseprice\_prediction.git

### Streamlit Live Demo
- Try the interactive app here: [Streamlit Live Demo](https://share.streamlit.io/darshanns7/houseprice_prediction/main/app.py)
- Enter house features to get predicted prices interactively.


