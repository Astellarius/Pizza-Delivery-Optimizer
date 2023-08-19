def get_delivery(delivery_size, available_pizzas: list):
    print("log: get_delivery()")
    print("Delivery Size: ", delivery_size)
    print("Available Pizzas: ", len(available_pizzas))

    pizza_ids = []

    for _ in range(0, delivery_size):
        pizza_id = available_pizzas[0]
        pizza_ids.append(pizza_id)
        available_pizzas.remove(pizza_id)

    # assemble 
    delivery = [] # Team Size, Pizza Id's 
    delivery.append(delivery_size)
    delivery += pizza_ids
    return delivery, available_pizzas


def basic(teams_data, pizzas_data):
    # Output
    deliveries = []

    # Internal Notes Unchangable
    total_pizzas = pizzas_data.get_total_pizzas()
    teams_size_4 = teams_data.get_number_of_teams_of_size(4)
    teams_size_3 = teams_data.get_number_of_teams_of_size(3)
    teams_size_2 = teams_data.get_number_of_teams_of_size(2)

    # Internal Notes Changable
    pizzas_used = 0
    team_2_served = 0
    team_3_served = 0
    team_4_served = 0 

    # Changable Variables for stuffs 
    available_pizzas = pizzas_data.get_pizza_ids()

    # More Delivery 
    no_more_delivery = False

    while(no_more_delivery == False):
        more_4_delivery = True
        more_3_delivery = True
        more_2_delivery = True
        
        if pizzas_used + 4 > total_pizzas or team_4_served >= teams_size_4:
            print("Log: You can't deliver to anymore teams of 4")
            more_4_delivery = False
        
        if pizzas_used + 3 > total_pizzas or team_3_served >= teams_size_3:
            print("Log: You can't deliver to anymore teams of 3")
            more_3_delivery = False

        if pizzas_used + 2 > total_pizzas or team_2_served >= teams_size_2:
            print("Log: You can't deliver to anymore teams of 2")
            more_2_delivery = False

        # Depending on Condition, Make Delivery
        if more_4_delivery:
            print("Lets make a 4 Delivery!")
            delivery, available_pizzas = get_delivery(4, available_pizzas)
            deliveries.append(delivery)

            pizzas_used += 4
            team_4_served += 1

        elif more_3_delivery:
            print("Lets make a 3 Delivery!")
            delivery, available_pizzas = get_delivery(3, available_pizzas)
            deliveries.append(delivery)

            pizzas_used += 3
            team_3_served += 1

        elif more_2_delivery:
            print("Lets make a 2 Delivery!")
            delivery, available_pizzas = get_delivery(2, available_pizzas)
            deliveries.append(delivery)

            pizzas_used += 2
            team_2_served += 1

        else:
            print("We cannot make any more deliveries!")
            no_more_delivery = True 

        # Update all values! 

    return deliveries
