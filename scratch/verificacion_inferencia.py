import pandas as pd

# Load dataset
file_path = r"c:\Users\WINDOWS 11\Documents\proyects\analisis-regresion-hidrocarburos-colombia\data\dataset.csv"
try:
    df = pd.read_csv(file_path, encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv(file_path, encoding='latin-1')

# 1. Check if 'formacion_productora' can be inferred from 'campo'
# Create a mapping of campo -> formacion (excluding 'No Reporta')
mapping = df[df['formacion_productora'] != 'No Reporta'].groupby('campo')['formacion_productora'].unique()

print("--- Campo to Formacion Mapping (Partial) ---")
for campo, formaciones in mapping.items():
    if len(formaciones) > 1:
        print(f"Campo '{campo}' has multiple formations: {formaciones}")
    else:
        print(f"Campo '{campo}' -> {formaciones[0]}")

# 2. Check overlap of Petroleo and Gas zeros
both_zero = ((df['petroleo_bbl'] == 0) & (df['gas_ksc'] == 0)).sum()
print(f"\nRecords with BOTH Petroleo and Gas == 0: {both_zero} ({(both_zero/len(df)*100):.2f}%)")

# 3. Check if 'modalidad' can be inferred from 'tipo_prueba'
modalidad_by_prueba = df.groupby('tipo_prueba')['modalidad'].value_counts()
print("\n--- Modalidad by Tipo de Prueba ---")
print(modalidad_by_prueba)
