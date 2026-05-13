# Plan de Implementación: Pipeline de Limpieza 🏗️

Este plan describe la arquitectura de software para el módulo `src/limpieza.py`, diseñado bajo principios de producción industrial.

## 1. Arquitectura: Orientación a Componentes
Utilizaremos un patrón de **Orquestador-Componente**. Una clase principal (`DataCleaner`) coordinará una serie de métodos especializados (componentes) que operan sobre el DataFrame.

### Ventajas:
- **Aislamiento**: Si decidimos cambiar cómo imputamos las fechas, solo modificamos el componente de fechas.
- **Legibilidad**: El método `run()` de la clase mostrará el flujo lógico como si fuera una receta.
- **Extensibilidad**: Fácil de añadir nuevos pasos sin romper la estructura.

## 2. Definición de Objetos y Responsabilidades

### Clase `DataCleaner`
**Atributos:**
- `path_raw`: Ruta al CSV original.
- `df`: El DataFrame en memoria.
- `mapping_campo_formacion`: Diccionario para la inferencia.

**Métodos (Componentes):**
1. `load_data()`: Manejo de encoding y carga inicial.
2. `normalize_strings()`: Limpieza de texto y estandarización de `NaN`.
3. `process_dates()`: Cálculo de `duracion_dias` e imputación por mediana.
4. `infer_geography()`: Aplicación del mapa `campo` -> `formacion`.
5. `filter_production()`: Eliminación de ceros y aplicación de `log1p`.
6. `save_cleaned_data()`: Exportación a `data/dataset_cleaned.csv`.

## 3. Estándares de Codificación (PEP 8 & KISS)
- **Nomenclatura**: `snake_case` para variables y funciones, `PascalCase` para clases.
- **Documentación**: Cada componente tendrá un `docstring` breve explicando su entrada y salida.
- **Simplicidad (KISS)**: Evitaremos abstracciones innecesarias. Usaremos métodos directos de `pandas` por eficiencia y claridad.

## 4. Flujo Detallado de Implementación

### Paso A: Carga y Normalización
- Detección automática de encoding (`utf-8` / `latin-1`).
- Aplicación de `.str.lower().str.strip()` y remoción de acentos mediante una función auxiliar `remove_accents`.

### Paso B: Lógica Temporal
- Cálculo de `delta_t` en días.
- Agrupación por `tipo_prueba` para obtener la mediana.
- Relleno de nulos usando `fillna()` segmentado.

### Paso C: Inferencia de Formación
- Construcción del mapa de referencia filtrando registros que NO sean "no reporta".
- Uso de `df['campo'].map(referencia)` para completar los huecos.

### Paso D: Transformación de Producción
- Filtrado de registros donde `(petroleo == 0) & (gas == 0)`.
- Aplicación de `np.log1p()` para mitigar el sesgo de los pozos con sobre-producción.

## 5. Contrato de Salida
El resultado final será un archivo en `data/dataset_cleaned.csv` con tipado correcto y listo para ser consumido por el módulo de `exploracion.py`.
