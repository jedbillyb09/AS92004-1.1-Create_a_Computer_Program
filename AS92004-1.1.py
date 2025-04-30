# ////////////////
# Script Name: AS92004-1.1.py
# ////////////////\

# Start of the script

print('Welcome to the school holiday camo!')

def get_name():
    while True:
        name = input('Please enter your name: ')
        if len(name) > 0:
            return name
        else:
            print('Name cannot be empty. Please try again.')

get_name()

