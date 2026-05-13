# Análisis de Regresión de Hidrocarburos en Colombia 🇨🇴🛢️

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Pandas](https://img.shields.io/badge/Library-Pandas-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Scikit-Learn](https://img.shields.io/badge/Library-Scikit--Learn-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)

Este proyecto realiza un análisis estadístico y de modelado predictivo sobre la producción de hidrocarburos en Colombia, utilizando técnicas de **Regresión Lineal Simple** para entender la relación entre variables operativas y volúmenes de producción.

---

## 🚀 Estructura del Análisis

El proyecto se desarrolla siguiendo los 6 puntos estratégicos definidos en el plan de trabajo:

### 1. Comprensión del Dataset 📊

El dataset contiene registros históricos de pruebas de producción de hidrocarburos en Colombia. Tras un análisis inicial, se han identificado las siguientes características clave:

*   **Dimensiones**: 723 registros y 14 columnas técnicas.
*   **Variables de Producción (Target candidates)**:
    *   `petroleo_bbl`: Producción de petróleo en barriles. Presenta una media de ~1,016 bbl con una desviación estándar muy alta (~16,393), lo que indica una gran dispersión y presencia de outliers extremos (Max: 440,200 bbl).
    *   `gas_ksc`: Producción de gas en KSCF. Media de ~1,240 ksc, con un 59% de los registros en cero, sugiriendo pozos puramente petroleros o falta de medición.
*   **Variables Temporales**:
    *   `fecha_inicio` y `fecha_fin`: Fundamentales para el cálculo de la variable derivada `duracion_dias`. Se detectaron entre un 5% y 7% de valores nulos que requieren imputación o descarte.
*   **Variables de Segmentación**:
    *   `tipo_fluido`: Clasifica la producción en 5 categorías (Petróleo, Gas, Mezclas).
    *   `formacion_productora` y `modalidad`: Variables de alto impacto geológico/operativo, aunque presentan un 47% de registros bajo la etiqueta "No Reporta".
*   **Calidad y Desafíos**:
    *   **Sesgo**: Alta concentración de valores en cero en ambas variables de producción.
    *   **Integridad**: El uso frecuente de "No Reporta" obligará a realizar una limpieza selectiva para no perder representatividad estadística.

### 2. Limpieza y Preparación de Datos 🧹

Para maximizar la utilidad del dataset y reducir el sesgo, se implementará un pipeline de limpieza basado en los siguientes pilares técnicos:

*   **Normalización y Estandarización**: 
    *   Conversión de variables categóricas a minúsculas y eliminación de tildes/espacios para evitar duplicados operativos (ej. *borbón* vs *borbon*).
    *   Unificación de etiquetas "No Reporta" a valores `NaN` de NumPy.
*   **Inferencia Geográfica (Imputación por Mapeo)**: 
    *   Uso de la relación `campo` -> `formacion_productora` para rellenar vacíos. Si un campo tiene una formación declarada en otros registros, se usará esa para completar los nulos del mismo campo.
*   **Imputación Temporal Robusta**: 
    *   Cálculo de la variable `duracion_dias`. 
    *   Para registros con fechas faltantes, se imputará la **mediana** de la duración segmentada por `tipo_prueba` (Iniciales/Extensas). Se elige la **mediana** por su robustez frente a outliers operativos que sesgarían la media.
*   **Filtrado de Ruido Operacional**: 
    *   Eliminación selectiva de registros con "Cero Total" (Petróleo y Gas simultáneamente en 0), ya que no aportan información a la relación de regresión.
*   **Ingeniería de Variables**: 
    *   Aplicación de **Transformación Logarítmica (`log1p`)** en variables de producción para estabilizar la varianza frente a outliers masivos.
    *   Creación de variables *dummy* para segmentación por tipo de fluido.

> [!NOTE]
> Para un desglose técnico paso a paso del procedimiento, consulte el documento anexo: [Plan de Limpieza Detallado](file:///c:/Users/WINDOWS%2011/Documents/proyects/analisis-regresion-hidrocarburos-colombia/plan%20de%20limpieza.md).

### 3. Análisis Exploratorio de Datos (EDA) 🔍
Entendimiento profundo de la distribución de los datos:
- Estadísticos descriptivos (media, desviación, percentiles).
- Detección de sesgos y colas largas en la producción.
- Identificación de *outliers* operacionales mediante técnicas de IQR y Boxplots.

### 4. Visualización de Relaciones Lineales 📈
Evaluación visual de patrones antes del modelado:
- Scatter plots de Petróleo vs Gas.
- Relación entre la duración de las pruebas y la producción acumulada.
- Segmentación visual inicial por formación y modalidad.

### 5. Regresión Lineal 🤖
Construcción y evaluación de modelos matemáticos:
- Implementación de modelos: `Gas ~ Petróleo` y `Producción ~ Duración`.
- Evaluación mediante métricas de error: **R²**, **MAE** y **RMSE**.
- Análisis de residuos para verificar supuestos de linealidad y homocedasticidad.

### 6. Segmentación y Modelos Especializados 🧩
Optimización de la capacidad explicativa:
- Evaluación del impacto del `tipo_fluido` en la correlación.
- Modelos específicos por formación geológica.
- Comparación de desempeño entre modelos globales vs. segmentados.

### [2026-05-12] - Justificación Estadística de Imputación
- **Decisión**: Utilizar la **mediana** para la imputación de `duracion_dias`.
- **Razón**: El dataset presenta alta varianza operacional. La mediana es un estadístico robusto que no se ve afectado por pruebas excepcionalmente largas (outliers) ni por distribuciones sesgadas, a diferencia de la media.
- **Autor**: Antigravity (AI Agent)

---
*Última actualización: 2026-05-12*

## 🛠️ Instalación y Uso

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/analisis-regresion-hidrocarburos-colombia.git
   ```

2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar el análisis:**
   Los scripts pueden ejecutarse de forma secuencial en la carpeta `src/` o mediante el notebook principal en `notebooks/`.

---

## 📂 Organización del Proyecto

```text
├── data/               # Datasets crudos y procesados
├── notebooks/          # Experimentación y EDA interactivo
├── outputs/            # Gráficos y reportes exportados
├── src/                # Código fuente modular
│   ├── limpieza.py
│   ├── exploracion.py
│   ├── visualizacion.py
│   └── regresion.py
├── MEMORY.md           # Memoria de contexto para agentes IA
└── README.md           # Documentación principal
```

---
*Desarrollado como parte del análisis técnico de producción de energía.*
