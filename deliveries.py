from pizzas import Pizzas
from teams import Teams
from globals import *


class Deliveries:
    def __init__(self, filepath: str):
        self.deliveries = [] # [Size of team + Pizza ID's]

        self._init_deliveries(filepath)

    def _init_deliveries(self, filepath: str):
        file = open(filepath, "r")
        _ = file.readline()  # Number of Pizza Deliveries : Redundant Info

        for line in file: 
            line = line.strip() # remove newline: "3 0 2 3\n" -> "3 0 2 3"
            line = line.split(" ") # get list spilt on space: "3 0 2 3" -> ["3", "0", "2", "3"]
            line = [int(x) for x in line] # convert list of strings to list of ints: ["3", "0", "2", "3"] -> [3, 0, 2, 3]
            self.deliveries.append(line)
        
    
class Deliveries_Validator:
    def __init__(self, deliveries: Deliveries, teams_data: Teams):
        self.deliveries = deliveries
        self.teams = teams_data

        self._validate_deliveries()

    def _validate_deliveries(self):
        if not self.validate_data(self.deliveries, self.teams):
            print("Log: There was an error with validation!")
            exit()
    
    def check_pizza_clones(self, deliveries: Deliveries):
        # Check 1: Pizza ID is used only once.
        pizza_id_list = []
        
        for delivery in deliveries.deliveries:
            pizza_ids = delivery[1:]
            for pizza_id in pizza_ids:
                if pizza_id in pizza_id_list:
                    return False
                else:
                    pizza_id_list.append(pizza_id)

        return True 

    def check_team_fed(self, deliveries: Deliveries):
        # Check 2: If Team Size N, N Pizzas 
        for delivery in deliveries.deliveries:
            team_size = delivery[0]
            pizzas_in_delivery = len(delivery) - 1
            if team_size != pizzas_in_delivery:
                return False

        return True 

    def check_team_size(self, team_size, deliveries: Deliveries, teams_data: Teams):
        count_deliveries_of_team_size = 0
        for delivery in deliveries.deliveries: 
            delivery_team_size = delivery[0] 
            if team_size == delivery_team_size:
                count_deliveries_of_team_size += 1

        return count_deliveries_of_team_size <= teams_data.get_number_of_teams_of_size(team_size)

    def validate_data(self, deliveries: Deliveries, teams_data: Teams):
        if not self.check_pizza_clones(deliveries):
            return False

        if not self.check_team_fed(deliveries):
            return False
        
        for team_size in TEAM_SIZES:
            if not self.check_team_size(team_size, deliveries, teams_data):
                return False

        return True 


class Deliveries_Scorer:
    def __init__(self, deliveries: Deliveries, pizzas_data: Pizzas):
        self.deliveries = deliveries
        self.pizzas_data = pizzas_data
        self.total_score = 0

        self._get_score()

    def get_ingredients(self, pizza_id):
        ingredients: tuple = self.pizzas_data.get_pizza(pizza_id)
        return ingredients

    def delivery_scoring(self, delivery: list):
        delivery_score = 0
        pizza_ids = delivery[1:]  # first int is the team size: Redundant Info
        unique_ingredients = set()

        for pizza_id in pizza_ids:
            ingredients: tuple = self.get_ingredients(pizza_id)
            for ingredient in ingredients:
                unique_ingredients.add(ingredient)
        
        delivery_score = len(unique_ingredients)**2
        return delivery_score

    def _get_score(self):

        for delivery in self.deliveries.deliveries:
            delivery_score = self.delivery_scoring(delivery)
            self.total_score += delivery_score
