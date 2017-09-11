import math
import sys
print("*" * 51)
print("Pick Your calc mode -- type (normal=n/scientific=s)")
print("*" * 51)
which_calc = input()

if which_calc == "n":
    class Normal_calc:
        print("=" * 27)
        print("Welcome to your Normal calc ")
        print("=" * 27)
        # Initiated the function with two variable for calculating the user input

        def __init__(self, integer_1, integer_2):
            self.integer_1 = integer_1
            self.integer_2 = integer_2
        # Wrote a function for all basic operators

        def add(self):
            return self.integer_1 + self.integer_2

        def sub(self):
            return self.integer_1 - self.integer_2

        def mul(self):
            return self.integer_1 * self.integer_2

        def div(self):
            return self.integer_1 / self.integer_2

        def percentage(self):
            return self.integer_1 / self.integer_2 * 100

    list_of_normal_calc_function = "You can do addition, subtraction, multiplication, division, Percentage in this calc"
    print(list_of_normal_calc_function)
    print("*" * 83)

    # this is where we are getting input from user
    user_integer_1 = int(input("Enter the first number:--"))
    user_integer_2 = int(input("Enter the second number:-"))
    # Created instance for class
    chirpy_normal_calc = Normal_calc(integer_1=user_integer_1, integer_2=user_integer_2)

    # Displayed the operations for what to do with user input
    print("0. Exit")
    print("1. addition")
    print("2. subtraction")
    print("3. multiplication")
    print("4. division")
    print("5. Percentage")
    print("6. All of the above")

    print("Pick your function from given above")

    # Here is where we are getting input from user for to do above operation
    opinion_for_normal_calc = int(input())
    if opinion_for_normal_calc == 1:
        print("addition of two number is %s" % (chirpy_normal_calc.add()))
        print("Welcome again")
    elif opinion_for_normal_calc == 2:
        print("subtraction of two number is %s" % (chirpy_normal_calc.sub()))
        print("Welcome again")
    elif opinion_for_normal_calc == 3:
        print("multiplication of two number is %s" % (chirpy_normal_calc.mul()))
        print("Welcome again")
    elif opinion_for_normal_calc == 4:
        print("division of two number is %s" %(chirpy_normal_calc.div()))
        print("Welcome again")
    elif opinion_for_normal_calc == 5:
        print("percentage is %s" %(chirpy_normal_calc.percentage()))
        print("Welcome again")
    elif opinion_for_normal_calc == 6:
        print("addition %s" % (chirpy_normal_calc.add()))
        print("subtraction %s" % (chirpy_normal_calc.sub()))
        print("multiplication %s" % (chirpy_normal_calc.mul()))
        print("division %s" % (chirpy_normal_calc.div()))
        print("percentage %s" % (chirpy_normal_calc.percentage()))
        print("Welcome again")

    else:
        sys.exit()

elif which_calc == "s":
    class Scientific_calc:
        print("=" * 42)
        print("Welcome to your scientific calc ('Radian')")
        print("=" * 42)

        def __init__(self, func_number):
            self.func_number = func_number

        def cos(self):
            return math.cos(self.func_number)

        def sin(self):
            return math.sin(self.func_number)

        def log(self):
            return math.log10(self.func_number)

        def pi(self):
            return 3.14 * self.func_number

        def tan(self):
            return math.tan(self.func_number)

        def square_root(self):
            return math.sqrt(self.func_number)


    list_of_scientific_calc_function = "You can do cos, sin, log, Pi, tan, square_root in this calc"
    print(list_of_scientific_calc_function)
    print("*" * 59)
    user_number = int(input("Enter the digit:-"))
    chirpy_scientific_calc = Scientific_calc(func_number=user_number)
    print("0. Exit")
    print("1. cos")
    print("2. sin")
    print("3. log")
    print("4. Pi")
    print("5. tan")
    print("6. Square_root")
    print("Pick your function from given above")

    opinion_for_scientific_calc = int(input())




    if opinion_for_scientific_calc == 1:
        print("Cos %s" % (chirpy_scientific_calc.cos()))
        print("Welcome again")
    elif opinion_for_scientific_calc == 2:
        print("Sin %s" % (chirpy_scientific_calc.sin()))
        print("Welcome again")
    elif opinion_for_scientific_calc == 3:
        print("Log %s" % (chirpy_scientific_calc.log()))
        print("Welcome again")
    elif opinion_for_scientific_calc == 4:
        print("Pi %s" % (chirpy_scientific_calc.pi()))
        print("Welcome again")
    elif opinion_for_scientific_calc == 5:
        print("Tan %s" % (chirpy_scientific_calc.tan()))
        print("Welcome again")
    elif opinion_for_scientific_calc == 6:
        print("Tan %s" % (chirpy_scientific_calc.square_root()))
        print("Welcome again")
    else:
        sys.exit()


else:
    sys.exit()




