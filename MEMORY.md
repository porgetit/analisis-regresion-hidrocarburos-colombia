# Memoria del Proyecto: Análisis de Regresión de Hidrocarburos en Colombia

Este documento sirve como memoria de contexto para agentes de IA que trabajen en este repositorio.

## 📌 Resumen del Proyecto
El objetivo es analizar las relaciones lineales en la producción de hidrocarburos en Colombia, específicamente entre la producción de petróleo (`petroleo_bbl`), gas (`gas_ksc`) y la duración de las pruebas (`duracion_dias`).

## 📂 Estructura del Repositorio
- `src/`: Scripts modulares para el procesamiento y modelado.
    - `limpieza.py`: Limpieza y preprocesamiento.
    - `exploracion.py`: Análisis exploratorio de datos (EDA).
    - `visualizacion.py`: Generación de gráficos.
    - `regresion.py`: Implementación de modelos de regresión.
- `data/`: Datos crudos y procesados.
    - `dataset.csv`: Archivo principal de datos.
- `notebooks/`: Espacio para experimentación interactiva.
- `outputs/`: Carpeta para guardar gráficos y reportes generados.
- `plan de trabajo.md`: Hoja de ruta detallada del proyecto (Documento de Verdad).

## 📊 Estado Actual
- **Fase**: Planificación Inicial y Configuración de Estructura.
- **Progreso**: 
    - El `plan de trabajo.md` está completo y detalla todas las fases.
    - La estructura de carpetas y archivos `.py` base ha sido creada.
    - El dataset principal (`ugxs-nafj.csv`) está disponible en la raíz y en `data/`.
    - Los scripts en `src/` están actualmente vacíos, listos para implementación.
    - Se ha creado el `README.md` con la estructura del plan de trabajo.

## 🛠️ Stack Tecnológico
- **Lenguaje**: Python 3.x
- **Librerías principales**: pandas, numpy, matplotlib, seaborn, scikit-learn, statsmodels.

## 📝 Guía para Futuros Agentes
1. **Seguir el Plan**: Consultar siempre `plan de trabajo.md` para determinar la siguiente tarea.
2. **Modularidad**: Mantener la lógica separada en los archivos de `src/` según su propósito.
3. **Limpieza de Datos**: El dataset contiene valores "No Reporta" y nulos que deben ser gestionados en `limpieza.py`.
4. **Variables Críticas**:
    - Derivar `duracion_dias` a partir de `fecha_inicio` y `fecha_fin`.
    - Atender a la segmentación por `tipo_fluido` y `modalidad` para mejorar la precisión de los modelos.
5. **Consistencia**: Asegurar que las visualizaciones se guarden en `outputs/` con nombres descriptivos.

---

## 🕒 Historial de Decisiones

### [2026-05-12] - Creación de Documentación Base
- **Decisión**: Crear un `README.md` estructurado específicamente siguiendo los 6 puntos del `plan de trabajo.md`.
- **Razón**: Asegurar consistencia absoluta entre la planificación estratégica y la documentación pública del repositorio, facilitando la navegación para humanos y agentes.
- **Autor**: Antigravity (AI Agent)

### [2026-05-12] - Análisis de Comprensión del Dataset
- **Decisión**: Ejecutar análisis estadístico inicial para validar el plan de trabajo.
- **Descubrimientos**:
    - Alta presencia de ceros en producción (44% petróleo, 59% gas).
    - Fragmentación masiva en variables categóricas (47% "No Reporta").
    - Outliers extremos identificados en `petroleo_bbl`.
- **Razón**: Definir la estrategia de limpieza; los resultados se integraron en el README.md.
- **Autor**: Antigravity (AI Agent)

### [2026-05-12] - Definición del Plan de Limpieza
- **Decisión**: Crear un documento formal (`plan de limpieza.md`) que detalle las técnicas de inferencia y filtrado.
- **Estrategias Clave**:
    - Inferencia de formaciones basada en el campo.
    - Eliminación de registros con doble cero en producción.
    - Uso de transformaciones logarítmicas para gestionar outliers.
- **Razón**: Maximizar la cantidad de datos útiles (Data Maximization) antes de iniciar la codificación en `src/`.
- **Autor**: Antigravity (AI Agent)

### [2026-05-12] - Justificación Estadística de Imputación
- **Decisión**: Utilizar la **mediana** para la imputación de `duracion_dias`.
- **Razón**: El dataset presenta alta varianza operacional. La mediana es un estadístico robusto que no se ve afectado por pruebas excepcionalmente largas (outliers) ni por distribuciones sesgadas, a diferencia de la media.
- **Autor**: Antigravity (AI Agent)

### [2026-05-12] - Vinculación de Anexos Técnicos
- **Decisión**: Añadir enlaces directos en el `README.md` a documentos detallados como el `plan de limpieza.md`.
- **Razón**: Mantener la legibilidad del documento principal sin sacrificar la profundidad técnica necesaria para la implementación.
- **Autor**: Antigravity (AI Agent)

### [2026-05-12] - Propuesta de Arquitectura de Software
- **Decisión**: Diseñar un plan de implementación basado en POO orientado a componentes para `src/limpieza.py`.
- **Principios**: KISS, PEP 8, y modularidad por componentes.
- **Razón**: Asegurar que cada fase del pipeline sea independiente y fácil de ajustar sin efectos secundarios.
- **Autor**: Antigravity (AI Agent)

---
*Última actualización: 2026-05-12*
