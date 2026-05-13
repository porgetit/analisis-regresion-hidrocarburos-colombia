import pandas as pd
import numpy as np

# Load dataset
file_path = r"c:\Users\WINDOWS 11\Documents\proyects\analisis-regresion-hidrocarburos-colombia\data\dataset.csv"
df = pd.read_csv(file_path)

# General Info
print("--- Info ---")
print(df.info())

# Descriptive Stats
print("\n--- Descriptive Stats ---")
print(df.describe(include='all'))

# Unique values for categorical columns
cat_cols = ['operadora', 'modalidad', 'tipo_fluido', 'estado', 'tipo_prueba', 'formacion_productora']
print("\n--- Unique Values ---")
for col in cat_cols:
    if col in df.columns:
        print(f"{col}: {df[col].unique()[:10]}... (Total: {df[col].nunique()})")

# Check for "No Reporta" and nulls
print("\n--- Special Values ---")
for col in df.columns:
    no_reporta_count = (df[col] == "No Reporta").sum()
    null_count = df[col].isnull().sum()
    print(f"{col} -> Nulls: {null_count}, 'No Reporta': {no_reporta_count}")
