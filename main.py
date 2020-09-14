#!/usr/bin/env python3
import sys
import argparse
from fpdf import FPDF
from src.restaurant import Restaurant

import src.input_csv_dataset as i_csv


def setup_arguments(parser):
    '''
    En esta función configuro los parámetros que va a aceptar el programa.
    '''
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

    group.add_argument("--report_to_pdf", 
                        dest="report_to_pdf",
                        help = "Buscar restaurantes por nombre y exportar datos a .PDF"
                        )

    return parser


def get_arguments(parser):
    '''
    Recibe: un objeto Parser de argparse.
    Devuelve: los argumentos que ha recibido desde CLI.
    '''
    parser = setup_arguments(parser)
    return parser.parse_args()


def pdf_setup():
    '''
    Función para configurar los parámetros básicos de FPDF.
    Devuelve un objeto pdf.
    '''
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "", 12)
    return pdf


def to_pdf(pdf, report_results, file_name="restaurant_report"):
    '''
    Recibe: un objeto pdf y un diccionario donde cada elemento es una cadena de texto.
    Devuelve: genera un fichero pdf en la carpeta output.
    '''
    # Recorro los restaurantes (normalmente hay uno solo, pero puede haber más) y los añado al PDF.
    for restaurant in report_results:
        texto = str(restaurant)
        pdf.multi_cell(0, 5, texto, border="B") # Pinto el borde inferior como separador por si hay varios restaurantes.
        pdf.ln()

    # Escribo el fichero PDF
    pdf.output(f"./output/{file_name}.pdf")


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
    prediccion_a_pdf = args.report_to_pdf

    # Creo un objeto para trabajar con los datos de los .CSV
    restaurants = i_csv.Restaurants(
        'input/one-star-michelin-restaurants.csv',
        'input/two-stars-michelin-restaurants.csv',
        'input/three-stars-michelin-restaurants.csv'
    )

    # La lógica del programa:
    # Cada uno de estos IF corresponde a un argumento y consulta al objeto restaurants.
    if nombre:
        # En este método es donde uso la API para regocer los datos meteorológicos.
        report_results = restaurants.get_by_name(nombre)
        if type(report_results) == list:
            for restaurant in restaurants.get_by_name(nombre):
                print(restaurant)
        else:
            print(report_results)

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

    if prediccion_a_pdf:
         # Obtengo una lista de restaurantes consultando por nombre
        name = prediccion_a_pdf
        report_results = restaurants.get_by_name(name)

        # Si lo que nos devuelve es una lista es que hay restaurantes con ese nombre:
        if type(report_results) == list:
            to_pdf(pdf_setup(), report_results)
        else:
            # En caso contrario es que no ha encontrado restaurantes. Imprimo el mensaje devuelto por cli:
            print(report_results)


if __name__ == "__main__":
    main()
