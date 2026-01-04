# Task 2 - Robust Pandas Data Wrangling

## Overview
Data cleaning and analysis using the Titanic dataset, demonstrating robust pandas operations for handling missing values and performing exploratory data analysis.

## Features
- Missing value detection and handling
- Data imputation (median for Age, mode for Embarked)
- Descriptive statistics
- Grouped analysis by categorical variables

## Dataset
- Titanic dataset (train.csv, test.csv, gender_submission.csv)
- Contains passenger information including Age, Sex, Embarked port, Fare, etc.

## Requirements
- pandas
- pathlib

## Usage
```bash
python data_analysis.py
```

## Analysis Performed
- Missing value assessment before and after cleaning
- Age imputation using median values
- Embarked port imputation using mode
- Mean age analysis by embarkation port
- Mean fare analysis by gender