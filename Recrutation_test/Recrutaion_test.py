# Importing json package
import json

# Creating Netflix class; loading data file
class Netflix:
    def __init__ (self, filename):
        self.filename = filename
        with open(filename, "rt") as file:
            self.rate_list = json.load(file)
    def picking_good(self):
        bad_rating = 3
        self.rate_list = [x for x in self.rate_list if x[2]>bad_rating]
    def picking_fav(self):
        user = 'Dennis'
        self.rate_list = [x for x in self.rate_list if x[0]==user]


# Testing file loading
netflix = Netflix("moviedata.json")
netflix.picking_good()
netflix.picking_fav()
print(netflix.rate_list)
