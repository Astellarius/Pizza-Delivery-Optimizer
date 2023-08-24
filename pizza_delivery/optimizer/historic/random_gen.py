from pizza_delivery.teams import Teams 
from pizza_delivery.pizzas import Pizzas
from pizza_delivery.pizza_delivery_optimizer.outputter import Outputter

import random
# from pizza_delivery.optimizer.globals import *

""" generate deliveries randomly
    are there 4 team's 
    are there 4 pizzas 
    put 4 pizzas into a delivery for 4
    repeat until either fail 
"""

def should_stop_deliveries(deliveries_for_four, pizzas_used, teams_data, pizzas_data):
    if deliveries_for_four >= teams_data.get_number_of_teams_of_size(4):
        return True
    
    if pizzas_used + 4 > pizzas_data.get_total_pizzas():
        return True

    return False

def random_gen(teams_data, pizzas_data):
    # Init Output Data
    deliveries = []

    deliveries_for_four = 0
    pizzas_used = 0
    total_pizzas = pizzas_data.get_total_pizzas()
    pizza_ids_unused = [i for i in range(0, total_pizzas)]

    stop_deliveries = should_stop_deliveries(deliveries_for_four, pizzas_used, teams_data, pizzas_data)

    while(not stop_deliveries):
        pizzas_for_delivery = []

        for _ in range(0, 4):
            random_pizza_id = random.choice(pizza_ids_unused)  # Index out of Range 
            pizza_ids_unused.remove(random_pizza_id)
            pizzas_for_delivery.append(random_pizza_id)
        
        delivery = [4] + pizzas_for_delivery  # [4] is size of team to deliver to
        deliveries.append(delivery)

        # Update and Check if Stop Deliveries
        deliveries_for_four += 1
        pizzas_used += 4
        stop_deliveries = should_stop_deliveries(deliveries_for_four, pizzas_used, teams_data, pizzas_data)

    return deliveries
