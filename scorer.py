from globals import *

from pizzas import Pizzas
from teams import Teams

from deliveries import Deliveries
from deliveries_validator import Deliveries_Validator
from deliveries_scorer import Deliveries_Scorer


def main_scorer(input_file, score_file):
    pizzas_data = Pizzas(input_file)
    teams_data = Teams(input_file)
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


main()
