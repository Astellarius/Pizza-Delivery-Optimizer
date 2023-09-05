""" Scorer scores deliveries 

Description
    How to score deliveries is explained in docs/practice_round_2021.pdf file. 
    For each delivery, the delivery score is the square of the 
    number of unique toppings of the pizzas in the delivery. 
    The total score is the sum of the scores for all deliveries. 

Example 
    scorer = Scorer(input_data_file, delivery_file)
    deliveries_score = scorer.score_deliveries()
"""

from info.pizzas import Pizzas


class Delivery: 
    def __init__(self, team_size: int, pizza_ids: list[int]):
        self.team_size: int = team_size
        self.pizza_ids: list[int] = pizza_ids

    def get_unique_toppings_count(self, pizzas_data: Pizzas) -> int:
        unique_toppings = set() 

        for pizza_id in self.pizza_ids:
            toppings = pizzas_data.get_pizza(pizza_id)
            unique_toppings.update(toppings) # O(k) where k is the size of the item being added to set

        unique_toppings_count = len(unique_toppings)
        return unique_toppings_count


class Scorer:
    def __init__(self, input_data_file, delivery_file):
        self.deliveries: list[Delivery] = self._generate_deliveries(delivery_file)
        self.pizzas_data = Pizzas(input_data_file)

    def _generate_deliveries(self, delivery_file):
        deliveries = []

        file = open(delivery_file, "r")

        _ = file.readline()  # Number of Pizza Deliveries : Redundant Info

        for line in file: 
            line = line.strip() # remove newline: "3 0 2 3\n" -> "3 0 2 3"
            line = line.split(" ") # get list spilt on space: "3 0 2 3" -> ["3", "0", "2", "3"]
            line = [int(x) for x in line] # convert list of strings to list of ints: ["3", "0", "2", "3"] -> [3, 0, 2, 3]

            # Separate team_size from pizza_id's 
            team_size = line[0] 
            pizza_ids = line[1:]
            delivery = Delivery(team_size, pizza_ids)
            deliveries.append(delivery)
        
        return deliveries


    def score_deliveries(self):
        deliveries_score = 0
        for delivery in self.deliveries:
            deliveries_score += self.score_delivery(delivery)
        return deliveries_score 
    
    def score_delivery(self, delivery: Delivery):
        total_different_ingredients = delivery.get_unique_toppings_count(self.pizzas_data)
        delivery_score = total_different_ingredients**2
        return delivery_score
