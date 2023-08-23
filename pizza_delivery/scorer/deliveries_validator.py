""" Deliveries_Validator validates deliveries.

Description 
    What constitutes a valid deliveries is explained in docs/practice_round_2021.pdf file. 
    Validation
    - Check 1: Each pizza must be part of at most one order.
    - Check 2: For all N-person teams, either nobody or everybody recieves a pizza. 
    - Check 3: There are T_N (number of N-person teams) or less deliveries to teams of N people. 

Example
    deliveries_validator = Deliveries_Validator(my_deliveries, my_teams_data)
    if deliveries_validator.is_deliveries_valid: 
        ... 
"""

from scorer.deliveries import Deliveries, Delivery
from info.teams import Teams


class Deliveries_Validator:

    def __init__(self, deliveries_data: Deliveries, teams_data: Teams):
        self._deliveries: list[Delivery] = deliveries_data.deliveries
        self._teams_data: Teams = teams_data
        
    def is_deliveries_valid(self) -> bool:
        check_1_passed = self.check_1()
        check_2_passed = self.check_2()
        check_3_passed = self.check_3()

        return check_1_passed and check_2_passed and check_3_passed


    def check_1(self):
        """Check 1: Each pizza must be part of at most one order
        
            Time Complexity O(N)
            Space Complexity O(N) - Using Linked List Method, O(1) is possible. 
        """

        seen_pizza_ids = set()

        for delivery in self._deliveries:
            for pizza_id in delivery.pizza_ids:
                if pizza_id in seen_pizza_ids:
                    return False 
                else:
                    seen_pizza_ids

        return True 
    
    def check_2(self):
        """Check 2: For all N-person teams, either nobody or everybody recieves a pizza

            Time Complexity O(d) where d = Number of Delivery in Deliveries
            Space Complexity O(1)
        """

        for delivery in self._deliveries:
            if delivery.team_size != len(delivery.pizza_ids):
                return False

        return True

    def check_3(self):
        """Check 3: There are T_N (number of N-person teams) or less deliveries to teams of N people
        
            Time Complexity O(N)
            Space Complexity O(1)
        """
        teams_of_four = self._teams_data.team_fours()
        teams_of_three = self._teams_data.team_threes()
        teams_of_two = self._teams_data.team_twos()

        delivery_team_size_fours = 0
        delivery_team_size_threes = 0
        delivery_team_size_twos = 0

        for delivery in self._deliveries:
            if delivery.team_size == 4:
                delivery_team_size_fours += 1
            
            if delivery.team_size == 3:
                delivery_team_size_threes += 1
            
            if delivery.team_size == 2: 
                delivery_team_size_twos += 1
        
        return delivery_team_size_fours <= teams_of_four and delivery_team_size_threes <= teams_of_three and delivery_team_size_twos <= teams_of_two
