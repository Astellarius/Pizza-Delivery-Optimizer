from optimizer import optimizer_main 
from validate import deliveries_validator
from score import deliveries_scorer


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


def run_validate_score(file_in, file_out):
    
    optimizer_main.run_optimizer(file_in, file_out)

    if deliveries_validator.validate_deliveries(file_in, file_out):
        print("File Validated")

        scorer = deliveries_scorer.Scorer(file_in, file_out)
        deliveries_score = scorer.score_deliveries()
        print("File Score: ", deliveries_score)

    else:
        print("File Not Validated")


def main():
    run_validate_score(FILE_A_IN, FILE_A_OUT)
    run_validate_score(FILE_B_IN, FILE_B_OUT)
    run_validate_score(FILE_C_IN, FILE_C_OUT)
    run_validate_score(FILE_D_IN, FILE_D_OUT)
    # run_validate_score(FILE_E_IN, FILE_E_OUT)


main()