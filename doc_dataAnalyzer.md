## Documentación para la Clase `DataAnalyzer`

### Descripción General
`DataAnalyzer` es una clase diseñada para realizar un Análisis Exploratorio de Datos (EDA) básico en archivos CSV. Proporciona funcionalidades para cargar datos, normalizar nombres de columnas, verificar y eliminar duplicados, y mostrar un resumen del conjunto de datos.

### Métodos de la Clase

#### `__init__(self, file_name: str)`
Constructor de la clase.
- **Parámetros**:
  - `file_name` (str): Ruta o nombre del archivo CSV a analizar.
- **Retorna**: No retorna nada.

#### `load_data(self) -> bool`
Intenta cargar el archivo CSV en un DataFrame.
- **Retorna**: 
  - `True` si el archivo se carga correctamente.
  - `False` si no se encuentra el archivo.

#### `normalize_column_names(self)`
Normaliza los nombres de las columnas del DataFrame a snake_case.
- **Retorna**: No retorna nada.

#### `check_for_duplicates(self)`
Verifica y elimina filas duplicadas en el DataFrame.
- **Retorna**: No retorna nada.

#### `show_summary(self)`
Muestra un resumen del DataFrame, incluyendo estadísticas descriptivas y gráficos.
- **Retorna**: No retorna nada.

#### `execute_analysis(self, normalize_cols=True, check_duplicates=True, show_summary_flag=True)`
Ejecuta el análisis completo en el archivo CSV proporcionado.
- **Parámetros**:
  - `normalize_cols` (bool): Si se deben normalizar los nombres de columnas (default `True`).
  - `check_duplicates` (bool): Si se deben verificar y eliminar duplicados (default `True`).
  - `show_summary_flag` (bool): Si se debe mostrar un resumen del DataFrame (default `True`).
- **Retorna**: `pd.DataFrame` o `None` en caso de error.

### Uso de la Clase
Para utilizar la clase `DataAnalyzer`, primero debes instanciarla con el nombre del archivo CSV y luego llamar al método `execute_analysis`. Por ejemplo:

```python
# Instanciar la clase con el nombre del archivo
analyzer = DataAnalyzer("mi_archivo.csv")

# Ejecutar el análisis
analyzer.execute_analysis()
```

### Dependencias
- pandas
- numpy
- matplotlib
- seaborn