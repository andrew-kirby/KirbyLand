""" MSU DINING ALERT CONTROLLER """
# Main class for the MSU Dining Alert System. Coordinates scanning the menus and sending the emails.

# Imports
import os

# Import from local scripts
from DictReader import *
from MenuScanner import *
from AlertEmailer import *

if __name__ == "__main__":

    # DEBUG_MODE = "ON"
    DEBUG_MODE = "OFF"

    # Initialize a dictionary reader
    dictReader = DictReader()

    # Load settings file
    settings = dictReader.readDict("../settings")
    print('SETTINGS:')
    print(settings)

    DEBUG_MODE = settings['debug_mode']

    # Load members
    if DEBUG_MODE == "off":
        members = os.listdir('../Members')
        for m in range(len(members)):
            members[m] = dictReader.readDict("../Members/" + members[m])
    elif DEBUG_MODE == "on":
        members = [dictReader.readDict("../Members/" + 'test')]

    # Scan the menu
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
            if settings['email_enabled'] == 'true':
                emailer.emailAlert(m, found_food)

    print("Scanning done! :)")
