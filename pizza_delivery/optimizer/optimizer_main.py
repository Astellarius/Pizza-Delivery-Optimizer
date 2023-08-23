from info.teams import Teams 
from info.pizzas import Pizzas
from optimizer.outputter import Outputter

# Algorithms 
from optimizer.one_at_a_time_algs import one_at_a_time





def run_optimizer(input_file, output_file):
    # Process Inputs 
    teams_data = Teams(input_file)
    pizzas_data = Pizzas(input_file)

    """ CHOOSE YOUR ALGORITHM HERE """
    deliveries = one_at_a_time(teams_data, pizzas_data)

    # Output Deliveries
    output_deliveries = Outputter(deliveries, output_file)
    output_deliveries.output_deliveries()
    print("Done")

def run_optimizers():
    run_optimizer(FILE_A_IN, FILE_A_OUT)
    run_optimizer(FILE_B_IN, FILE_B_OUT)
    run_optimizer(FILE_C_IN, FILE_C_OUT)
    run_optimizer(FILE_D_IN, FILE_D_OUT)
    # run_optimizer(FILE_E_IN, FILE_E_OUT)


# main()