# Este es el README
¿Quieres organizar una cena en un restaurante de postín y no quieres arriesgarte a que un tiempo de mierda te la arruine? Con este programa puedes consultar una serie de restaurantes de 1, 2 y 3 estrellas de la guía Michelín por su ubicación y obtener una predicción meteorológica con la temperatura actual y prevista para los próximos días.

Este proyecto se trata de una PoC para uno de los proyectos semanales de IronHack y hace uso de un dataset sacado de www.kaggle.com con datos de restaurantes para los años 2018 y 2019 y de la api de openweathermap.org.


## Voy a usar el siguiente dataset:
https://www.kaggle.com/jackywang529/michelin-restaurants

Restaurantes de la guía michelin.

Mi intención es cruzar los datos con datos meteorológicos sacados de una API.

### Tendré que describir la estructura de las filas y columnas del dataset...
El dataset está compuesto de tres CSV (uno para restaurantes de una estrella, otro para restaurantes de dos estrellas y otro para restaurantes de tres estrellas).

Los junto en un único dataset.


## Y esta api:
https://openweathermap.org/

Concretamente:
https://openweathermap.org/api/one-call-api

Que me proporciona dados de:
- tiempo actual.
- previsión por minuto (1 hora).
- previsión por horas (48 horas).
- previsión próximos 7 días.
- datos meteorológicos históricos de 5 días antes.

[ALTERNATIVA] Para pensarlo:
    Aunque también podría usar una combinación de estos dos:
    - Tiempo actual
    https://openweathermap.org/current

    - Previsión diaria (puedes pasarle hasta 7 días con la subscripción gratuita)
    https://openweathermap.org/forecast16
    
### También tendré que describir la estructura del JSON que nos da la API.
En esta página vienen todos los parámetros y valores:
https://openweathermap.org/weather-data

En esta te describe las unidades de temperatura que se pueden adoptar:
https://openweathermap.org/api/one-call-api#data

Me tendré que centrar solo en las que me interesan.