# Task 02 — Machine Learning Pipeline

## Objective

Build a machine learning pipeline for predicting whether an Olist order will be delivered late or on time.

## Data Preparation

The dataset was prepared by selecting delivered orders and creating the target variable:

* `is_late = 0` → On time
* `is_late = 1` → Late

The final labeled dataset contained:

* On-time orders: 88,652
* Late orders: 7,826

## Train / Validation / Test Split

The labeled data was divided into three datasets:

| Dataset    |   Rows |
| ---------- | -----: |
| Training   | 67,534 |
| Validation | 14,472 |
| Test       | 14,472 |

The same class distribution was maintained across the splits.

## Exploratory Data Analysis

EDA was performed to understand the distribution of the target variable and investigate the available order and delivery-related information.

## Feature Engineering

The final features used for the model were:

* `purchase_hour`
* `purchase_day_of_week`
* `purchase_month`
* `purchase_year`
* `approval_delay_hours`
* `estimated_delivery_days`

The feature engineering pipeline also handled missing values and applied the required preprocessing steps.

## Model

A Random Forest classifier was trained to predict late deliveries.

The fitted model and preprocessing objects were saved for later use in the production inference service.

Saved artifacts include:

* `random_forest_model.pkl`
* `imputer.pkl`
* `scaler.pkl`
* `feature_list.pkl`

## Notebooks

The Task 02 development process is documented in the project notebooks, including:

* Data reading and joining
* Label creation
* Train / validation / test split
* Exploratory Data Analysis
* Feature engineering
* Model training and evaluation

## Completion

* [x] Data preparation
* [x] Target label creation
* [x] Train / validation / test split
* [x] EDA
* [x] Feature engineering
* [x] Model training
* [x] Model evaluation
* [x] Model artifacts saved
