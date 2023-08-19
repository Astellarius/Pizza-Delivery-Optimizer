from pizzas import Pizzas

class DeliveryInfo:
    def __init__(self, pizzas_data: Pizzas):
        self.pizzas_assigned = 0
        self.available_pizzas = pizzas_data.get_pizza_ids()

        self.team_2_served = 0
        self.team_3_served = 0
        self.team_4_served = 0 
    
    def increase_team_served(self, team_size):
        if team_size == 4:
            self.team_4_served += 1

        elif team_size == 3:
            self.team_3_served += 1

        elif team_size == 2:
            self.team_2_served += 1
        
        else:
            print("Log: increase_team_served got team size other than 2,3,4")
            exit()