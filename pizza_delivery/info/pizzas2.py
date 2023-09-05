from collections import defaultdict


class Pizzas:
    def __init__(self, input_data_file):
        self.total_pizzas: int = self._init_total_pizzas()
        # self.pizza_dict = dict()  # should it be dict or defaultdict
        self.pizza_toppings: defaultdict = self._init_pizza_toppings(input_data_file)  # should it be dict or defaultdict

    def _init_total_pizzas(self, input_data_file) -> int:
        file = open(input_data_file, "r")
        firstline = file.readline() # skip firstline



        # open file 
        # get first line 
        # get total pizzas 


    def convert_line_to_topping_int_list(self, pizza_file_line):
        return [0]

    def _init_pizza_toppings(self, input_data_file) -> defaultdict:
        file = open(input_data_file, "r")
        _ = file.readline() # skip firstline

        for line_index, line in enumerate(file):
            pizza_id = line_index
            topping_int_list = self.convert_line_to_topping_int_list(line)
            self.pizza_toppings[pizza_id] = topping_int_list

        # open file 
        # for line_index, line in enumerate(file): 
            # pizza_id = line_index
            # topping_int = convert_line_to_topping_int
            # pizza_toppings[pizza_id] = list[topping_int]


    def get_pizza_toppings(self, pizza_id) -> int:
        # return 0
        return self.pizza_toppings[pizza_id]
    
    # get_total_pizas is pizzas.total_pizzas 
    # get_pizza_toppings_keys_list is list(self.pizza_toppings.keys())
