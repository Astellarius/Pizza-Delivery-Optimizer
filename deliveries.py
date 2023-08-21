from pizzas import Pizzas
from teams import Teams
from globals import *


class Delivery: 
    def __init__(self, team_size: int, pizza_ids: list[int]):
        self.team_size: int = team_size
        self.pizza_ids: list[int] = pizza_ids


class Deliveries:
    def __init__(self, filepath: str):
        self.deliveries: list[Delivery] = []

        self._init_deliveries(filepath)

    def _init_deliveries(self, filepath: str):
        file = open(filepath, "r")
        _ = file.readline()  # Number of Pizza Deliveries : Redundant Info

        for line in file: 
            line = line.strip() # remove newline: "3 0 2 3\n" -> "3 0 2 3"
            line = line.split(" ") # get list spilt on space: "3 0 2 3" -> ["3", "0", "2", "3"]
            line = [int(x) for x in line] # convert list of strings to list of ints: ["3", "0", "2", "3"] -> [3, 0, 2, 3]

            # Separate team_size from pizza_id's 
            team_size = line[0] 
            pizza_ids = line[1:]
            delivery = Delivery(team_size, pizza_ids)

            self.deliveries.append(delivery)
