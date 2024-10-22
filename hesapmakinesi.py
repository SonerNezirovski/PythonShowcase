import math
from sympy import symbols, Eq, solve
def basic_calculator():
    attempts = 3

    while attempts > 0:
        print("Choose the operation which you want:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Percentage (%)")
        print("6. Solve an algebraic equation")
        print("7. Geometry calculations (area, perimeter)")
        choice = input("Enter the number of the operation you want to perform: ")
        if choice == '1':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 + num2
            print(f"Result: {result}")
            break

        elif choice == '2':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 - num2
            print(f"Result: {result}")
            break

        elif choice == '3':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 * num2
            print(f"Result: {result}")
            break

        elif choice == '4':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if num2 == 0:
                print("Error: Division by zero is not allowed!")
            else:
                result = num1 / num2
                print(f"Result: {result}")
            break

        elif choice == '5':
            base = float(input("Enter the base value: "))
            percentage = float(input("Enter the percentage: "))
            result = (percentage / 100) * base
            print(f"{percentage}% of {base} is {result}")
            break

        elif choice == '6':
            print("Example: Solve an equation like '2*x + 3 = 7'")
            x = symbols('x')
            equation = input("Enter an equation (in terms of x, use '*' for multiplication): ")
            eq = Eq(eval(equation.split('=')[0]), eval(equation.split('=')[1]))
            solution = solve(eq, x)
            print(f"Solution for x: {solution}")
            break

        elif choice == '7':
            # Geometry calculations
            print("Choose a shape:")
            print("1. Square (area, perimeter)")
            print("2. Circle (area, circumference)")
            shape_choice = input("Enter the number of the shape: ")

            if shape_choice == '1':
                side = float(input("Enter the length of the side of the square: "))
                area = side ** 2
                perimeter = 4 * side
                print(f"Area of the square: {area}")
                print(f"Perimeter of the square: {perimeter}")
            elif shape_choice == '2':
                radius = float(input("Enter the radius of the circle: "))
                area = math.pi * radius ** 2
                circumference = 2 * math.pi * radius
                print(f"Area of the circle: {area}")
                print(f"Circumference of the circle: {circumference}")
            else:
                print("Invalid shape choice.")
            break

        else:
            attempts -= 1
            if attempts > 0:
                print(f"Invalid operation choice. You have {attempts} attempts left.")
            else:
                print("Invalid operation choice. No attempts left. Exiting the program.")
                break
basic_calculator()
