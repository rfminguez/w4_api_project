# Behold!
¿Quieres organizar una cena en un restaurante de postín y no quieres arriesgarte a que el mal tiempo te la arruine? ¡Estás de suerte! Con este programa puedes consultar una serie de restaurantes de 1, 2 y 3 estrellas Michelín y obtener una predicción meteorológica para la próxima hora.

## Disclaimer:
Este proyecto es una PoC para uno de los proyectos semanales de IronHack y hace uso de un dataset sacado de www.kaggle.com con datos de restaurantes para los años 2018 y 2019 junto a la api de openweathermap.org.

Mi intención es cruzar datos de restaurantes con datos meteorológicos sacados de la API en un programa de línea de comandos para hacer reports.

## TO-DO:
Añadir previsión para los próximos días.

Añadir previsión para una hora concreta.

Estos datos los tengo porque los proporciona la API pero por falta de tiempo y habilidad no he conseguido incluir esta funcionalidad.


# Dataset:
Voy a usar este dataset sacado de kaggle:

https://www.kaggle.com/jackywang529/michelin-restaurants

Es un conjunto de tres CSV con restaurantes de la guía michelin de los años 2018 y 2019.

## Estructura del dataset
Las columnas del dataset son:
- name:         nombre del restaurante.
- year:         año en que aparece en la guía.
- latitude:     coordenadas de latitud (gracias a esta columna podemos cruzar datos con la API).
- longitude:    coordenadas de longitud (ídem).
- city:         ciudad.
- region:       región.
- zipCode:      código postal (no lo usamos).
- cuisine:      tipo de cocina
- price:        categorización del precio en símbolos de dolar (de más barato $ a más caro $$$$$).
- url:          web del restaurante (no lo usamos).
- stars:        estrellas michelín.

Una vez unidos los tres CSV el dataset resultanto tiene 695 entradas.

# API:
Voy a utilizar la API de openweathermap:

https://openweathermap.org/

Permite registrarse de forma gratuíta con un límite de 60 consultas por minuto. 

Dado el límite de consultas reduzco el análisis meteorológico a restaurantes individuales para no consumir demasiado rápido la cuota.

## Endpoint
La página nos proporciona varios endpoints para obtener datos históricos, diarios y predicciones por horas y para días siguientes. 

Sin embargo me quedo con este endpoint:
https://openweathermap.org/api/one-call-api

Que me proporciona datos de:
- situación actual.
- predicción por minuto para la próxima hora.
- predicción para las próximas 48 horas.
- predicción para los próximos 7 días.
- datos históricos de los 5 días anteriores.

Estos datos los devuelve en formato JSON y es bastante fácil de tratar.

Por lo demás he dejado un par de ejemplos de respuestas en el notebook de análisis de datos.


# Contenido del proyecto
- 00-instrucciones.ipynb: jupyter notebook con el enunciado del ejercicio.
- 01-analisis_de_los_datos.ipynb: análisis preliminar de los datos del dataset y de la API.
- main.py: el programa principal (he separado el código en varios ficheros).
- src/input_csv_dataset.py: código destinado a trabajar con el set de datos descargado de Kaggle.
- src/restaurant.py: código encargado de interactuar con la API de openweathermap.
- output/restaurant_report.pdf: un ejemplo de datos exportados a PDF.

# Uso del programa principal
El programa main.py debería tener permisos de ejecución para poder usarse.

Las opciones que admite son las siguientes:
- "-n": recibe el nombre de un restaurante y muestra la información meteorológica por pantalla. 
Aquí es donde cruzo datos de los CSV con la API.
- "-r": recibe una región y muestra los restaurantes que hay en dicha región.
- "-c": ídem para una ciudad.
- "-s": recibe como argumento el número de estrellas y devuelve los restaurantes con ese ranking.
- "-p": recibe como argumento el precio categorizado y devuelve los restaurantes con ese precio.
- "--list_cities": listado de todas las ciudades.
- "--list_regions": listado de todas las regiones.
- "--top_cities": las cinco ciudades con más restaurantes. Este valor está calculado usando un groupby.
- "--top_regions": ídem pero para regiones.
- "--report_to_pdf": como "-n" pero en vez de devolver la información por pantalla crea un PDF.

Estas opciones son mutuamente exclusivas, así que solo podemos usar una a la vez.

## Ejemplos:
```
usage: main.py [-h]
               [-n NAME | -r REGION | -c CITY | -s {1,2,3} | -p {1,2,3,4,5} | --list_cities | --list_regions | --top_cities | --top_regions | --report_to_pdf REPORT_TO_PDF]

Predicción meteorológica para restaurantes en la Guía Michelín.

optional arguments:
  -h, --help            show this help message and exit
  -n NAME               Buscar restaurantes por nombre.
  -r REGION             Buscar restaurantes por region.
  -c CITY               Buscar restaurantes por ciudad.
  -s {1,2,3}            Buscar restaurantes por número de estrellas.
  -p {1,2,3,4,5}        Buscar restaurantes por categoría de precio (valores válidos: entre 1 y 5).
  --list_cities         Listado de ciudades.
  --list_regions        Listado de regiones.
  --top_cities          Listado de las ciudades con más restaurantes.
  --top_regions         Listado de las regiones con más restaurantes.
  --report_to_pdf REPORT_TO_PDF
                        Buscar restaurantes por nombre y exportar datos a .PDF
```

```
./main.py -n "Balwoo Gongyang"

El restaurante Balwoo Gongyang, de 1 estrella, está en la ciudad de Seoul (South Korea). Sirve comida de tipo Temple cuisine.

El precio es muy caro.

La previsión meteorológica para la próxima hora es:
- Temperatura: 19.3.
- Sensación térmica: 21.73.
- Tiempo: Rain.
- Previsión de lluvia: 0.18
```

```
./main.py --top_cities

city
New York         74
Hong Kong        61
San Francisco    55
Singapore        39
Seoul            26
Name: name, dtype: int64
```

