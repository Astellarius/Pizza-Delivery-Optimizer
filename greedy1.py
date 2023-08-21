from delivery_info import DeliveryInfo
from pizzas import Pizzas




# Given DeliverySize (2-4) and Delivery Info
# return a delivery of pizza ids 
def greedy1(delivery_size, info: DeliveryInfo, pizza_info: Pizzas):
    # print("Calculating Delivery!")
    pizza_ids = []

    unique_ingredients = set()
    for _ in range(0, delivery_size):
        most_new_ingredients_count = -1
        most_new_ingredients_pizza_id = -1

        for pizza_id in info.available_pizzas:
            ingredients = pizza_info.get_pizza(pizza_id)
            if most_new_ingredients_count > len(ingredients):
                break

            this_pizza_ingredients = set(pizza_info.get_pizza(pizza_id))
            set_difference = this_pizza_ingredients - unique_ingredients
            new_possible_ingredients_count = len(set_difference)

            if new_possible_ingredients_count > most_new_ingredients_count:
                most_new_ingredients_count = new_possible_ingredients_count
                most_new_ingredients_pizza_id = pizza_id

        # At this point in time, we have best pizza_id. 
        # add pizza to delivery 
        if most_new_ingredients_pizza_id == -1:
            print("Log: PANIC! See greedy1")
            exit()

        pizza_ids.append(most_new_ingredients_pizza_id)
        unique_ingredients.add(pizza_info.get_pizza(most_new_ingredients_pizza_id))
        info.available_pizzas.remove(most_new_ingredients_pizza_id)
        

    # assemble 
    delivery = [] # Team Size, Pizza Id's 
    delivery.append(delivery_size)
    delivery += pizza_ids

    return delivery