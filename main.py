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

    group.add_argument("-c", dest="city",
                        help = "Buscar restaurantes por ciudad.")

    group.add_argument("-s", dest="stars",
                        help = "Buscar restaurantes por número de estrellas.",
                        type = int,
                        choices = [1, 2, 3]
                        )

    group.add_argument("-p", dest="price",
                        help = "Buscar restaurantes por categoría de precio (valores válidos: entre 1 y 5).",
                        type = int,
                        choices = [1, 2, 3, 4, 5]
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

    print("---")
    print(args)
    print("---")


    nombre = args.name
    region = args.region
    ciudad = args.city
    estrellas = args.stars
    precio = args.price

    print(f"{nombre} {region} {ciudad} {estrellas} {precio}")


    # Creo un objeto para trabajar con todos los .CSV
    restaurants = i_csv.Restaurants(
        'input/one-star-michelin-restaurants.csv',
        'input/two-stars-michelin-restaurants.csv',
        'input/three-stars-michelin-restaurants.csv'
    )

    # La lógica del programa
    if nombre:
        print(restaurants.get_by_name(nombre))
        # Aquí debería llamar a la API para regocer los datos meteorológicos.

    if region:
        print(restaurants.get_by_name(region))
    
    if ciudad:
        print(restaurants.get_by_city(ciudad))

    if estrellas:
        print(restaurants.get_by_stars(estrellas))

    if estrellas:
        print(restaurants.get_by_price(precio))

    restaurants.get_list_of_cities()

if __name__ == "__main__":
    main()
