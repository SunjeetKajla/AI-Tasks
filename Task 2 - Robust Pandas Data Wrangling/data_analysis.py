import pandas as pd
from pathlib import Path

base_dir = Path(__file__).parent
df = pd.read_csv(base_dir / 'dataset/train.csv')

print("Missing values before cleaning:")
print(df.isnull().sum())

df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nFirst 5 rows after cleaning:")
print(df.head())

print("\nDescriptive statistics:")
print(df.describe())

print("\nMean Age by Embarked port:")
print(df.groupby('Embarked')['Age'].mean())

print("\nMean Fare by Sex:")
print(df.groupby('Sex')['Fare'].mean())