import pandas as pd

class Restaurants():
    def __init__(self, csv_one_star, csv_two_stars, csv_three_stars):
        df_one_star = pd.read_csv('input/one-star-michelin-restaurants.csv')
        df_two_stars = pd.read_csv('input/two-stars-michelin-restaurants.csv')
        df_three_stars = pd.read_csv('input/three-stars-michelin-restaurants.csv')

        df_one_star["stars"] = 1
        df_two_stars["stars"] = 2
        df_three_stars["stars"] = 3

        self.df_restaurants = pd.concat([df_one_star, df_two_stars, df_three_stars])

    def get_by_name(self, name):
        result = self.df_restaurants[self.df_restaurants["name"] == name]
        return result if len(result) > 0 else "No hay restaurantes con ese nombre."

    def get_by_region(self, region):
        result = self.df_restaurants[self.df_restaurants["region"] == region]
        return result if len(result) > 0 else "No hay restaurantes en esa región."

    def get_by_city(self, city):
        result = self.df_restaurants[self.df_restaurants["city"] == city]
        return result if len(result) > 0 else "No hay restaurantes en esa ciudad."

    def get_by_stars(self, stars):
        result = self.df_restaurants[self.df_restaurants["stars"] == stars]
        return result if len(result) > 0 else "Estrellas debe ser un entero entre 1 y 3."

    def get_by_price(self, price):
        result = self.df_restaurants[self.df_restaurants["price"] == price]
        return result if len(result) > 0 else "Precio debe ser un entero entre 1 y 5."

    def get_list_of_cities(self):
        # no funciona :(
        return self.df_restaurants["city"].unique()