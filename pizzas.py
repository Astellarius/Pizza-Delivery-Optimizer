from collections import defaultdict
from globals import *

class Pizzas: 
    def __init__(self, filename):
        self._pizzas = defaultdict()

        self._set_pizzas(filename)


    # Internal Methods 
    def _set_pizzas(self, filename: str):
        file = open(filename, "r")
        _ = file.readline() # skip firstline - processed by _set_pizzaria_orders()

        for pizza_id, line in enumerate(file): 
            line = line.strip() # remove newline: "3 onion pepper olive\n" -> "3 onion pepper olive"
            line = line.split(" ") # get list spilt on space: "3 onion pepper olive" -> ["3", "onion", "pepper", "olive"]
            line = line[1:] # remove first element of list: number of ingredients not needed
            pizza_toppings = tuple(line) # make ingredients tuple so it can't be modified
            self._pizzas[pizza_id] = pizza_toppings


    # External Methods 
    def get_total_pizzas(self) -> int:
        return len(self._pizzas)
    
    def get_pizza(self, pizza_id: int) -> tuple:
        return self._pizzas[pizza_id] # should be tuple - which is immutable.

    def get_pizza_ids(self) -> list[int]:
        return list(self._pizzas.keys())
