# Task 5 - Comparative Machine Learning Modeling

## Overview
Comparative analysis of different machine learning algorithms using the Wine Quality dataset, implementing K-Nearest Neighbors (KNN) and Support Vector Classifier (SVC).

## Features
- Wine dataset classification
- KNN with multiple k values (3, 4, 10)
- SVC with linear kernel
- Performance comparison and model selection
- 80/20 train-test split

## Dataset
- Wine Quality dataset from Kaggle
- Multi-class classification problem
- Features include various wine chemical properties

## Requirements
- scikit-learn
- pandas
- numpy

## Files
- `comparative_ml_modeling.py` - Main implementation
- `comparative_ml_modelling.ipynb` - Jupyter notebook version
- `dataset/WineQT.csv` - Wine quality dataset

## Usage
```bash
python comparative_ml_modeling.py
```

## Models Compared
1. **K-Nearest Neighbors (KNN)**
   - Tested with k=3, 4, 10
   - Best performance with k=3

2. **Support Vector Classifier (SVC)**
   - Linear kernel
   - Compared against best KNN model

## Results
The script outputs accuracy scores for each model configuration and identifies the best performing algorithm.