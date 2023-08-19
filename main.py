from globals import *
from teams import Teams 
from pizzas import Pizzas
from outputter import Outputter

# Algorithms 
from random_gen import random_gen
from basic import basic_greedy


def algorithm(input_file, output_file):
    # Process Inputs 
    teams_data = Teams(input_file)
    pizzas_data = Pizzas(input_file)

    """ CHOOSE YOUR ALGORITHM HERE """
    deliveries = basic_greedy(teams_data, pizzas_data)
    print("log: deliveries", deliveries)

    # Output Deliveries
    output_deliveries = Outputter(deliveries, output_file)

def main():
    # algorithm(FILE_A_IN, FILE_A_OUT)
    # algorithm(FILE_B_IN, FILE_B_OUT)
    # algorithm(FILE_C_IN, FILE_C_OUT)
    # algorithm(FILE_D_IN, FILE_D_OUT)
    algorithm(FILE_E_IN, FILE_E_OUT)

main()