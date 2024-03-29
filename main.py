import os
import time
import random

GREEN = '\033[92m'
BLUE = '\033[94m'
RESET = '\033[0m'

def menu():

    def question_range(operation_sign):
        os.system("cls")
        print(f"Range: [() to ()] {operation_sign} [() to ()]")
        while True:
            
            range_input = input("Enter left operand range as a,b: ")
            if range_input == 'Q'or range_input == 'q':
                exit() 
            elif range_input == "B" or range_input == 'b':
                menu()
            try:
                range_a, range_b = map(int, range_input.split(","))
            except ValueError:
                os.system('cls')
                print("Invalid input. Please enter a valid range as a,b or 'Q' to quit.")
                continue

            range_input = input("Enter right operand range as c,d: ")
            if range_input == 'Q' or range_input == 'q':
                exit() 
            elif range_input == "B" or range_input == 'b':
                menu()
            try:
                range_c, range_d = map(int, range_input.split(","))
            except ValueError:
                os.system('cls')
                print("Invalid input. Please enter a valid range as c,d or 'Q' to quit.")
                continue

            num_questions = input("Number of questions: ").upper()
            if num_questions == 'Q':
                exit()  
            elif num_questions == "B":
                menu()
            try:
                num_questions = int(num_questions)
            except ValueError:
                os.system('cls')
                print("Invalid input. Please enter a valid number of questions.")
                continue

            if range_a > range_b or range_c > range_d or num_questions < 0:
                input("Invalid response. Press retype your inputs. ")
                question_range(operation_sign)

            range_input = input(f"Range - [{range_a} to {range_b}] {operation_sign} [{range_c} to {range_d}] for {num_questions} questions (Y/N): ").upper()
            
            if range_input == 'Q' or range_input == 'q':
                exit() 
            elif range_input == "B" or range_input == 'b':
                menu()
            try:
                num_questions = int(num_questions)
            except ValueError:
                os.system('cls')
                print("Invalid input. Please enter a valid response.")
                continue

            if range_input == "Y" or range_input == 'y':
                if operation_sign == "+":
                    addition(range_a, range_b, range_c, range_d, operation_sign, num_questions)
                elif operation_sign == "-":
                    subtraction(range_a, range_b, range_c, range_d, operation_sign, num_questions)
                elif operation_sign == "*":
                    multiplication(range_a, range_b, range_c, range_d, operation_sign, num_questions)  
                elif operation_sign == "/":
                    division(range_a, range_b, range_c, range_d, operation_sign, num_questions)
            if range_input == "N" or range_input == 'n':
                question_range(operation_sign) 
            if range_input == "Q" or range_input == 'q':
                exit()
            if range_input == "B" or range_input == 'b':
                menu()
            else:
                os.system('cls')
                print("Invalid input. Please enter a valid response.")
                continue
    
    def help_menu():
        os.system('cls')
        print(f"Mental Math Monster ({GREEN}Triple-M-{BLUE}Lite{RESET})\nPress 'Q' to quit the game and 'B' to go back to the main menu.\n")
        help_menu_input = input("Input: ").upper()
        help_menu_list = ["Q", "B"]
        while help_menu_input not in help_menu_list:
            help_menu_input = input("Select a valid input:").upper()
        if help_menu_input == "Q":
            exit()
        if help_menu_input == "B":
            menu()

    menu_list = ["A", "S", "M", "D", "Q", "H", "B"]
    os.system("cls")
    print(f"""Mental Math Monster ({GREEN}Triple-M-{BLUE}Lite{RESET}) \n{GREEN}(A){RESET} {BLUE}Addition\n{GREEN}(S){RESET} {BLUE}Subtraction\n{GREEN}(M){RESET} {BLUE}Multiplication\n{GREEN}(D){RESET} {BLUE}Division\n{GREEN}(H){RESET} {BLUE}Help{RESET}\n """)
    menu_input = input(f"Input: ").upper()
    while menu_input not in menu_list:
        menu_input = input("Select a valid input:").upper()
    while menu_input == "B":
        menu_input = input("You're as far back as you can go, selct another input: ").upper()
    if menu_input == "A":
        question_range("+")
    if menu_input == "S":
        question_range("-")
    if menu_input == "M":
        question_range("*")
    if menu_input == "D":
        question_range("/")
    if menu_input == "Q":
        exit()
    if menu_input == "H":
        help_menu()
        
   
def addition(range_a, range_b, range_c, range_d, operation_sign, num_questions):
    score = 0
    total_attempts = 0
    for _ in range(num_questions):  # Limit the number of questions
        left_operator = random.randint(range_a, range_b)
        right_operator = random.randint(range_c, range_d)
        answer = str(left_operator + right_operator)
        
        os.system('cls')
        print(f"Addition Practice  |  Score: {score}  |  Total Attempts: {total_attempts}")

        while True:
            user_input = input(f"{left_operator} {operation_sign} {right_operator} = ")

            if user_input == answer:
                score += 1
                total_attempts += 1
                os.system('cls')
                print(f"Addition Practice  |  Score: {score}  |  Total Attempts: {total_attempts}")
                break
            elif user_input == "Q" or user_input == 'q':
                exit()
            elif user_input == "B" or user_input == 'b':
                menu()
            else:
                total_attempts += 1
                os.system('cls')
                print(f"Addition Practice  |  Score: {score}  |  Total Attempts: {total_attempts}")
    os.system('cls')
    print(input(f"Category: Addition\nTotal Score: {score}\nTotal Attempts: {total_attempts}\n"))            
    menu()

def subtraction(range_a, range_b, range_c, range_d, operation_sign, num_questions):
    score = 0
    total_attempts = 0
    for _ in range(num_questions):  # Limit the number of questions
        left_operator = random.randint(range_a, range_b)
        right_operator = random.randint(range_c, range_d)
        answer = str(left_operator - right_operator)
        os.system('cls')
        print(f"Subtraction Practice  |  Score: {score}  |  Total Attempts: {total_attempts}")

        while True:
            user_input = input(f"{left_operator} {operation_sign} {right_operator} = ")

            if user_input == answer:
                score += 1
                total_attempts += 1
                os.system('cls')
                print(f"Subtraction Practice  |  Score: {score}  |  Total Attempts: {total_attempts}")
                break
            elif user_input == "Q" or user_input == 'q':
                exit()
            elif user_input == "B" or user_input == 'b':
                menu()
            else:
                total_attempts += 1
                os.system('cls')
                print(f"Subtraction Practice  |  Score: {score}  |  Total Attempts: {total_attempts}")
    os.system('cls')
    print(input(f"Category: Subtraction  |  Total Score: {score}  |  Total Attempts: {total_attempts}"))            
    menu()

def multiplication(range_a, range_b, range_c, range_d, operation_sign, num_questions):
    score = 0
    total_attempts = 0
    for _ in range(num_questions):  # Limit the number of questions
        left_operator = random.randint(range_a, range_b)
        right_operator = random.randint(range_c, range_d)
        answer = str(left_operator * right_operator)
        os.system('cls')
        print(f"Multiplication Practice\nScore: {score}\nTotal Attempts: {total_attempts}\n")

        while True:
            user_input = input(f"{left_operator} {operation_sign} {right_operator} = ")

            if user_input == answer:
                score += 1
                total_attempts += 1
                os.system('cls')
                print(f"Multiplication Practice  |  Score: {score}  |  Total Attempts: {total_attempts}")
                break
            elif user_input == "Q" or user_input == 'q':
                exit()
            elif user_input == "B" or user_input == 'b':
                menu()
            else:
                total_attempts += 1
                os.system('cls')
                print(f"Multiplication Practice  |  Score: {score}  |  Total Attempts: {total_attempts}")
    os.system('cls')
    print(input(f"Category: Multiplication\nTotal Score: {score}\nTotal Attempts: {total_attempts}\n"))            
    menu()

def division(range_a, range_b, range_c, range_d, operation_sign, num_questions):
    score = 0
    total_attempts = 0
    for _ in range(num_questions):  # Limit the number of questions
        left_operator = random.randint(range_a, range_b)
        right_operator = random.randint(range_c, range_d)
        answer = str(int(left_operator / right_operator))
        os.system('cls')
        print(f"Division Practice  |  Score: {score}  |  Total Attempts: {total_attempts}")

        while True:
            user_input = input(f"{left_operator} {operation_sign} {right_operator} = ")

            if user_input == answer:
                score += 1
                total_attempts += 1
                os.system('cls')
                print(f"Division Practice  |  Score: {score}  |  Total Attempts: {total_attempts}")
                break
            elif user_input == "Q" or user_input == 'q':
                exit()
            elif user_input == "B" or user_input == 'b':
                menu()
            else:
                total_attempts += 1
                os.system('cls')
                print(f"Division Practice  |  Score: {score}  |  Total Attempts: {total_attempts}")
    os.system('cls')
    print(input(f"Category: Division\nTotal Score: {score}\nTotal Attempts: {total_attempts}\n"))            
    menu()


if __name__ == '__main__':
    menu()