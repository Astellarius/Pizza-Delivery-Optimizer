from optimizer.delivery_info import DeliveryInfo
from info.pizzas import Pizzas


# Given DeliverySize (2-4) and Delivery Info
# return a delivery of pizza ids 
def greedy2(delivery_size, info: DeliveryInfo, pizza_info: Pizzas):
    pizza_ids = []

    unique_ingredients = set()
    for _ in range(0, delivery_size):
        most_new_ingredients_count = -1
        most_new_ingredients_pizza_id = -1

        mnip_topping_count = 1000000  # we want the lowest number. 


        # get best pizza id given pizza_id and unique_toppings_set
        for pizza_id in info.available_pizzas:
            # print(mnip_topping_count)
            ingredients = pizza_info.get_pizza(pizza_id) # can be improved 
            
            if most_new_ingredients_count > len(ingredients):
                # print(most_new_ingredients_count, len(ingredients))
                break

            this_pizza_ingredients = set(ingredients)
            set_difference = this_pizza_ingredients - unique_ingredients

            new_possible_ingredients_count = len(set_difference)

            this_topping_count = len(this_pizza_ingredients)
            #print(this_topping_count)

            if new_possible_ingredients_count > most_new_ingredients_count:
                most_new_ingredients_count = new_possible_ingredients_count
                most_new_ingredients_pizza_id = pizza_id
                mnip_topping_count = this_topping_count

            elif new_possible_ingredients_count == most_new_ingredients_count:
                #print("what the ffff")
                # new_topping_count = this_topping_count
                #print(new_topping_count, mnip_topping_count)
                if this_topping_count < mnip_topping_count:
                    most_new_ingredients_count = new_possible_ingredients_count
                    most_new_ingredients_pizza_id = pizza_id
                    mnip_topping_count = this_topping_count

        # At this point in time, we have best pizza_id. 
        if most_new_ingredients_pizza_id == -1:
            print("Log: PANIC! See greedy1")
            exit()

        pizza_ids.append(most_new_ingredients_pizza_id)
        
        unique_ingredients = unique_ingredients.union(set(pizza_info.get_pizza(most_new_ingredients_pizza_id)))
        # del info.available_pizzas2[most_new_ingredients_pizza_id]
        info.available_pizzas.remove(most_new_ingredients_pizza_id)

    # assemble 
    delivery = [] # Team Size, Pizza Id's 
    delivery.append(delivery_size)
    delivery += pizza_ids

    return delivery
