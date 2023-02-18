from collections import namedtuple
from dataclasses import dataclass

print("Let's make some pizza!")

# inputs 

file = open("/home/andyw/linux_andyw/hashcode2/practice-2021/inputs/a_example.in", "r")

firstline = file.readline() 
firstline = firstline.split(" ") # string to list[str]
firstline = firstline[:-1] # remove \n
pizzaria_info = [int(i) for i in firstline] # list[str] to list[int]

Pizzaria = namedtuple("BakeryInfo", "pizzas_available twp_person_teams three_person_teams four_person_teams")
pizzaria = Pizzaria(pizzaria_info[0], pizzaria_info[1], pizzaria_info[2], pizzaria_info[3])

@dataclass
class PizzariaInfo: 
    pizza_quantity: int = ""
    orders_for_2: int = ""
    orders_for_3: int = ""
    orders_for_4: int = ""
    pizza_dict: dict = {}



def get_pizzariaInfo(filename: str) -> PizzariaInfo:
    pizzaria_info = PizzariaInfo()

    firstline = file.readline() 
    firstline = firstline.split(" ") # string to list[str]
    firstline = firstline[:-1] # remove \n
    firstline = [int(i) for i in firstline] # list[str] to list[int]

    pizzaria_info.pizza_quantity, pizzaria_info.orders_for_2, pizzaria_info.orders_for_3, pizzaria_info.orders_for_4 = firstline


pizzas = []

for line in file:
    line = line.split(" ")
    line = line[:-1]
    line[0] = int(line[0])
    pizzas.append(line)

print(pizzas)

# inputs are done

# outputs 

# first line - num of pizzas to deliver
    # 1 <= n <= t2 + t3 + t4
# teamsize pizza_id ...

# each pizza must be pa of at most one order,
# for all N-person teams, either nobody or everybody receives a pizza,
# there are TN or less deliveries to teams of N people.

# score
# the delivery score is the square of the total number of different ingredients of all the pizzas in the delivery. 
# The total score is the sum of the scores for all deliveries.


