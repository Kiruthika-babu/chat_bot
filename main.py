print ( "BOT: Welcome to chatbot, I'm Mathbot " )
user_input = input ( "USER:" )
import math


def math_bot() :
    while True :
        # Get user input
        print ( "BOT:What operation would you like me to perform? or You can quit my friend😑")
        1.
        "Addition"
        2.
        "Subtract"

        user_input_1 = input ( "USER:" )

        # Exit the loop if the user enters "quit" message
        if user_input_1 == "quit" :
            print ( "BOT:Goodbye!😒" )
            break

        print ( "BOT:Please enter the First operand" )
        operand1 = int ( input ( "USER:" ) )

        print ( "BOT:Please enter the Second operand" )
        operand2 = int ( input ( "USER:" ) )

        # Perform the appropriate operation correctly and print the result to display
        if user_input_1 == "addition" or user_input_1 == "add" :
            result = operand1 + operand2
            print ( "BOT:The sum of", operand1, "and", operand2, "is", result )
        elif user_input_1 == "subtraction" or user_input_1 == "sub" :
            result = operand1 - operand2
            print ( "BOT:The difference between", operand1, "and", operand2, "is", result )
        elif user_input_1 == "multiplication" or user_input_1 == "multiply" :
            result = operand1 * operand2
            print ( "BOT:The product of", operand1, "and", operand2, "is", result )
        elif user_input_1 == "division" or user_input_1 == "divide" :
            if operand2 == 0 :
                print ( "BOT:Cannot divide by zero!" )
            else :
                result = operand1 / operand2
                print ( "BOT:The quotient of", operand1, "and", operand2, "is", result )
        elif user_input_1 == "Power of" or user_input_1 == "power" :
            result = operand1 ** operand2
            print ( "BOT:The power of", operand1, "and", operand2, "is", result )
        elif user_input_1 == "Square root" or user_input_1 == "square" :
            result = pow ( operand1, 1 / operand2 )
            print ( "BOT:The square root of", operand1, "to the", operand2, "is", result )
        else :
            print ( "BOT:Invalid operator. Please enter a valid operation" )

        print ( "BOT:Do you want to continue?(yes/no)" )
        opt = input ( "USER:" )
        if opt == "no" :
            print ( "BOT:Thank you for using the MathBot" )
            break
        else :
            continue


# Call the chat bot function
math_bot ()