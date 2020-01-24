""" Dictionary Reader """
# Creates a dictionaries from input/settings files.
# Assumes files consist of name:value pairs, each on a newline with a colon separating name and value.

class DictReader:

    def readDict(self, file):
        # Init dictionary d
        d = {};
        # Open file
        f = open(file)
        lines = f.read().splitlines()
        # Populate dictionary with items
        for line in lines:
            # Split line on delimiter ':'
            info = line.split(':')
            # Place in the dictionary
            d[info[0]] = info[1];
        # Close file
        f.close()
        return d
