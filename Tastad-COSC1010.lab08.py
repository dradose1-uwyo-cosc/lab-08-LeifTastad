# Leif Tastad
# UWYO COSC 1010
# Submission Date: 11/7/2024
# Lab 08
# Lab Section: 13

# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def conversion(value):
    if value.lstrip('-').isdigit():
        return int(value)
    if value.count('.') == 1:
        values = value.split('.')
        value_intergral = values[0]
        value_fractional = values[1]
        if value_intergral.lstrip('-').isdigit() and value_fractional.isdigit():
            return float(value)
    return False

while True:
    value_input = input("Please enter a value to check if it's an integer or a float. To quit type exit: ")
    result = conversion(value_input)

    if result is not False:
        print("Converted value:", result)
    elif value_input.upper() == 'EXIT':
        break
    else:
        print("This input can not be converted to an integer or a float, please try again.")

print("*" * 75)

# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def point_slope_intercept(m, b, lower_x, upper_x):
    if lower_x > upper_x:
        return False
    y_values = [(m * x + b) for x in range(lower_x, upper_x + 1)]
    return y_values

while True:
    slope_input = input("Enter the slope/the m value of the line or enter exit to quit: ")
    if slope_input.upper() == 'EXIT':
        break
    y_intercept_input = input("Enter the y-intercept/the b value value of the line or enter exit to quit: ")
    if y_intercept_input.upper() == 'EXIT':
        break
    lower_x_input = input("Enter an integer for the lower x bound of the line or enter exit to quit: ")
    if lower_x_input.upper() == 'EXIT':
        break
    upper_x_input = input("Enter an integer for the upper x bound of the line or enter exit to quit: ")
    if upper_x_input.upper() == 'EXIT':
        break
    
    if (slope_input.lstrip('-').replace('.', '', 1).isdigit() and 
        y_intercept_input.lstrip('-').replace('.', '', 1).isdigit() and 
        lower_x_input.lstrip('-').replace('.', '', 1).isdigit() and 
        upper_x_input.lstrip('-').replace('.', '', 1).isdigit()):
        m = float(slope_input)
        b = float(y_intercept_input)
        lower_x = int(lower_x_input)
        upper_x = int(upper_x_input)
    else:
        print("Invalid input. Make sure m and b are numbers and the lower and upper x bounds are integers")
        continue
    
    result = point_slope_intercept(m, b, lower_x, upper_x)
    if result is not False:
        print(f"The y values of the given range: {result}")
    else:
        print("Invalid bounds. Please ensure the lower x value is not greater then the upper x value.")

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

def negative_sqrt_check(value):
    if value < 0:
        return None
    return value ** 0.5

def quadratic_formula(a, b, c):
    discriminant = (b ** 2) - (4 * a * c)
    sqrt_discriminant = negative_sqrt_check(discriminant)
    if sqrt_discriminant is None:
        return None, None
    solution_1 = ((-b + sqrt_discriminant) / (2 * a))
    solution_2 = ((-b - sqrt_discriminant) / (2 * a))
    return solution_1, solution_2

while True:
    a_input = input("Enter a value for a or type exit to quit: ")
    if a_input.upper() == 'EXIT':
        break
    b_input = input("Enter a value for b or type exit to quit: ")
    if b_input.upper() == 'EXIT':
        break
    c_input = input("Enter a value for c or type exit to quit: ")
    if c_input.upper() == 'EXIT':
        break

    if (a_input.lstrip('-').replace('.', '', 1).isdigit() and 
        b_input.lstrip('-').replace('.', '', 1).isdigit() and 
        c_input.lstrip('-').replace('.', '', 1).isdigit()):
        a = float(a_input)
        b = float(b_input)
        c = float(c_input)
        if a == 0:
            print("a can not have the value of 0 in a quadratic equation, please enter a different number for a")
            continue
        soltion_1_input, solution_2_input = quadratic_formula(a, b, c)
        if soltion_1_input is None:
            print("The equation is invalid as there is a negative value in the square root")
        else:
            print(f"The solutions to this quadtratic forumla are x = {soltion_1_input}, {solution_2_input}.")
    else:
        print("Please enter numerical values and try again")
        continue