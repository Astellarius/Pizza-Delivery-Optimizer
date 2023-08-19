# find the maximum number of ingredients per file 

from globals import *
from teams import Teams 
from pizzas import Pizzas
from outputter import Outputter

# Algorithms 
from random_gen import random_gen


def algorithm(input_file, output_file):
    # Process Inputs 
    teams_data = Teams(input_file)
    pizzas_data = Pizzas(input_file)

    max_ingredients = 0

    for key in pizzas_data._pizzas:
        value = pizzas_data._pizzas[key]
        if len(value) >= max_ingredients:
            max_ingredients = len(value)
    
    print("Max Ingredients: ", max_ingredients)


def main():
    algorithm(FILE_A_IN, FILE_A_OUT)
    algorithm(FILE_B_IN, FILE_B_OUT)
    algorithm(FILE_C_IN, FILE_C_OUT)
    algorithm(FILE_D_IN, FILE_D_OUT)
    algorithm(FILE_E_IN, FILE_E_OUT)

main()