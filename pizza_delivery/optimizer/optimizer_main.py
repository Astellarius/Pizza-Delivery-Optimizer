from info.teams import Teams 
from info.pizzas import Pizzas
from optimizer.outputter import Outputter

# Algorithms 
from optimizer.one_at_a_time_algs import one_at_a_time


def run_optimizer(input_file, output_file):
    """ Given a problem input file, produces an output file with a deliveries solution. """

    # Process Inputs 
    teams_data = Teams(input_file)
    pizzas_data = Pizzas(input_file)

    """ CHOOSE YOUR ALGORITHM HERE """
    deliveries = one_at_a_time(teams_data, pizzas_data)

    # Output Deliveries
    output_deliveries = Outputter(deliveries, output_file)
    output_deliveries.output_deliveries()
    print("Done")
