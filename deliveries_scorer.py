""" Deliveries_Scorer scores Deliveries 

Description
    How to score deliveries is explained in docs/practice_round_2021.pdf file. 
    For each delivery, the delivery score is the square of the 
    total number of different ingredients of all the pizzas in the delivery. 
    The total score is the sum of the scores for all deliveries. 

Example 
    deliveries_scorer = Deliveries_Scorer(my_deliveries, my_pizzas_data)
    deliveries_score = deliveries_scorer.calculate_score()
    print(deliveries_score)
"""

from deliveries import Deliveries, Delivery
from pizzas import Pizzas


class Deliveries_Scorer:
    def __init__(self, deliveries_data: Deliveries, pizzas_data: Pizzas):
        self._deliveries: list[Delivery] = deliveries_data.deliveries
        self._pizzas_data: Pizzas = pizzas_data

    def calculate_score(self) -> int:
        """ Calculates the total score of the deliveries
        
            The total score of the deliveries is the sum of the scores of every Delivery. 
        """

        total_deliveries_score = 0

        for delivery in self._deliveries:
            delivery_score = self._calculate_delivery_score(delivery)
            total_deliveries_score += delivery_score

        return total_deliveries_score
    
    def _calculate_delivery_score(self, delivery: Delivery):
        """ Calculates the score of a delivery 

            The delivery score is the square of the 
            total number of different ingredients of all the pizzas in the delivery.
        """

        total_different_ingredients = self._get_total_different_ingredients(delivery) 
        delivery_score = total_different_ingredients**2
        return delivery_score

    def _get_total_different_ingredients(self, delivery: Delivery):
        """ Gets the Total Unique Ingredients of a Delivery

            For every pizza in a delivery, add its ingredients to a set. 
            The set only contains unique items, so there will be no duplicate ingredients.
            Return the size of the set. 
        """

        total_different_ingredients_set = set() 

        for pizza_id in delivery.pizza_ids:
            ingredients_list = self._pizzas_data.get_pizza(pizza_id)
            total_different_ingredients_set.update(ingredients_list) # O(k) where k is the size of the item being added to set

        return len(total_different_ingredients_set)
