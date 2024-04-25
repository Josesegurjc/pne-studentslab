import json
import termcolor
from pathlib import Path

# -- Read the json file
jsonstring = Path("people-e1.json").read_text()

# Create the object person from the json string
person = json.loads(jsonstring)
list_of_dicts = person["People"]

print("Total people in the database: " + str(len(list_of_dicts)))

# Print the information on the console, in colors
for e in list_of_dicts:
    print()
    termcolor.cprint("Name: ", 'green', end="")
    print(e['Firstname'], e['Lastname'])
    termcolor.cprint("Age: ", 'green', end="")
    print(e['age'])

    # Get the phoneNumber list
    phoneNumbers = e['phoneNumber']

    # Print the number of elements in the list
    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phoneNumbers))

    # Print all the numbers
    for i, dictnum in enumerate(phoneNumbers):
        termcolor.cprint("  Phone " + str(i + 1) + ": ", 'blue')

        # The element num contains 2 fields: number and type
        termcolor.cprint("\t- Type: ", 'red', end='')
        print(dictnum['type'])
        termcolor.cprint("\t- Number: ", 'red', end='')
        print(dictnum['number'])
