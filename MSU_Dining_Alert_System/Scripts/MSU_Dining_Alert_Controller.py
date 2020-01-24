""" MSU DINING ALERT CONTROLLER """
# Does stuff

# Imports
import time
import os

# Import from local scripts
from DictReader import *
from MenuScanner import *
from AlertEmailer import *

if __name__ == "__main__":

    DEBUG_MODE = "ON"
    # DEBUG_MODE = "OFF"

    # Initialize a dictionary reader
    dictReader = DictReader()

    # Load settings file
    settings = dictReader.readDict("../settings")
    print('SETTINGS:')
    print(settings)
    print('\n')

    # Load members
    if DEBUG_MODE == "OFF":
        members = os.listdir('../Members')
        for m in range(len(members)):
            members[m] = dictReader.readDict("../Members/" + members[m])
    elif DEBUG_MODE == "ON":
        members = [dictReader.readDict("../Members/" + 'andy')]

    # Scan the menu periodically
    while(True):
        print("Scanning...")

        # Initialize the menu scanner
        scanner = MenuScanner()
        scanner.loadMenus() # Load the menus!

        # Initialize the emailer
        emailer = AlertEmailer()
        emailer.loadCredentials()

        # For each user, make a list of tracked items and scan for them
        for m in members:
            items = m['alert_items'].split(',')
            found_food = []
            for item in items: # Search for each item, appending to a list of found items
                found_food = found_food + scanner.scanMenus(item)

            # Generate and send report to user based on found items
            if len(found_food) > 0:
                print(found_food)
                emailer.emailAlert(m, found_food)


        #time.sleep(settings['scan_interval'] * 60)
        time.sleep(200)