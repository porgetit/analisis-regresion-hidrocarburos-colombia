# Plan de Limpieza y Maximización de Datos 🛠️

Este documento detalla la estrategia técnica para transformar el dataset crudo en un conjunto de datos óptimo para el análisis de regresión lineal, basándose en los hallazgos del análisis exploratorio inicial.

## 1. Normalización de Datos y Texto
Para asegurar que las agrupaciones y mapas de inferencia funcionen correctamente, se aplicarán las siguientes reglas:
*   **Conversión a Minúsculas**: Todas las columnas categóricas (`operadora`, `campo`, `formacion_productora`, `tipo_fluido`) se convertirán a minúsculas.
*   **Limpieza de Caracteres**: Eliminación de espacios en blanco al inicio/final y unificación de caracteres especiales/tildes (ej. unificar "borbón" y "borbon").
*   **Estandarización de Nulos**: Convertir variaciones de "No Reporta", "no reporta", y espacios vacíos a un valor `NaN` uniforme de NumPy para procesamiento computacional.

## 2. Estrategia de Inferencia (Imputación de Datos)
Para minimizar la pérdida de registros útiles:
*   **Mapa Campo-Formación**: Se creará un diccionario de referencia `campo -> formacion_productora` basado en los registros válidos. Los valores `NaN` en formación se rellenarán consultando este mapa.
*   **Imputación Temporal**: Para registros con `fecha_inicio` o `fecha_fin` faltantes:
    *   Se calculará la mediana de `duracion_dias` segmentada por `tipo_prueba`.
    *   Se utilizará esta mediana para completar la variable de duración sin depender de las fechas exactas.

## 3. Reducción de Ruido y Filtrado
*   **Criterio de Exclusión de Producción Cero**: Se eliminarán los registros donde `petroleo_bbl == 0` Y `gas_ksc == 0` (aprox. 28% del dataset). Estos registros no aportan información sobre la relación de productividad entre fluidos.
*   **Gestión de Outliers**:
    *   **Detección**: Uso de Z-Score robusto para identificar valores físicamente improbables.
    *   **Tratamiento**: Se aplicará una **Transformación Logarítmica (`log1p`)** a las variables de producción para reducir el impacto de valores extremos sin eliminarlos, permitiendo capturar la tendencia de los pozos de alto rendimiento.

## 4. Ingeniería de Características (Feature Engineering)
*   **Variable `duracion_dias`**: Calculada como la diferencia absoluta en días entre el fin y el inicio de la prueba.
*   **Variables Dummies**: Creación de indicadores binarios para `tipo_fluido` y `tipo_prueba` para permitir interceptos diferentes en los modelos de regresión.

## 5. Pipeline de Ejecución (src/limpieza.py)
El script de limpieza seguirá este orden estrictamente:
1.  Carga de datos con detección de encoding (`latin-1`/`utf-8`).
2.  Normalización de strings.
3.  Cálculo de `duracion_dias` e imputación de nulos.
4.  Inferencia de Formaciones Geológicas.
5.  Filtrado de registros con producción nula total.
6.  Exportación del dataset procesado a `data/dataset_cleaned.csv`.

---
*Este plan busca preservar la mayor representatividad estadística del sector de hidrocarburos en Colombia.*
