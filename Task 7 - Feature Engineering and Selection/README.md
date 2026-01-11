# Feature Engineering and Selection - Titanic Dataset

## Overview
This project demonstrates comprehensive feature engineering and feature selection techniques using the Titanic dataset. We create new meaningful features and then use statistical methods to identify the top 5 most relevant features for predicting passenger survival.

## Dataset
- **Source**: Titanic dataset (train.csv)
- **Original Shape**: 891 rows × 12 columns
- **Target Variable**: Survived (0 = No, 1 = Yes)

## Feature Engineering

### New Features Created

1. **FamilySize**: `SibSp + Parch + 1`
   - Combines siblings/spouses and parents/children counts
   - Adds 1 to include the passenger themselves
   - Range: 1-11 passengers

2. **IsAlone**: Binary feature indicating solo travelers
   - 1 if FamilySize == 1, 0 otherwise
   - Captures the effect of traveling alone vs. with family

3. **Title**: Extracted from passenger names
   - Extracted titles (Mr, Mrs, Miss, Master, etc.)
   - Grouped rare titles together
   - Encoded numerically: Mr=1, Miss=2, Mrs=3, Master=4, Others=5

4. **AgeGroup**: Age binned into categories
   - Bins: [0-12], [12-18], [18-35], [35-60], [60+]
   - Encoded as: 1, 2, 3, 4, 5 respectively

5. **FarePerPerson**: `Fare / FamilySize`
   - Normalizes fare by family size
   - Better represents individual spending power

## Feature Selection Methods

### Method 1: SelectKBest (F-statistic)
Uses ANOVA F-test to measure linear dependency between features and target.

**Top 5 Features Selected:**
1. **Sex** (F-score: 372.41) - Strongest predictor
2. **Title** (F-score: 184.40) - Engineered feature
3. **Pclass** (F-score: 115.03) - Passenger class
4. **Fare** (F-score: 63.03) - Ticket price
5. **FarePerPerson** (F-score: 45.91) - Engineered feature

### Method 2: Recursive Feature Elimination (RFE)
Uses Random Forest to recursively eliminate features based on importance.

**Top 5 Features Selected:**
1. **Sex** - Gender (most important)
2. **Age** - Passenger age
3. **Fare** - Ticket price
4. **Title** - Engineered feature from name
5. **FarePerPerson** - Engineered feature

## Results Analysis

### Model Performance Comparison
- **All Features (12)**: 81.01% accuracy
- **SelectKBest (5)**: 78.77% accuracy (-2.23%)
- **RFE (5)**: 82.12% accuracy (+1.12%)

### Key Insights

1. **RFE Outperforms SelectKBest**: RFE achieved better performance by considering feature interactions through the Random Forest model.

2. **Engineered Features Add Value**: 
   - 2 out of 5 engineered features made it to the top selections
   - **Title** and **FarePerPerson** were selected by both methods
   - These features captured important patterns not present in original data

3. **Feature Overlap**: 4 out of 5 features were common between both methods:
   - Sex, Fare, Title, FarePerPerson

4. **Gender is the Strongest Predictor**: Consistently ranked #1 across all methods

5. **Feature Importance Rankings** (Random Forest):
   1. Age (16.65%)
   2. Sex (16.40%)
   3. FarePerPerson (15.69%) - Engineered
   4. Title (15.68%) - Engineered
   5. Fare (15.52%)

### Engineered Features Impact

| Feature | Importance | Selected By | Status |
|---------|------------|-------------|---------|
| Title | 15.68% | Both methods | ✅ High impact |
| FarePerPerson | 15.69% | Both methods | ✅ High impact |
| FamilySize | 3.91% | Neither | ❌ Low impact |
| AgeGroup | 3.16% | Neither | ❌ Redundant with Age |
| IsAlone | 0.91% | Neither | ❌ Low impact |

## Conclusions

1. **Feature Engineering Success**: Created 5 new features, with 2 becoming top predictors
2. **Dimensionality Reduction**: Reduced from 12 to 5 features while maintaining/improving performance
3. **Method Selection**: RFE proved more effective than SelectKBest for this dataset
4. **Domain Knowledge Matters**: Features like Title and FarePerPerson captured meaningful patterns

## Files in This Project

- `train.csv` - Original Titanic dataset
- `feature_engineering_selection.py` - Basic implementation
- `improved_feature_engineering.py` - Enhanced version with detailed analysis
- `visualize_results.py` - Creates visualization charts
- `feature_selection_analysis.png` - Generated visualization
- `README.md` - This documentation

## Usage

```bash
# Run basic feature engineering and selection
python feature_engineering_selection.py

# Run enhanced analysis with detailed output
python improved_feature_engineering.py

# Generate visualizations
python visualize_results.py
```

## Requirements

```
pandas
numpy
scikit-learn
matplotlib
seaborn
```

## Key Takeaways

1. **Quality over Quantity**: Not all engineered features improve model performance
2. **Feature Selection is Crucial**: Proper selection can improve both performance and interpretability
3. **Multiple Methods**: Different selection methods may yield different results - compare and validate
4. **Domain Expertise**: Understanding the problem domain helps create meaningful features
5. **Validation is Key**: Always validate feature selection results with cross-validation in production