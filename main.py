import os
import random

def menu():

    def question_range(operation_sign):
        os.system("cls")
        print(f"Range: [() to ()] {operation_sign} [() to ()]")
        while True:
            range_input = input("Enter left operand range as a,b: ")
            if range_input == 'Q':
                exit() # Quit the operation
            try:
                range_a, range_b = map(int, range_input.split(","))
            except ValueError:
                print("Invalid input. Please enter a valid range as a,b or 'Q' to quit.")
                continue

            range_input = input("Enter right operand range as c,d: ")
            if range_input == 'Q':
                exit() # Quit the operation
            try:
                range_c, range_d = map(int, range_input.split(","))
            except ValueError:
                print("Invalid input. Please enter a valid range as c,d or 'Q' to quit.")
                continue

            num_questions = input("Number of questions: ")
            if num_questions == 'Q':
                exit()  # Quit the operation
            try:
                num_questions = int(num_questions)
            except ValueError:
                print("Invalid input. Please enter a valid number of questions.")
                continue

            range_input = input(f"Range - [{range_a} to {range_b}] {operation_sign} [{range_c} to {range_d}] for {num_questions} questions (Y/N): ")
            if range_input == 'Q':
                exit() # Quit the operation
            try:
                num_questions = int(num_questions)
            except ValueError:
                print("Invalid input. Please enter a valid response.")
                continue

            if range_input == "Y":
                if operation_sign == "+":
                    addition(range_a, range_b, range_c, range_d, operation_sign, num_questions)
                elif operation_sign == "-":
                    subtraction(range_a, range_b, range_c, range_d, operation_sign, num_questions)
                elif ttable == 1:
                    times_tables(range_a, range_b, range_c, range_d, operation_sign, num_questions) 
                elif operation_sign == "*":
                    multiplication(range_a, range_b, range_c, range_d, operation_sign, num_questions)  
                elif operation_sign == "/":
                    division(range_a, range_b, range_c, range_d, operation_sign, num_questions)
            if range_input == "N":
                return  
            if range_input == "Q":
                exit()
            
    menu_list = ["A", "S", "M", "D", "T", "Q", "H"]
    ttable = 0
    os.system("cls")
    print("""Mental Math (Double-M) \n(A) Addition\n(S) Subtraction\n(M) Multiplication\n(D) Division\n(T) Times-tables \n(H) Help\n """)
    menu_input = input("Input: ")
    while menu_input not in menu_list:
        menu_input = input("Select a valid input:")
    if menu_input == "A":
        question_range("+")
    if menu_input == "S":
        question_range("-")
    if menu_input == "M":
        question_range("*")
    if menu_input == "D":
        question_range("/")
    if menu_input == "T":
        question_range("*")
        ttable = 1
    if menu_input == "Q":
        exit()

    
def addition(range_a, range_b, range_c, range_d, operation_sign, num_questions):
    for _ in range(num_questions):  # Limit the number of questions
        left_operator = random.randint(range_a, range_b)
        right_operator = random.randint(range_c, range_d)
        answer = str(left_operator + right_operator)
        os.system('cls')
        print("Addition\nPress Q to quit\n")

        while True:
            user_input = input(f"{left_operator} {operation_sign} {right_operator} = ")

            if user_input == answer:
                break
            elif user_input == "Q":
                exit()
            else:
                os.system('cls')
                print("Addition\nPress Q to quit\n")
    menu()

def subtraction(range_a, range_b, range_c, range_d, operation_sign, num_questions):
    for _ in range(num_questions):  # Limit the number of questions
        left_operator = random.randint(range_a, range_b)
        right_operator = random.randint(range_c, range_d)
        answer = str(left_operator - right_operator)
        os.system('cls')
        print("Subtraction\nPress Q to quit\n")

        while True:
            user_input = input(f"{left_operator} {operation_sign} {right_operator} = ")

            if user_input == answer:
                break
            elif user_input == "Q":
                exit()
            else:
                os.system('cls')
                print("Subtraction\nPress Q to quit\n")
    menu()

def multiplication(range_a, range_b, range_c, range_d, operation_sign, num_questions):
    for _ in range(num_questions):  # Limit the number of questions
        left_operator = random.randint(range_a, range_b)
        right_operator = random.randint(range_c, range_d)
        answer = str(left_operator * right_operator)
        os.system('cls')
        print("Multiplication\nPress Q to quit\n")

        while True:
            user_input = input(f"{left_operator} {operation_sign} {right_operator} = ")

            if user_input == answer:
                break
            elif user_input == "Q":
                exit()
            else:
                os.system('cls')
                print("Multiplication\nPress Q to quit\n")
    menu()

def division(range_a, range_b, range_c, range_d, operation_sign, num_questions):
    for _ in range(num_questions):  # Limit the number of questions
        left_operator = random.randint(range_a, range_b)
        right_operator = random.randint(range_c, range_d)
        answer = str(int(left_operator / right_operator))
        os.system('cls')
        print("Division\nPress Q to quit\n")

        while True:
            user_input = input(f"{left_operator} {operation_sign} {right_operator} = ")

            if user_input == answer:
                break
            elif user_input == "Q":
                exit()
            else:
                os.system('cls')
                print("Division\nPress Q to quit\n")
    menu()

def times_tables():
    for left_operator in range(2, 13):
        for right_operator in range(2, 13):
            answer = str(left_operator * right_operator)
            os.system('cls')
            print("Times-tables\nPress Q to quit\n")

            while True:
                tt_input = input(f"{left_operator} * {right_operator} = ")

                if tt_input == answer:
                    break
                elif tt_input == "Q":
                    return
                else:
                    os.system('cls')
                    print("Times-tables\nPress Q to quit\n")


if __name__ == '__main__':
    menu()