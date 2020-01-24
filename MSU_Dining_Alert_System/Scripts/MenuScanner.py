""" MENU SCANNER """

from lxml import html
import requests

from FoodItem import *


class MenuScanner:

    MILLER_URL = 'http://www.montana.edu/culinaryservices/residence_dining_commons/menu.php?proxy=MDH'
    RENDEZVOUS_URL = 'http://www.montana.edu/culinaryservices/residence_dining_commons/menu.php?proxy=RenDC'

    def __init__(self):
        self.millerMenu = None
        self.rendezvousMenu = None

    def loadMenus(self):
        page = requests.get(self.MILLER_URL)
        self.millerMenu = html.fromstring(page.content)
        page = requests.get(self.RENDEZVOUS_URL)
        self.rendezvousMenu = html.fromstring(page.content)

    # Scan for food on the menu containing the string <item>
    # Returns a list of results
    def scanMenus(self, item):
        return self.scanMenu(item, "Miller") + self.scanMenu(item, "Rendezvous")

    def scanMenu(self, item, location):
        query = '//*[contains(text(),"' + item + '")]'
        if location == "Miller":
            results = self.millerMenu.xpath(query)
        elif location == "Rendezvous":
            results = self.rendezvousMenu.xpath(query)

        if results == []:
            return []
        # Handle the results appropriately if there are more than one elements found
        if len(results) > 0:  # More than one result
            list = []
            for r in results:
                f = self.parseElement(r)
                f.setLocation(location)
                list.append(f)
            return list
        else:  # Just one result
            f = self.parseElement(results)
            f.setLocation(location)
            return [f]

    # Handle an element that has been found to have a food item
    def parseElement(self, element):
        # Identify full food item name
        name = element.text

        # Identify what meal the food is in
        meal = element.getparent().getparent().getparent().getchildren()[0].text

        # Identify where the food is (Mill vs. Vous)
        station = element.getparent().getparent().getparent().getparent().getparent().getchildren()[0].getchildren()[0].text

        return FoodItem(name, meal, station, None)




