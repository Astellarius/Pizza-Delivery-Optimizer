from pizzas import Pizzas
from teams import Teams
from globals import *
from deliveries import *


def main_scorer(input_file, score_file):
    pizzas_data = Pizzas(input_file)
    teams_data = Teams(input_file)
    deliveries_data = Deliveries(score_file)

    # Validation 
    deliveries_validator = Deliveries_Validator(deliveries_data, teams_data)

    # Scoring 
    scorer = Deliveries_Scorer(deliveries_data, pizzas_data)
    print("Total Score of File ", input_file, " is: ", scorer.total_score)


def main():
    main_scorer(FILE_A_IN, FILE_A_OUT)
    main_scorer(FILE_B_IN, FILE_B_OUT)
    main_scorer(FILE_C_IN, FILE_C_OUT)
    main_scorer(FILE_D_IN, FILE_D_OUT)
    main_scorer(FILE_E_IN, FILE_E_OUT)  # Takes too Long

main()
