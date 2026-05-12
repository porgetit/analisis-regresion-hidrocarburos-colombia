# Plan de Trabajo — Análisis de Relaciones Lineales en Producción de Hidrocarburos

## Objetivo General

Analizar relaciones lineales entre variables de producción de hidrocarburos utilizando técnicas de regresión lineal simple y análisis exploratorio de datos sobre el dataset:

**“Pruebas Iniciales y Extensas de Producción”**

El propósito es identificar correlaciones lineales significativas entre variables físicas y temporales relacionadas con la producción de petróleo y gas.

---

# 1. Comprensión del Dataset

## Variables relevantes

| Variable | Tipo | Descripción |
|---|---|---|
| `petroleo_bbl` | Numérica | Producción de petróleo en barriles |
| `gas_ksc` | Numérica | Producción de gas en KSCF |
| `fecha_inicio` | Temporal | Inicio de la prueba |
| `fecha_fin` | Temporal | Fin de la prueba |
| `vigencia` | Numérica | Año de reporte |
| `mes` | Numérica | Mes de reporte |
| `tipo_fluido` | Categórica | Petróleo, Gas, Petróleo y Gas |
| `modalidad` | Categórica | Evaluación o Explotación |
| `formacion_productora` | Categórica | Formación geológica |
| `estado` | Categórica | Activo/Inactivo |

---

# 2. Limpieza y Preparación de Datos

## Objetivo

Garantizar consistencia, tipado correcto y calidad suficiente para el análisis estadístico.

---

## 2.1 Carga del Dataset

### Tareas

- Importar dataset usando pandas.
- Verificar:
  - dimensiones,
  - tipos de datos,
  - nombres de columnas,
  - duplicados.

### Herramientas

- `pandas`
- `numpy`

---

## 2.2 Limpieza de Valores Nulos

### Tareas

Identificar:
- nulos,
- vacíos,
- strings inválidos.

Evaluar:
- porcentaje de datos faltantes por columna,
- impacto estadístico de eliminarlos.

### Decisiones esperadas

- eliminar registros incompletos,
- o imputar si la pérdida es excesiva.

---

## 2.3 Conversión de Fechas

### Tareas

Convertir:
- `fecha_inicio`
- `fecha_fin`

a tipo datetime.

### Validaciones

- fechas inválidas,
- fechas invertidas,
- diferencias negativas.

---

## 2.4 Creación de Variables Derivadas

### Variable principal

Duración de la prueba:

$$
\Delta t = fecha\_fin - fecha\_inicio
$$

### Nueva columna

`duracion_dias`

### Objetivo

Introducir una variable continua físicamente interpretable para regresión.

---

## 2.5 Conversión de Variables Numéricas

### Tareas

Asegurar tipo numérico en:
- `petroleo_bbl`
- `gas_ksc`
- `vigencia`
- `mes`

### Validaciones

- caracteres extraños,
- separadores,
- negativos imposibles,
- outliers extremos.

---

# 3. Análisis Exploratorio de Datos (EDA)

## Objetivo

Entender distribuciones, dispersión y posibles relaciones lineales.

---

## 3.1 Estadísticos Descriptivos

### Calcular

- media,
- mediana,
- desviación estándar,
- mínimos,
- máximos,
- percentiles.

### Variables

- `petroleo_bbl`
- `gas_ksc`
- `duracion_dias`

---

## 3.2 Distribuciones

### Visualizaciones

Histogramas de:
- producción de petróleo,
- producción de gas,
- duración.

### Objetivos

Detectar:
- sesgo,
- colas largas,
- concentraciones,
- necesidad de transformaciones.

---

## 3.3 Detección de Outliers

### Técnicas

- boxplots,
- IQR,
- z-score.

### Objetivo

Evaluar impacto de valores extremos sobre la regresión lineal.

---

## 3.4 Matriz de Correlación

### Variables

- `petroleo_bbl`
- `gas_ksc`
- `duracion_dias`
- `vigencia`
- `mes`

### Objetivo

Identificar:
- relaciones lineales fuertes,
- correlaciones débiles,
- independencia parcial.

---

# 4. Visualización de Relaciones Lineales

## Objetivo

Evaluar visualmente patrones lineales antes del modelado.

---

## 4.1 Scatter Plot — Petróleo vs Gas

Modelo esperado:

$$
gas\_ksc = m \cdot petroleo\_bbl + b
$$

### Objetivo

Determinar:
- linealidad,
- agrupamientos,
- dispersión,
- posibles subpoblaciones.

---

## 4.2 Scatter Plot — Duración vs Petróleo

Modelo esperado:

$$
petroleo\_bbl = m \cdot duracion\_dias + b
$$

### Hipótesis

Mayor duración podría asociarse con mayor producción acumulada.

---

## 4.3 Scatter Plot — Duración vs Gas

Modelo esperado:

$$
gas\_ksc = m \cdot duracion\_dias + b
$$

---

## 4.4 Visualización Segmentada

### Segmentar por

- `tipo_fluido`
- `modalidad`
- `formacion_productora`

### Objetivo

Evaluar si las relaciones lineales mejoran en subconjuntos homogéneos.

---

# 5. Regresión Lineal

## Objetivo

Construir modelos lineales simples y evaluar su capacidad explicativa.

---

# 5.1 Regresión Lineal Simple

## Modelo 1 — Gas vs Petróleo

$$
gas\_ksc = m \cdot petroleo\_bbl + b
$$

### Métricas

- coeficiente de correlación,
- coeficiente de determinación \(R^2\),
- MAE,
- RMSE.

---

## Modelo 2 — Petróleo vs Duración

$$
petroleo\_bbl = m \cdot duracion\_dias + b
$$

---

## Modelo 3 — Gas vs Duración

$$
gas\_ksc = m \cdot duracion\_dias + b
$$

---

# 5.2 Evaluación de Residuos

## Objetivo

Verificar supuestos de regresión lineal.

### Analizar

- distribución de residuos,
- heterocedasticidad,
- linealidad residual,
- sensibilidad a outliers.

---

# 5.3 Comparación Entre Modelos

## Comparar

- pendiente,
- intercepto,
- \(R^2\),
- error medio,
- estabilidad visual.

### Objetivo

Determinar cuál relación presenta mejor comportamiento lineal.

---

# 6. Segmentación y Modelos Especializados

## Objetivo

Evaluar si subconjuntos homogéneos presentan relaciones lineales más fuertes.

---

# 6.1 Segmentación por Tipo de Fluido

### Categorías esperadas

- Petróleo
- Gas
- Petróleo y Gas

### Hipótesis

Las mezclas podrían degradar la correlación global.

---

# 6.2 Segmentación por Modalidad

### Categorías

- Evaluación
- Explotación

### Hipótesis

Las dinámicas de producción podrían diferir significativamente.

---

# 6.3 Segmentación por Formación Productora

## Objetivo

Detectar:
- comportamientos geológicos distintos,
- relaciones lineales locales,
- agrupamientos físicos.

---

# 6.4 Comparación Global vs Segmentado

## Objetivo

Determinar si:

$$
R^2_{segmentado} > R^2_{global}
$$

### Discusión esperada

- heterogeneidad del dataset,
- subpoblaciones,
- mejora de linealidad mediante segmentación.

---

# 7. Resultados Esperados

## Posibles hallazgos

- correlación moderada o fuerte entre petróleo y gas,
- relación lineal parcial entre duración y producción,
- mejora significativa al segmentar,
- presencia de outliers operacionales,
- evidencia de heterogeneidad geológica.

---

# 8. Herramientas Recomendadas

## Librerías Python

```python
pandas
numpy
matplotlib
scikit-learn
scipy
statsmodels
