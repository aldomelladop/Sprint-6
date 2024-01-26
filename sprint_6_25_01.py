import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Lectura de los archivos
try:
    res_01 = pd.read_csv('/datasets/project_sql_result_01.csv')
    res_04 = pd.read_csv('/datasets/project_sql_result_04.csv')
except Exception as e:
    res_01 = pd.read_csv('./datasets/project_sql_result_01.csv')
    res_04 = pd.read_csv('./datasets/project_sql_result_04.csv')
    

# Descripción de los datos
"""
    descripción de las columnas en el DataFrame `project_sql_result_01.csv`:
        1. company_name: nombre de la empresa de taxis
        2. trips_amount: el número de viajes de cada compañía de taxis el 15 y 16 de noviembre de 2017. 

        Se verificó que los nombres de las columnas están en snake_case, que sus tipos de datos son concordantes 
        con la información mostrada y su nomenclatura es la adecuada.
"""

"""
    descripción de las columnas en el DataFrame `project_sql_result_04.csv`:
        1. dropoff_location_name: barrios de Chicago donde finalizaron los viajes
        2. average_trips: el promedio de viajes que terminaron en cada barrio en noviembre de 2017.
        
        Se verificó que los nombres de las columnas están en snake_case, que sus tipos de datos son concordantes 
        con la información mostrada y su nomenclatura es la adecuada.
"""

# Analizamos el tipo de datos de las columnas del dataFrame 
print(res_01.info())
print(res_04.info())

# Verificamos si hay valores NaN
print("\nValores NaN:\n", res_01.isna().sum())
print("\nValores NaN:\n", res_04.isna().sum())



# Verificamos si hay valores duplicados en cada columna [No es a lugar para ninguna de las columnas]

# Etapa de preprocesamiento de Datos (EDA)

"""
# Datos Nulos
Se observa nula presencia de valores NaN en las columnas de ambos dataFrames, a la vez que se observa que
el tipo de dato de las colunmas de datos es el correcto y el esperado para estas.

# Snake_case
Se obseva que el nombre de las variables satisface el standard

# Datos duplicados
No se observan duplicados implícitos en el dataframe res_01 y aunque si se observan en res_04, esto no afecta el análisis 
por cuanto tiene sentido que estos valores numéricos se repitan al ser vlaores de propinas.
"""

# Creación de función que permite hallar valores repetidos en columnas específicas


def hallar_repetidos(df):
    """
        Analiza las columnas del dataFrane para encontrar duplicados implicitos, es decir,
        columnas cuyo nombre es similar a otros pero no exactamente iguales.
    """
    columns_to_check = [col for col in df.columns]

    duplicados_dict = {}
    for columna in columns_to_check:
        # Contamos las ocurrencias de cada valor
        value_counts = df[columna].value_counts()
        # Filtramos para quedarnos solo con los valores que se repiten
        repetidos = value_counts[value_counts > 1].index.tolist()

        if repetidos:
            duplicados_dict[columna] = repetidos

    return duplicados_dict


# Uso de la función
# comprobamos que no existen duplicados implícitos en las columnas seleccionadas
repetidos_01 = hallar_repetidos(res_01)
print("\nDuplicados implícitos:\n", repetidos_01)

repetidos_04 = hallar_repetidos(res_04)
print("\nDuplicados implícitos:\n", repetidos_04)
