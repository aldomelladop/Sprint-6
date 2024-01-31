"""
Módulo para realizar un Análisis Exploratorio de Datos (EDA) básico en un archivo CSV.
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1  Importar los archivos - Lectura de los archivos
try:
    res_01 = pd.read_csv('./datasets/project_sql_result_01.csv')
    res_04 = pd.read_csv('./datasets/project_sql_result_04.csv')
    res_07 = pd.read_csv('./datasets/project_sql_result_07.csv')
except FileNotFoundError:
    res_01 = pd.read_csv('project_sql_result_01.csv')
    res_04 = pd.read_csv('project_sql_result_04.csv')
    res_07 = pd.read_csv('project_sql_result_07.csv')

# 2  Descripción de los datos - Descripción de las columnas en el DataFrame project_sql_result_01.csv:
"""
    company_name: nombre de la empresa de taxis
    trips_amount: el número de viajes de cada compañía de taxis el 15 y 16 de noviembre de 2017.
    Se verificó que los nombres de las columnas están en snake_case, que sus tipos de datos son concordantes con la información mostrada y su nomenclatura es la adecuada.

    Descripción de las columnas en el DataFrame project_sql_result_04.csv:

    dropoff_location_name: barrios de Chicago donde finalizaron los viajes
    average_trips: el promedio de viajes que terminaron en cada barrio en noviembre de 2017.
    Se verificó que los nombres de las columnas están en snake_case, que sus tipos de datos son concordantes con la información mostrada y su nomenclatura es la adecuada.
"""

# 3  Asegurarte de que los tipos de datos sean correctos
print(res_01.dtypes)
print()
print(res_04.dtypes)

# Analizamos el tipo de datos de las columnas del dataFrame 
print(res_01.info())
print()
print(res_04.info())

# Verificamos si hay valores NaN
print("\nValores NaN:\n\t",res_01.isna().sum())
print("\nValores NaN:\n\t",res_04.isna().sum())

# Creación de función que permite hallar valores repetidos en columnas específicas
def hallar_repetidos(df):
    """
    Analiza las columnas del dataFrame para encontrar duplicados implícitos, es decir,
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

# Uso de la función:  comprobamos que no existen duplicados implícitos en las columnas seleccionadas

repetidos_01 = hallar_repetidos(res_01)
print("\nDuplicados implícitos:\n", repetidos_01)

repetidos_04 = hallar_repetidos(res_04)
print("\nDuplicados implícitos:\n", repetidos_04)


#Etapa de preprocesamiento de Datos (EDA)
"""
    Datos Nulos Se observa nula presencia de valores NaN en las columnas de ambos dataFrames, a la vez que se observa que el tipo de dato de las colunmas de datos es el correcto y el esperado para estas.
    Snake_case Se observa que el nombre de las variables satisface el standard
    Datos duplicados No se observan duplicados implícitos en el dataframe res_01 y aunque si se observan en res_04, esto no afecta el análisis por cuanto tiene sentido que estos valores numéricos se repitan al ser vlaores de propinas.
    estudiar los datos que contienen asegurarte de que los tipos de datos sean correctos identificar los 10 principales barrios en términos de finalización del recorrido hacer gráficos: empresas de taxis y número de viajes, los 10 barrios principales por número de finalizaciones sacar conclusiones basadas en cada gráfico y explicar los resultados
"""

#4  Identificar los 10 principales barrios en términos de finalización del recorrido

# Agrupa por 'dropoff_location_name' y cuenta las ocurrencias
neighbourhood = res_04.groupby('dropoff_location_name')['average_trips'].sum()

# Ordena los resultados en orden descendente y obtiene los primeros 10
top_10 = neighbourhood.sort_values(ascending=False).head(10)

# Imprime los resultados
print(top_10)

plt.figure(figsize=(10,6))
sns.barplot(x=top_10.values.round(2), y=top_10.index)
plt.title('Top 10 Barrios por Número de Finalizaciones')
plt.xlabel('Ingreso promedio por viaje')
plt.ylabel('Barrio')
plt.grid(alpha = 0.15)
plt.show()

# Agrupa por empresa de taxi y cuenta los viajes
taxi_trips = res_01.groupby('company_name')['trips_amount'].sum()

# Ordena los resultados en orden descendente y obtiene los primeros 10
top_10_taxi_trips = taxi_trips.sort_values(ascending=False).head(10)

# Imprime los resultados
print(top_10_taxi_trips)


plt.figure(figsize=(10,6))
sns.barplot(x= top_10_taxi_trips.values, y= top_10_taxi_trips.index)
plt.title('Empresas de Taxis y Número de Viajes')
plt.xlabel('Ingresos totales [USD]')
plt.ylabel('Nombre de la Empresa')
plt.grid(alpha = 0.15)
plt.show()


#4.1  Conclusiones preliminares
"""
El gráfico, "Top 10 Barrios por Número de Finalizaciones", clasifica los barrios según el volumen de viajes finalizados en ellos, con "Loop" a la cabeza, sugiriendo que es el barrio más activo en términos de servicios de taxi. Además, se proporciona información sobre los ingresos promedio por viaje, lo que podría señalar la rentabilidad de viajar a esos barrios. Esto podría indicar que ciertos barrios no solo son populares destinos sino también más lucrativos para los conductores de taxi.

En el gráfico "Empresas de Taxis y Número de Viajes", se ve que "Flash Cab" lidera el mercado en términos de número de viajes. La competencia entre las empresas se hace evidente, y este ranking podría ser crucial para entender las dinámicas del mercado y la cuota de mercado de cada empresa.

En conjunto, estos gráficos son una herramienta valiosa para entender la distribución geográfica de la demanda de taxis y las operaciones de las empresas de taxis. Los datos podrían utilizarse para tomar decisiones estratégicas sobre la asignación de recursos, la identificación de áreas de alta demanda, y para optimizar los servicios de transporte en la ciudad.
"""

# 5  Importamos datos de clima
"""
    start_ts: fecha y hora de la recogida
    weather_conditions: condiciones climáticas en el momento en el que comenzó el viaje
    duration_seconds: duración del viaje en segundos
"""

#5.1  Prueba la hipótesis:
"La duración promedio de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare cambia los sábados lluviosos"

print(res_01.columns)
print()
print(res_04.columns)
print()
print(res_07.columns)


 #Convertimos las fechas a formato datetime
res_07['start_ts'] = pd.to_datetime(res_07['start_ts']) #Convertimos las fechas a formato datetime
res_07['day_of_week'] = res_07['start_ts'].dt.dayofweek # Obtenemos el día de la semana para cada viaje


rainy_saturdays = res_07[ (res_07['day_of_week'] == 5) & (res_07.weather_conditions == 'Bad')]
print(rainy_saturdays)

duration_rainy_saturdays = rainy_saturdays['duration_seconds']
print(duration_rainy_saturdays)

non_rainy_saturdays = res_07[ (res_07['day_of_week'] == 5) & (res_07.weather_conditions == 'Good')]
duration_non_rainy_saturdays = non_rainy_saturdays['duration_seconds']
print(duration_non_rainy_saturdays)
print(duration_non_rainy_saturdays)


#5.2  Información preliminar
# Antes de evaluar el resultado de la prueba, podemos hacer una comparación a priori de manera gráfica y de manera cuántitativa, esto nos permitirá visualizar la distribución de los datos y cotejar con los resultados de la t-test

print(f"Duración media en dias de no lluvia {duration_non_rainy_saturdays.mean()}")
print(f"\nDuración media en dias de lluvia {duration_rainy_saturdays.mean()}")
print(f"\nDiferencia porcentual lluvia v/s no lluvia: {((duration_non_rainy_saturdays.mean()-duration_rainy_saturdays.mean())/duration_non_rainy_saturdays.mean())*100:.2f}%")

#El resultado final es la reducción o incremento porcentual en la duración promedio de los viajes de sábados lluviosos en comparación con los sábados no lluviosos.

print(duration_rainy_saturdays)
duration_rainy_saturdays = duration_rainy_saturdays.astype(float)
duration_non_rainy_saturdays = duration_non_rainy_saturdays.astype(float)

# Crear un DataFrame para el boxplot con pandas
data_to_plot = pd.DataFrame({
    'Rainy Saturdays': duration_rainy_saturdays,
    'Non-Rainy Saturdays': duration_non_rainy_saturdays
})

# Graficar el boxplot
plt.figure(figsize=(10, 8))
data_to_plot.boxplot()
plt.title('Duration of Trips on Rainy vs Non-Rainy Saturdays')
plt.ylabel('Duration in Seconds')
plt.show()

# 5.3  Hipótesis
"""
    Para probar la hipótesis mencionada, debemos primero formular nuestras hipótesis nula y alternativa:

    Hipótesis nula (H0): La duración promedio de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare no cambia los sábados lluviosos, es decir, la lluvia no tiene efecto en la duración del viaje.
    Hipótesis alternativa (H1): La duración promedio de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare cambia los sábados lluviosos.
    5.4  Nivel de significación
    El siguiente paso es decidir el nivel de significación (α), que es la probabilidad de rechazar la hipótesis nula cuando es cierta (error tipo I). Un nivel comúnmente usado es 0.05, pero dependiendo de la gravedad de cometer un error tipo I, podrías elegir un nivel más conservador como 0.01 o más liberal como 0.1.

    El criterio para probar las hipótesis depende del p-valor obtenido del test estadístico:

    Si el p-valor es menor que α,

    rechazas la hipótesis nula y concluyes que hay suficiente evidencia para afirmar que la duración promedio del viaje cambia los sábados lluviosos.
    Si el p-valor es mayor que α,

    no rechazas la hipótesis nula y concluyes que no hay suficiente evidencia para afirmar que la duración promedio del viaje cambia los sábados lluviosos.
    Si el p-valor resultante de la prueba eresulta ser menor que el nivel de significancia preestablecido (0.05), entonces rechazamos la hipótesis nula y aceptamos la hipótesis alternativa, concluyendo que existe una diferencia estadísticamente significativa.
"""

from scipy import stats

# Tenemos dos listas: 
# que contienen la duración de los viajes en segundos para sábados lluviosos y no lluviosos, respectivamente.

# Realiza la prueba T-test
t_stat, p_value = stats.ttest_ind(duration_rainy_saturdays, duration_non_rainy_saturdays, equal_var=True)

# Imprime los resultados
print(f"Estadístico T: {t_stat}")
print(f"Valor P: {p_value}")

# Interpreta los resultados
alpha = 0.05  # Nivel de significancia comúnmente usado
if p_value < alpha:
    print("Rechazamos la hipótesis nula: hay una diferencia significativa en las medias.")
else:
    print("No rechazamos la hipótesis nula: no hay una diferencia significativa en las medias.")


#6  Conclusiones
#Dado que el valor P es menor que 0.05, rechazamos la hipótesis nula. Esto sugiere que hay una diferencia estadísticamente significativa en la duración promedio de los viajes entre sábados lluviosos y no lluviosos. En términos prácticos, esto podría indicar que el clima lluvioso afecta la duración de los viajes en la fecha y ubicación especificadas en la hipótesis, pero también es importante señalar que correlación no implica causalidad, de modo que el tener un valor tal puede no deberse a ese motivo, ya sea por si solo o en su conjunto y por ende es importante revisar y ejecutar más pruebas.

#6.1  Criterios de selección t-test
"""
    El razonamiento detrás de la elección de un t-test o cualquier prueba estadística debe basarse en el diseño de tu estudio y las características de tus datos, siendo para este problema un conjunto de datos pequeños, los cuales presentan varianzas y medias diferentes. Sus datos no se reparten de manera, tal y como lo pudimos ver en boxplot de más arriba.

    Un viaje en un sábado lluvioso no debería influir en los viajes de un sábado no lluvioso, por lo que podemos asumir que estas muestras de datos son independientes entre sí.

    El valor-p informa sobre la probabilidad de observar una diferencia al menos tan extrema como la observada, dado que la hipótesis nula (la suposición de que no hay diferencia) es cierta. Un valor-p bajo sugiere que tal diferencia sería muy improbable bajo la hipótesis nula, por lo que se puede rechazar la hipótesis nula a favor de la hipótesis alternativa (la suposición de que hay una diferencia).
"""