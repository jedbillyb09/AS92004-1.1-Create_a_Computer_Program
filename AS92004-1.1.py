# ////////////////
# Script Name: AS92004-1.1.py
# ////////////////

# Lists
activity_list = [
'Cultural immersion. This is for 5 days and is considered "easy" and costs $800.',
'Kayaking and pancakes. This is for 3 days and is considered "moderate" and costs $400.',
'Mountain biking. This is for 4 days and is considered "difficult" and costs $900.']

meal_list = ['Vegan', 'Vegetarian', 'Standerd']

# Constants

shuttle_bus_cost = 80

min_age = 5

max_age = 17

# /////////////////
# Start of the script
# /////////////////

# Welcome message
print('Welcome to the holiday camp!')

# Blank Line 
print()

# Subroutine gathering camper name
def def_camper_name():
    while True:
        camper_name = input('Please enter your name: ')
        if len(camper_name) > 0:
            return camper_name
        else:
            print('Name cannot be empty. Please try again.')
            print()

# Call the function to get camper name
camper_name = def_camper_name()

# Blank Line
print()

# Subroutine gathering camper age
def def_camper_age(min_age, max_age):
    while True:
        try:
            camper_age = int(input(f'Hi {camper_name}, how old are you? '))
            if camper_age < min_age:
                print('Sorry, you are too young to attend the camp.')
                exit()
            elif camper_age > max_age:
                print('Sorry, you are too old to attend the camp.')
                exit()
            elif min_age <= camper_age <= max_age:
                if camper_age >= 15:
                    print('You hava a chance to be a camp leader!')
                    print()
                elif camper_age <= 15:
                    print('You are too old to be a campe leader!')
                    print()
                return camper_age   
            else:
                print('Age must be a positive number. Please try again.')
                print()
        except ValueError:
            print('Invalid input. Please enter a valid number for age.')
            print()

# Call the function to get camper age
camper_age = def_camper_age(min_age, max_age)

# Blank Line
print()

# Subroutine gathering camper activity choice
def def_activity_choice(activity_list):
    
    print('Please choose an activity from the list below:')
    print(f'1. {activity_list[0]}')
    print(f'2. {activity_list[1]}')
    print(f'3. {activity_list[2]}')

    print()

    while True:
        try:
            activity_choice = int(input('Please enter the number corresponding to the activity you wish to participate in: '))
            if activity_choice == 1:
                return 'Cultural immersion', 5, 'easy', 800
            elif activity_choice == 2:
                return 'Kayaking and pancakes', 3, 'moderate', 400
            elif activity_choice == 3:
                return 'Mountain biking', 4, 'difficult', 900
            else:
                print('Invalid choice. Please enter a number between 1 and 3.')
                print()
        except ValueError:
            print('Invalid input. Please enter a number corresponding to your chosen activity.')
            print()

# Call the function to get camper activity choice
chosen_activity, day_length, difficulty, cost = def_activity_choice(activity_list)

# Subroutine gathering meal preference
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

# Call the function to get camper meal preference
meal_choice = get_meal_preference(meal_list)

# Blank Line
print()

# Subroutine gathering shuttle bus choice
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

# Call the function to get camper shuttle bus choice
aditional_cost, shuttle_bus = get_shuttle_bus(shuttle_bus_cost)

# Final cost calculation
final_cost = cost + aditional_cost

# Blank Line
print()

# Final output
print(f'Hello {camper_name}, you are {camper_age} years old. you are going to participate in {chosen_activity} which is {day_length} days long and is considered {difficulty} and costs ${cost}. Your meal preference is {meal_choice} and you have chosen to {shuttle_bus} the shuttle bus. Your total cost is ${final_cost}.')

# Blank Line
print()

# Subroutine gathering final cost confirmation
def final_cost_input(final_cost):
    while True:
        final = input(f'Would you like to confirm your booking at the cost of {final_cost}? (yes/no) (y/n): ')
        if final.lower() in ['yes', 'y']:
            print('Thank you for confirming your booking!')
            return
        elif final.lower() in ['no', 'n']:
            print('Booking cancelled.')
            exit()
        else:
            print('Invalid input. Please enter "yes" or "no".')
            print()

# Call the function to get camper final cost confirmation
final_cost_input(final_cost)

# End of the script