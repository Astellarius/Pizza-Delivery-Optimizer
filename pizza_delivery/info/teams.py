import copy


class Teams: 
    def __init__(self, input_file):
        self._total_teams = 0
        self._size_two_teams = 0
        self._size_three_teams = 0
        self._size_four_teams = 0

        self._init_teams(input_file)


    # Internal Methods 
    def _init_teams(self, input_file: str):
        file = open(input_file, "r")

        firstline = file.readline() 
        firstline = firstline.strip() # removes unnecessary spaces and newlines.
        firstline = firstline.split(" ") # string to list[str]
        firstline = [int(i) for i in firstline] # list[str] to list[int]
        
        _, self._size_two_teams, self._size_three_teams, self._size_four_teams = firstline
        self._total_teams = self._size_two_teams + self._size_three_teams + self._size_four_teams


    # External Methods 
    def get_total_teams(self):
        return copy.deepcopy(self._total_teams)

    def team_fours(self):
        return self._size_four_teams
    
    def team_threes(self):
        return self._size_three_teams
    
    def team_twos(self):
        return self._size_two_teams

    def get_number_of_teams_of_size(self, size):
        if(size == 2):
            return copy.deepcopy(self._size_two_teams)
        elif(size == 3):
            return copy.deepcopy(self._size_three_teams)
        elif(size == 4):
            return copy.deepcopy(self._size_four_teams)
        else:
            print("Sorry, This size team is invalid!")
            return 0
            
    def print_info(self):
        print("Total Teams: ", self._total_teams)
        print("Teams of Size 2: ", self._size_two_teams)
        print("Teams of Size 3: ", self._size_three_teams)
        print("Teams of Size 4: ", self._size_four_teams)
