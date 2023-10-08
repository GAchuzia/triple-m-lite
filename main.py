import os

def menu():
    print("""Mental Math (Double-M) \n(A) Addition\n(S) Subtraction\n(M) Multiplication\n(D) Division\n(T) Times-tables """)
    menu_input = input("Input: ")

    while menu_input != "T":
        menu_input = input("Select a valid input:")

    if menu_input == "T":
        times_tables()

def addition():
    pass

def subtraction():
    pass

def multiplication():
    pass

def division():
    pass

def question_range():
    pass
def times_tables():

    for left_operator in range (2, 13):
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