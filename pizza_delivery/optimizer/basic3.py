from pizza_delivery.optimizer.delivery_info import DeliveryInfo

def basic(delivery_size, info: DeliveryInfo):
    pizza_ids = []

    for _ in range(0, delivery_size):
        pizza_id = info.available_pizzas[0]
        pizza_ids.append(pizza_id)
        info.available_pizzas.remove(pizza_id)

    # assemble 
    delivery = [] # Team Size, Pizza Id's 
    delivery.append(delivery_size)
    delivery += pizza_ids

    return delivery