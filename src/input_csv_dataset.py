import pandas as pd
from src.restaurant import Restaurant

class Restaurants():
    def __init__(self, csv_one_star, csv_two_stars, csv_three_stars):
        # Saco cada dataframe en un fichero
        df_one_star = pd.read_csv('input/one-star-michelin-restaurants.csv')
        df_two_stars = pd.read_csv('input/two-stars-michelin-restaurants.csv')
        df_three_stars = pd.read_csv('input/three-stars-michelin-restaurants.csv')

        # Creo una variable para indicar el número de estrellas (en función del fichero del que vengan los datos)
        df_one_star["stars"] = 1
        df_two_stars["stars"] = 2
        df_three_stars["stars"] = 3

        # Junto los tres dataframes
        self.df_restaurants = pd.concat([df_one_star, df_two_stars, df_three_stars])

        # Limpio los valores NaN en la columna "price" sustituyéndolos por cadenas vacías.
        self.df_restaurants = self.df_restaurants.fillna(value={"price":""})

        # Creo un campo auxiliar para buscar por precio.
        self.df_restaurants["price_num"] = self.df_restaurants["price"].apply(lambda s: len(s))

    def get_by_name(self, name):
        '''
        receives: the name of a restaurant.
        returns: the restaurants with this name and the weather report for each one.
        '''
        list_of_restaurants = []

        result = self.df_restaurants[self.df_restaurants["name"] == name]
        for index, row in result.iterrows():
            restaurant = Restaurant(row['name'], 
                                    row['city'], 
                                    row['region'], 
                                    row['latitude'],
                                    row['longitude'],
                                    row['cuisine'], 
                                    row['price'],
                                    row['stars'])

            list_of_restaurants.append(restaurant)

        # el resultado es un dataframe con cero, uno o varios restaurantes
        #for r in list_of_restaurants:
        #    print(r)
        
        if len(list_of_restaurants) == 0:
            return "No hay restaurantes con ese nombre"
        # return result if len(result) > 0 else "No hay restaurantes con ese nombre."
        return list_of_restaurants

    def get_by_region(self, region):
        result = self.df_restaurants[self.df_restaurants["region"] == region][['name', 'city', 'cuisine', 'price', 'stars']]
        return result if len(result) > 0 else "No hay restaurantes en esa región."

    def get_by_city(self, city):
        result = self.df_restaurants[self.df_restaurants["city"] == city][['name', 'region', 'cuisine', 'price', 'stars']]
        return result if len(result) > 0 else "No hay restaurantes en esa ciudad."

    def get_by_stars(self, stars):
        result = self.df_restaurants[self.df_restaurants["stars"] == stars][['name', 'city', 'region', 'cuisine', 'price']]
        return result if len(result) > 0 else "Estrellas debe ser un entero entre 1 y 3."

    def get_by_price(self, price):
        #print(self.df_restaurants[self.df_restaurants["name"] == "West House"][['price', 'price_num']])
        result = self.df_restaurants[self.df_restaurants["price_num"] == price][['name', 'city', 'region', 'cuisine', 'stars']]
        return result if len(result) > 0 else "Precio debe ser un entero entre 1 y 5."

    def get_list_of_cities(self):
        return self.df_restaurants["city"].unique()

    def get_list_of_regions(self):
        return self.df_restaurants["region"].unique()

    def get_top_cities(self):
        result = self.df_restaurants.groupby("city")["name"].count().sort_values(ascending=False).head()
        return result

    def get_top_regions(self):
        result = self.df_restaurants.groupby("region")["name"].count().sort_values(ascending=False).head()
        return result
