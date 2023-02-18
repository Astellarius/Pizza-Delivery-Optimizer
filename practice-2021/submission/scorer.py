def get_deliveries(filepath: str) -> list:
    file = open(filepath, "r")

    firstline = file.readline()
    print(firstline)

    deliveries = []

    for line in file:
        line = line.split(" ") # string to list[str]
        line = [int(i) for i in line] # list[str] to list[int]
        deliveries.append(line) 

    return deliveries

def scorer(filepath: str):
    deliveries = get_deliveries(filepath)

    # assume that the file has no errors

    # needs pizza id -> ingredients 
    