from collections import defaultdict


class Pizzas: 
    def __init__(self, filename):
        self._pizzas = defaultdict()
        self._toppings_dict = dict()
        self._topping_counter = 0

        self._set_pizzas(filename)

    def number_of_pizzas(self):
        return len(self._pizzas)

    # Internal Methods 
    def _set_pizzas2(self, filename: str):
        file = open(filename, "r")
        _ = file.readline() # skip firstline - processed by _set_pizzaria_orders()

        for pizza_id, line in enumerate(file): 
            line = line.strip() # remove newline: "3 onion pepper olive\n" -> "3 onion pepper olive"
            line = line.split(" ") # get list spilt on space: "3 onion pepper olive" -> ["3", "onion", "pepper", "olive"]
            line = line[1:] # remove first element of list: number of ingredients not needed
            pizza_toppings = tuple(line) # make ingredients tuple so it can't be modified
            self._pizzas[pizza_id] = pizza_toppings

    def convert_toppings_str_to_int(self, topping_string: str) -> int:
        if topping_string not in self._toppings_dict:
            self._toppings_dict[topping_string] = self._topping_counter
            self._topping_counter += 1
        
        return self._toppings_dict[topping_string]
        
    def _set_pizzas(self, filename: str):
        file = open(filename, "r")
        _ = file.readline() # skip firstline - processed by _set_pizzaria_orders()

        for pizza_id, line in enumerate(file): 
            line = line.strip() # remove newline: "3 onion pepper olive\n" -> "3 onion pepper olive"
            line = line.split(" ") # get list spilt on space: "3 onion pepper olive" -> ["3", "onion", "pepper", "olive"]
            line = line[1:] # remove first element of list: number of ingredients not needed
            pizza_toppings = tuple(line) # make ingredients tuple so it can't be modified

            pizza_toppings_ints = []
            for pizza_topping_str in pizza_toppings:
                pizza_topping_int = self.convert_toppings_str_to_int(pizza_topping_str)
                pizza_toppings_ints.append(pizza_topping_int)

            self._pizzas[pizza_id] = tuple(pizza_toppings_ints)

    # External Methods 
    def get_total_pizzas(self) -> int:
        return len(self._pizzas)
    
    def get_pizza(self, pizza_id: int) -> tuple:
        return self._pizzas[pizza_id] # should be tuple - which is immutable.

    def get_pizza_ids(self) -> list[int]:
        return list(self._pizzas.keys())
