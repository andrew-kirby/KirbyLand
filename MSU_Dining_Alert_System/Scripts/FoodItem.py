
# A class that contains food items

class FoodItem:

    def __init__(self, name, meal, station, location):
        self.name = name
        self.meal = meal
        self.station = station
        self.location = location

    def setLocation(self, location):
        self.location = location

    def getAlertText(self):
        return "" + self.name + " may be found in " + self.location + " (" + self.station + ") during " + self.meal + "!!!"
