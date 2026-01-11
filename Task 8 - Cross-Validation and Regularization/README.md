# Task 8 - Cross-Validation and Regularization

## Overview
Comprehensive analysis of regularized regression models using cross-validation techniques on the California Housing dataset.

## Features
- Ridge and Lasso regression comparison
- Cross-validation with different k-folds (5, 10)
- Hyperparameter tuning with GridSearchCV
- Multiple alpha values testing (0.01, 0.1, 1.0, 10.0, 100.0)
- Standardized preprocessing pipeline

## Dataset
- California Housing dataset from scikit-learn
- Regression problem predicting house values
- Multiple features including location, demographics, and housing characteristics

## Requirements
- scikit-learn
- numpy

## Files
- `comprehensive_cv_analysis.py` - Main analysis script
- `regularized_regression.py` - Additional regression implementations

## Usage
```bash
python comprehensive_cv_analysis.py
```

## Analysis Performed
1. **Ridge Regression**
   - L2 regularization
   - Cross-validation with different alpha values
   - Performance evaluation with R² scoring

2. **Lasso Regression**
   - L1 regularization with feature selection
   - Cross-validation optimization
   - Comparison with Ridge performance

## Key Insights
- Ridge generally performs better than Lasso on this dataset
- Higher alpha values work better for Ridge (more regularization)
- Lower alpha values work better for Lasso (less regularization)
- Cross-validation provides robust model evaluation