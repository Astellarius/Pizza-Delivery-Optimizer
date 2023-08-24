class Outputter:
    """ The Outputter class writes the deliveries to a text file. """

    def __init__(self, deliveries, output_file):
        self.deliveries = deliveries
        self.output_file = output_file

    def output_deliveries(self):
        with open(self.output_file, "w") as file:
            file.write(str(len(self.deliveries)) + "\n")

            for delivery in self.deliveries:
                delivery_strings = [str(i) for i in delivery]  # Convert integers to strings 
                delivery_line = " ".join(delivery_strings)  # join them with a space
                file.write(delivery_line + "\n")  # Write the line to the file

        file.close()
