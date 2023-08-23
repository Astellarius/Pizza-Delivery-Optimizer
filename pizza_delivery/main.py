from optimizer import optimizer_main 
from scorer import scorer_main

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

def main():
    optimizer_main.run_optimizer(FILE_A_IN, FILE_A_OUT)
    optimizer_main.run_optimizer(FILE_B_IN, FILE_B_OUT)
    optimizer_main.run_optimizer(FILE_C_IN, FILE_C_OUT)
    optimizer_main.run_optimizer(FILE_D_IN, FILE_D_OUT)
    # optimizer_main.run_optimizer(FILE_E_IN, FILE_E_OUT) # May take over 5 minutes.

    scorer_main.main_scorer(FILE_A_IN, FILE_A_OUT)
    scorer_main.main_scorer(FILE_B_IN, FILE_B_OUT)
    scorer_main.main_scorer(FILE_C_IN, FILE_C_OUT)
    scorer_main.main_scorer(FILE_D_IN, FILE_D_OUT)
    scorer_main.main_scorer(FILE_E_IN, FILE_E_OUT)


main()