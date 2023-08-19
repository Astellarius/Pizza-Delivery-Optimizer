""" Problems with Basic 

1. DeliveryPossibility
    The possibility to make a Delivery took up a large chunk of code. 
    This logic is not really specific to basic. 
    Should Separate these two. 

2. Floating Variables 
    There are many variables that need to be changed and moved around. 
    This will become challenging as later we will need more function helpers. 
    Create objects to contain data. 

"""
from teams import Teams 
from pizzas import Pizzas
from delivery_info import DeliveryInfo
from basic3 import basic


class MakeDeliveryChecker:
    def __init__(self, teams_data: Teams, pizzas_data: Pizzas):
        self.teams = teams_data
        self.pizzas = pizzas_data

        self.can_delivery = True 
        self.can_4_delivery = True 
        self.can_3_delivery = True 
        self.can_2_delivery = True 
    
    def can_make_4_delivery(self, info: DeliveryInfo):
        enough_pizzas = info.pizzas_assigned + 4 <= self.pizzas.get_total_pizzas()
        enough_4teams = info.team_4_served < self.teams.team_fours()
        return enough_pizzas and enough_4teams
    
    def can_make_3_delivery(self, info: DeliveryInfo):
        enough_pizzas = info.pizzas_assigned + 3 <= self.pizzas.get_total_pizzas()
        enough_3teams = info.team_3_served < self.teams.team_threes()
        return enough_pizzas and enough_3teams

    def can_make_2_delivery(self, info: DeliveryInfo):
        enough_pizzas = info.pizzas_assigned + 2 <= self.pizzas.get_total_pizzas()
        enough_2teams = info.team_2_served < self.teams.team_twos()
        return enough_pizzas and enough_2teams

    def can_make_delivery(self, info: DeliveryInfo):
        self.can_4_delivery = self.can_make_4_delivery(info)
        self.can_3_delivery = self.can_make_3_delivery(info)
        self.can_2_delivery = self.can_make_2_delivery(info)
        
        return self.can_4_delivery or self.can_3_delivery or self.can_2_delivery

    def make_delivery_size(self):
        if self.can_4_delivery: 
            return 4
        elif self.can_3_delivery:
            return 3
        elif self.can_2_delivery:
            return 2
        else:
            print("Log: Make Delivery Size: Delivery Not Possible, still tried to make delivery: Error")
            exit()


def one_at_a_time(teams_data, pizzas_data):
    deliveries = []
    
    delivery_info = DeliveryInfo(pizzas_data)
    make_delivery_checker = MakeDeliveryChecker(teams_data, pizzas_data)

    while(make_delivery_checker.can_make_delivery(delivery_info)):
        delivery_size = make_delivery_checker.make_delivery_size()

        """ Change Algorithms Here """
        delivery = basic(delivery_size, delivery_info)
        deliveries.append(delivery)

        # Make sure to update delivery_info!
        delivery_info.pizzas_assigned += delivery_size
        delivery_info.increase_team_served(delivery_size)

    return deliveries
    