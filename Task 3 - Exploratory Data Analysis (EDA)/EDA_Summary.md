# Exploratory Data Analysis (EDA) - Ames Housing Dataset

## Overview
This analysis explores the Ames Housing dataset containing 1,460 houses with 81 features, focusing on understanding relationships between key features and house prices.

## Visualizations Created

### 1. **Correlation Heatmap of Numerical Features**
- **Purpose**: Visualize relationships between key numerical features
- **Key Features Analyzed**: SalePrice, GrLivArea, TotalBsmtSF, GarageArea, 1stFlrSF, YearBuilt, OverallQual, OverallCond
- **Key Insights**:
  - **OverallQual** has the strongest correlation with SalePrice (0.791)
  - **GrLivArea** (Above Grade Living Area) shows strong correlation (0.709)
  - **GarageArea** and **TotalBsmtSF** also correlate well with price
  - **OverallCond** shows weak negative correlation (-0.078)

### 2. **Seaborn Pair Plot / Scatter Plot**
- **Purpose**: Show relationship between two key features and the target variable
- **Features**: GrLivArea vs SalePrice (colored by OverallQual)
- **Key Insights**:
  - Clear positive relationship between living area and sale price
  - Higher quality homes (darker colors) tend to have higher prices
  - Some outliers exist with very large living areas

### 3. **Violin Plots - Distribution Analysis**
Two violin plots were created to show how the numerical target variable (SalePrice) varies across different nominal (categorical) features:

#### A. **Sale Price by House Style**
- **Nominal Feature**: HouseStyle (1Story, 2Story, 1.5Fin, SLvl, SFoyer)
- **Key Insights**:
  - **2Story** houses have the highest average price ($210,052)
  - **1Story** houses are most common (726 houses) with average price $175,985
  - **SFoyer** houses have the lowest average price ($135,074)
  - Distribution shapes vary significantly between house styles

#### B. **Sale Price by Neighborhood**
- **Nominal Feature**: Top 5 neighborhoods by house count
- **Key Insights**:
  - **NoRidge** has the highest average price ($335,295)
  - **NridgHt** and **StoneBr** are also premium neighborhoods
  - Clear neighborhood-based price clustering
  - Some neighborhoods show wider price distributions than others

## Dataset Statistics
- **Total Houses**: 1,460
- **Total Features**: 81
- **Average Sale Price**: $180,921
- **Price Range**: $34,900 - $755,000
- **Standard Deviation**: $79,443

## Top Correlations with Sale Price
1. **OverallQual**: 0.791 (Overall material and finish quality)
2. **GrLivArea**: 0.709 (Above grade living area)
3. **GarageArea**: 0.623 (Garage size in square feet)
4. **TotalBsmtSF**: 0.614 (Total basement area)
5. **1stFlrSF**: 0.606 (First floor area)
6. **YearBuilt**: 0.523 (Construction year)

## Files Generated
1. `final_eda_visualizations.png` - Main comprehensive visualization
2. `seaborn_pairplot.png` - Detailed pair plot of key features
3. `enhanced_eda_visualizations.png` - Additional analysis
4. `eda_visualizations.png` - Initial exploration
5. `pairplot_housing_features.png` - Feature relationships

## Key Takeaways
1. **Quality matters most**: Overall quality is the strongest predictor of price
2. **Size is important**: Living area strongly correlates with price
3. **Location premium**: Certain neighborhoods command significantly higher prices
4. **House style impact**: 2-story homes typically sell for more than single-story
5. **Multiple factors**: Garage size, basement area, and construction year all contribute to pricing

This analysis provides a solid foundation for understanding the housing market dynamics in Ames, Iowa, and can inform both buyers and sellers about key value drivers.