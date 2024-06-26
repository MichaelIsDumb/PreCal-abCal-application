import math
epsilon = 0.000001

def given_function(x): #the given function
    return x**3 - 5*x + 6 #plug the function you want, can be anything

def prime_function(x): #finding the slope / derivative of the function
    global epsilon
    delta_x = 1
    current_slope = (given_function(x + delta_x) - given_function(x - delta_x))/(2*delta_x)
    while True:
        delta_x = delta_x / 10
        next_slope = (given_function(x + delta_x) - given_function(x - delta_x))/(2*delta_x)
        if abs(next_slope - current_slope) <= epsilon:
            break
        else:
            current_slope = next_slope
    
    return current_slope

def finding_zero(): #using the sequence: x1 = x0 - [f(x0)/f'(x0)]
    x_initial = float(int(input("Enter an x-value you like to start calculating: ")))
    x = x_initial
    count = 1
    print(f"{count}: x = {x:.8f}, y = {given_function(x):.8f}")
    x_next = x - given_function(x)/prime_function(x)
    while abs(x_next - x) >= epsilon:
        count += 1
        x = x_next
        x_next = x - given_function(x)/prime_function(x)
        print(f"{count}: x = {x:.8f}, y = {given_function(x):.8f}")
    
    return x_next

finding_zero()