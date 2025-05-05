# ////////////////
# Script Name: AS92004-1.1.py
# ////////////////

# Start of the script

# Lists
# 1. List of activities
activity_list = [
'Cultural immersion. This is for 5 days and is considered "easy" and costs $800.',
'Kayaking and pancakes. This is for 3 days and is considered "moderate" and costs $400.',
'Mountain biking. This is for 4 days and is considered "difficult" and costs $900.'
]
# 2. List of meal preferences
meal_list = ['Standard', 'Vegetarian', 'Vegan']

# Constants
# 1. Cost of the shuttle bus
shuttle_bus_cost = 80
# 2 minimum age for the camp
min_age = 5
# 3. maximum age for the camp
max_age = 18

print('Welcome to the holiday camp!')

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

def get_age(min_age, max_age):
    while True:
        try:
            age = int(input(f'Hi {name}, how old are you? '))
            if age < 5:
                print('Sorry, you are too young to attend the camp.')
                exit()
            elif age > 18:
                print('Sorry, you are too old to attend the camp.')
                exit()
            elif 5 <= age <= 18:
                return age
            else:
                print('Age must be a positive number. Please try again.')
                print()
        except ValueError:
            print('Invalid input. Please enter a valid number for age.')
            print()

age = get_age(min_age, max_age)


print()

def get_chosen_activity(activity_list):
    
    print('Please choose an activity from the list below:')
    print(f'1. {activity_list[0]}')
    print(f'2. {activity_list[1]}')
    print(f'3. {activity_list[2]}')

    print()

    while True:
        try:
            chosen_activity = int(input('Please enter the number corresponding to the activity you wish to participate in: '))
            if chosen_activity == 1:
                return 'Cultural immersion', 5, 'easy', 800
            elif chosen_activity == 2:
                return 'Kayaking and pancakes', 3, 'moderate', 400
            elif chosen_activity == 3:
                return 'Mountain biking', 4, 'difficult', 900
            else:
                print('Invalid choice. Please enter a number between 1 and 3.')
                print()
        except ValueError:
            print('Invalid input. Please enter a number corresponding to your chosen activity.')
            print()

# Call the function and unpack the returned values
activity, day_length, difficulty, cost = get_chosen_activity(activity_list)

def get_meal_preference(meal_list):

    print()
    print('Please choose a meal preference from the list below:')
    print(f'1. {meal_list[0]} ')
    print(f'2. {meal_list[1]} ')
    print(f'3. {meal_list[2]} ')
    print()

    while True:
        try:
            meal_preference = int(input('Please enter the number corresponding to your meal preference: '))
            if meal_preference == 1:
                meal_choice = 'Standard'
                return meal_choice
            elif meal_preference == 2:
                meal_choice = 'vegetarian'
                return meal_choice
            elif meal_preference == 3:
                meal_choice = 'vegan'
                return meal_choice
            else:
                print('Invalid choice. Please enter a number between 1 and 3.')
                print()
        except ValueError:
            print('Invalid input. Please enter a number corresponding to your meal preference.')
            print()

meal_choice = get_meal_preference()

print()

def get_shuttle_bus(shuttle_bus_cost):
    while True:
        shuttle_bus = input('Do you require a shuttle bus for $80? (yes/no) (y/n): ')
        if shuttle_bus.lower() in ['yes', 'y']:
            aditional_cost = + shuttle_bus_cost
            shuttle_bus = 'take'
            return aditional_cost, shuttle_bus
        elif shuttle_bus.lower() in ['no', 'n']:
            aditional_cost = 0
            shuttle_bus = 'not take'
            return aditional_cost, shuttle_bus
        else:
            print('Invalid input. Please enter "yes" or "no".')
            print()

aditional_cost, shuttle_bus = get_shuttle_bus()

final_cost = cost + aditional_cost


print()
print(f'Hello {name}, you are {age} years old. you are going to participate in {activity} which is {day_length} days long and is considered {difficulty} and costs ${cost}. Your meal preference is {meal_choice} and you have chosen to {shuttle_bus} the shuttle bus. Your total cost is ${final_cost}.')
print()

final = input(f'Would you like to confirm your booking at the cost of {final_cost}? (yes/no) (y/n)')
if final.lower() in ['yes', 'y']:
    print('Thank you')
else:
    print('Cancelled.')
    exit()

# End