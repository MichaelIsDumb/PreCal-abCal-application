import math

def info_obtain(): #obtain information of user's desired quadratic
    print("Enter the quadratic function in form of Ax^2 + Bx + C")
    x_square = int(input("What number would you choose for A: "))
    x_normal = int(input("What number would you choose for B: "))
    x_zero = int(input("What number would you choose for C: "))
    print("It will takes 2 seconds for the machine to process!")
    return [x_square, x_normal, x_zero]

def info_process(): #execute info_obtain() and print the function in an explicit form
    result = info_obtain() #calling info_obtain() function
    if "-" in str(result[0]):
        if "-" in str(result[1]):
            if "-" in str(result[2]):
                print("f(x) = " + str(result[0]) + "x^2 - " + str(abs(result[1])) + "x - " + str(abs(result[2])))
            else:
                print("f(x) = " + str(result[0]) + "x^2 - " + str(abs(result[1])) + "x + " + str(result[2]))
        else:
            if "-" in str(result[2]):
                print("f(x) = " + str(result[0]) + "x^2 + " + str(result[1]) + "x - " + str(abs(result[2])))
            else:
                print("f(x) = " + str(result[0]) + "x^2 + " + str(result[1]) + "x + " + str(result[2]))
    else:
        if "-" in str(result[1]):
            if "-" in str(result[2]):
                print("f(x) = " + str(result[0]) + "x^2 - " + str(abs(result[1])) + "x - " + str(abs(result[2])))
            else:
                print("f(x) = " + str(result[0]) + "x^2 - " + str(abs(result[1])) + "x + " + str(result[2]))
        else:
            if "-" in str(result[2]):
                print("f(x) = " + str(result[0]) + "x^2 + " + str(result[1]) + "x - " + str(abs(result[2])))
            else:
                print("f(x) = " + str(result[0]) + "x^2 + " + str(result[1]) + "x + " + str(result[2]))
    return result

def info_confirm(): #confirm if the function print seems ideal for the user or not
    confirm = input("This is your ideal equation! Enter (yes/no): ")
    confirm = confirm.lower()
    while confirm != 'yes':
        info_process()
        confirm = input("This is your ideal equation! Enter (yes/no): ")
        confirm = confirm.lower()
    print("We will try to solve for the roots of the equation!")
    print("It will take the machine 2 seconds to process!")

def finding_zero(): #finding zeroes from quadratic function
    finale = info_process() #calling info_process() function and obtain the values of returning variables
    info_confirm() #calling info_confirm() function to execute the order

    #organizing values obtained from the other function
    a = finale[0]
    b = finale[1]
    c = finale[2]
    discriminant = (b*b) - (4*a*c)
    vertex_formula = (-b/(2*a))
    
    if discriminant < 0:
        print("The solutions are imaginary numbers!")
        print("First solution: " + str(vertex_formula) + " + " + str(math.sqrt(abs(discriminant))) + "i")
        print("Second solution: " + str(vertex_formula) + " - " + str(math.sqrt(abs(discriminant))) + "i")
        print("Notice how these two solutions are a conjudgate pair!")
    elif discriminant == 0:
        print("There is only one solution!")
        print("The solution is: " + str(vertex_formula))
    else:
        print("There are two real solutions!")
        print("First solution: " + str(vertex_formula + math.sqrt(discriminant)))
        print("Second solution: " + str(vertex_formula - math.sqrt(discriminant)))
    return finale

def tangent_line(): #finding tangent line of a given x_value
    values = finding_zero()
    a = values[0]
    b = values[1]
    c = values[2]
    request_tangent = int(input("Satisfied? Now please choose any x value point for us to calculate its tangent line: x = "))
    number_of_times = int(input("For how many times do you wish to find the tangent lines for precision: "))
    delta_x = 1
    for i in range(number_of_times): #repeat the process for precision as epsilon becomes smaller by a power of 10^-1
        #data
        x_value = request_tangent #input written as x
        prime_x_value_positive = x_value + delta_x #input written as x + rate of change
        y_value = a*x_value*x_value + b*x_value + c #output written as f(x)
        
        #positive tangent approach
        prime_y_value_positive = a*prime_x_value_positive*prime_x_value_positive + b*prime_x_value_positive + c #output written as f'(x + rate of change)
        positive_slope_tangent = (prime_y_value_positive - y_value)/delta_x #(f'(x + rate of change) - f(x))/rate of change
        
        #negative tangent approach
        prime_x_value_negative = x_value - delta_x #input written as x - rate of change
        prime_y_value_negative = a*prime_x_value_negative*prime_x_value_negative + b*prime_x_value_negative + c #ouput written as f'(x - rate of change)
        negative_slope_tangent = (y_value - prime_y_value_negative)/delta_x #(f'(x - rate of change) - f(x))/rate of change
        
        #avgerage tangent calculation
        average = (positive_slope_tangent + negative_slope_tangent)/2
        intercept_value = y_value - (average*x_value) #finding b in y = mx + b
        print("The tangent line equation at which delta x equals " + str(delta_x) + " is: y = " + str(average) + "x + " + str(intercept_value))
        delta_x *= 0.1

tangent_line()