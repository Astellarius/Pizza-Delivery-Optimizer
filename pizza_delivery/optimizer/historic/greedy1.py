from pizza_delivery.optimizer.delivery_info import DeliveryInfo
from pizza_delivery.pizzas import Pizzas


# Given DeliverySize (2-4) and Delivery Info
# return a delivery of pizza ids 
def greedy1(delivery_size, info: DeliveryInfo, pizza_info: Pizzas):
    pizza_ids = []

    unique_ingredients = set()
    for _ in range(0, delivery_size):
        most_new_ingredients_count = -1
        most_new_ingredients_pizza_id = -1

        # get best pizza id given pizza_id and unique_toppings_set
        # for pizza_id in info.available_pizzas:
        for pizza_id in info.available_pizzas2.keys():

            ingredients = pizza_info.get_pizza(pizza_id) # can be improved 
            if most_new_ingredients_count > len(ingredients):
                break

            this_pizza_ingredients = set(ingredients)
            set_difference = this_pizza_ingredients - unique_ingredients
            new_possible_ingredients_count = len(set_difference)

            if new_possible_ingredients_count > most_new_ingredients_count:
                most_new_ingredients_count = new_possible_ingredients_count
                most_new_ingredients_pizza_id = pizza_id

        # At this point in time, we have best pizza_id. 
        if most_new_ingredients_pizza_id == -1:
            print("Log: PANIC! See greedy1")
            exit()

        pizza_ids.append(most_new_ingredients_pizza_id)
        unique_ingredients.add(pizza_info.get_pizza(most_new_ingredients_pizza_id))
        # info.available_pizzas.remove(most_new_ingredients_pizza_id)
        del info.available_pizzas2[most_new_ingredients_pizza_id]

    # assemble 
    delivery = [] # Team Size, Pizza Id's 
    delivery.append(delivery_size)
    delivery += pizza_ids

    return delivery