class House():
    def __init__(self, x, y, max_output):
        self.x = x
        self.y = y
        self.max_output = max_output
        
    def load_houses(house_file):
        """
        Load the position of the houses and their max output.
        """
        house_coordinatesX = {}
        house_coordinatesY = {}
        house_max_output = {}
        with open(house_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            for count, row in enumerate(reader):
                house_coordinatesX[count+1] = row['x']
                house_coordinatesY[count+1] = row['x']
                house_max_output[count+1] = row['maxoutput']

        return house_coordinatesX, house_coordinatesX, house_max_output
