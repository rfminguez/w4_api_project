#!/usr/bin/env python3
import sys
import argparse

import src.input_csv_dataset as i_csv


def setup_arguments(parser):
    group = parser.add_mutually_exclusive_group()

    group.add_argument("-n",
                        dest = "name",
                        help = "Buscar restaurantes por nombre.")

    group.add_argument("-r",
                        dest = "region",
                        help = "Buscar restaurantes por region.")

    group.add_argument("-c", 
                        dest="city",
                        help = "Buscar restaurantes por ciudad.")

    group.add_argument("-s", 
                        dest="stars",
                        help = "Buscar restaurantes por número de estrellas.",
                        type = int,
                        choices = [1, 2, 3]
                        )

    group.add_argument("-p", 
                        dest="price",
                        help = "Buscar restaurantes por categoría de precio (valores válidos: entre 1 y 5).",
                        type = int,
                        choices = [1, 2, 3, 4, 5]
                        )

    group.add_argument("--list_cities", 
                        dest="list_cities",
                        help = "Listado de ciudades.",
                        action = "store_true"
                        )

    group.add_argument("--list_regions", 
                        dest="list_regions",
                        help = "Listado de regiones.",
                        action = "store_true"
                        )

    group.add_argument("--top_cities", 
                        dest="top_cities",
                        help = "Listado de las ciudades con más restaurantes.",
                        action = "store_true"
                        )

    group.add_argument("--top_regions", 
                        dest="top_regions",
                        help = "Listado de las regiones con más restaurantes.",
                        action = "store_true"
                        )


    return parser


def get_arguments(parser):
    parser = setup_arguments(parser)
    return parser.parse_args()


def main():
    # Creo el parser
    parser = argparse.ArgumentParser(description="Predicción meteorológica para restaurantes en la Guía Michelín.")

    # Obtengo los args
    args = get_arguments(parser)

    nombre = args.name
    region = args.region
    ciudad = args.city
    estrellas = args.stars
    precio = args.price
    consulta_ciudades = args.list_cities 
    consulta_regiones = args.list_regions
    top_ciudades = args.top_cities
    top_regiones = args.top_regions

    # Creo un objeto para trabajar con todos los .CSV
    restaurants = i_csv.Restaurants(
        'input/one-star-michelin-restaurants.csv',
        'input/two-stars-michelin-restaurants.csv',
        'input/three-stars-michelin-restaurants.csv'
    )

    # La lógica del programa:
    if nombre:
        # En este método es donde uso la API para regocer los datos meteorológicos.
        print(restaurants.get_by_name(nombre))

    if region:
        print(restaurants.get_by_region(region))
    
    if ciudad:
        print(restaurants.get_by_city(ciudad))

    if estrellas:
        print(restaurants.get_by_stars(estrellas))

    if precio:
        print(restaurants.get_by_price(precio))

    if consulta_ciudades:
        print(restaurants.get_list_of_cities())

    if consulta_regiones:
        print(restaurants.get_list_of_regions())

    if top_ciudades:
        print(restaurants.get_top_cities())

    if top_regiones:
        print(restaurants.get_top_regions())



if __name__ == "__main__":
    main()
