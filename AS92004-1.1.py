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

def get_age():
    while True:
        try:
            age = int(input('Please enter your age: '))
            if age > 0:
                return age
            else:
                print('Age must be a positive number. Please try again.')
        except ValueError:
            print('Invalid input. Please enter a valid number for age.')

get_age()