from info import pizzas 
from info import teams

from scorer.deliveries import Deliveries
from scorer.deliveries_validator import Deliveries_Validator
from scorer.deliveries_scorer import Deliveries_Scorer


FILE_A_IN = "inputs/a.in"
FILE_B_IN = "inputs/b.in"
FILE_C_IN = "inputs/c.in"
FILE_D_IN = "inputs/d.in"
FILE_E_IN = "inputs/e.in"

FILE_A_OUT = "outputs/a.txt"
FILE_B_OUT = "outputs/b.txt"
FILE_C_OUT = "outputs/c.txt"
FILE_D_OUT = "outputs/d.txt"
FILE_E_OUT = "outputs/e.txt"


def main_scorer(input_file, score_file):
    pizzas_data = pizzas.Pizzas(input_file)
    teams_data = teams.Teams(input_file)
    deliveries_data = Deliveries(score_file)

    # Validation 
    deliveries_validator = Deliveries_Validator(deliveries_data, teams_data)
    if deliveries_validator.is_deliveries_valid():
        # Scoring 
        deliveries_scorer = Deliveries_Scorer(deliveries_data, pizzas_data)
        deliveries_score = deliveries_scorer.calculate_score()
        print("Total Score of File ", input_file, " is: ", deliveries_score)

    else:
        print("Deliveries are Invalid")


def main():
    main_scorer(FILE_A_IN, FILE_A_OUT)
    main_scorer(FILE_B_IN, FILE_B_OUT)
    main_scorer(FILE_C_IN, FILE_C_OUT)
    main_scorer(FILE_D_IN, FILE_D_OUT)
    main_scorer(FILE_E_IN, FILE_E_OUT)


# main()
