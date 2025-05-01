# ////////////////
# Script Name: AS92004-1.1.py
# ////////////////

# Start of the script

print('Welcome to the school holiday camp!')

print()

def get_name():
    while True:
        name = input('Please enter your name: ')
        if len(name) > 0:
            return name
        else:
            print('Name cannot be empty. Please try again.')
            print()

name = get_name()

print()

def get_age():
    while True:
        try:
            age = int(input(f'Hi {name}, how old are you? '))
            if age > 0:
                return age
            else:
                print('Age must be a positive number. Please try again.')
                print()
        except ValueError:
            print('Invalid input. Please enter a valid number for age.')
            print()


def validate_age(age):
    if age < 5:
        print('Sorry, you are too young to attend the camp.')
        exit()
    elif age > 18:
        print('Sorry, you are too old to attend the camp.')
        exit()
    else:
        return True

validate_age(get_age())

print()

def get_chosen_activity():

    activity_list = ['Cultural immersion. This is for 5 days and is considers "easy" and cost $800.','Kayaking and pancakes. This is for 3 days and is considered "moderate" and costs $400.','Mountain biking. This is for 4 days and is considered "difficult and cost $900.']
    
    print('Please choose an activity from the list below:')
    print()
    print(f'1. {activity_list[0]} ')
    print(f'2. {activity_list[1]} ')
    print(f'3. {activity_list[2]} ')


    while True:
        try:
            chosen_activity = int(input('Please enter the number corresponding to the activity you wish to particpate in : '))
            if chosen_activity in [1, 2, 3]:
                return chosen_activity
            else:
                print('Invalid choice. Please enter a number between 1 and 3.')
                print()
        except ValueError:
            print('Invalid input. Please enter a number corresponding to your chosen activity.')
            print()
            

chosen_activity = get_chosen_activity()