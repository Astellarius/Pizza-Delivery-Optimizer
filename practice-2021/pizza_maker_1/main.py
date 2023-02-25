from collections import namedtuple
# from dataclasses import dataclass
from collections import defaultdict
import copy

print("Let's make some pizza!")

FILENAME = "/home/andyw/linux_andyw/hashcode2/practice-2021/inputs/a.in"

class Pizzaria: 
    def __init__(self, filename):
        # orders 
        self._pizza_quantity = 0
        self._orders_for_2 = 0
        self._orders_for_3 = 0
        self._orders_for_4 = 0

        # pizzas 
        self._pizzas = defaultdict()

        # init attributes 
        self._set_orders(filename)
        self._set_pizzas(filename)

    def get_pizza_quantity(self) -> int:
        return copy.deepcopy(self._pizza_quantity)

    def get_orders_for_2(self) -> int:
        return copy.deepcopy(self._orders_for_2)

    def get_orders_for_3(self) -> int:
        return copy.deepcopy(self._orders_for_3)
    
    def get_orders_for_4(self) -> int:
        return copy.deepcopy(self._orders_for_4)
    
    def get_pizza(self, pizza_id: int) -> tuple:
        return self._pizzas[pizza_id] # should be tuple - which is immutable.

    def _set_orders(self, filename: str):
        file = open(filename, "r")

        firstline = file.readline() 
        firstline = firstline.strip() # removes unnecessary spaces and newlines.
        firstline = firstline.split(" ") # string to list[str]
        # firstline = firstline[:-1] # remove \n
        firstline = [int(i) for i in firstline] # list[str] to list[int]
        self._pizza_quantity, self._orders_for_2, self._orders_for_3, self._orders_for_4 = firstline

    def _set_pizzas(self, filename: str):
        file = open(filename, "r")
        _ = file.readline() # skip firstline - processed by _set_pizzaria_orders()

        for pizza_id, line in enumerate(file): 
            line = line.strip() # remove newline: "3 onion pepper olive\n" -> "3 onion pepper olive"
            line = line.split(" ") # get list spilt on space: "3 onion pepper olive" -> ["3", "onion", "pepper", "olive"]
            line = line[1:] # remove first element of list: number of ingredients not needed
            pizza_toppings = tuple(line) # make ingredients tuple so it can't be modified
            self._pizzas[pizza_id] = pizza_toppings


def print_pizzaria(pizzaria: Pizzaria):
    print(pizzaria.get_pizza_quantity())
    print(pizzaria.get_orders_for_2())
    print(pizzaria.get_orders_for_3())
    print(pizzaria.get_orders_for_4())

    for pizza_id in range(0, pizzaria.get_pizza_quantity()):
        print(pizzaria.get_pizza(pizza_id))

def main():
    my_pizzaria = Pizzaria(FILENAME)

    print_pizzaria(my_pizzaria)


main()
# each pizza must be pa of at most one order,
# for all N-person teams, either nobody or everybody receives a pizza,
# there are TN or less deliveries to teams of N people.

# score
# the delivery score is the square of the total number of different ingredients of all the pizzas in the delivery. 
# The total score is the sum of the scores for all deliveries.


