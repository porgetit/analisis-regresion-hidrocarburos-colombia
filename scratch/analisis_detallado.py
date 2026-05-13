import pandas as pd

# Load dataset with potential encoding handling
file_path = r"c:\Users\WINDOWS 11\Documents\proyects\analisis-regresion-hidrocarburos-colombia\data\dataset.csv"
try:
    df = pd.read_csv(file_path, encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv(file_path, encoding='latin-1')

print("--- Statistics for Numerical Columns ---")
print(df[['petroleo_bbl', 'gas_ksc']].describe())

print("\n--- Zero values counts ---")
print(f"Petroleo == 0: {(df['petroleo_bbl'] == 0).sum()}")
print(f"Gas == 0: {(df['gas_ksc'] == 0).sum()}")

print("\n--- Encoding check (tipo_fluido) ---")
print(df['tipo_fluido'].unique())
