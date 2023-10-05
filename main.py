import os

def menu():
    print("""Mental Math (Double-M) \n(A) Addition\n(S) Subtraction\n(M) Multiplication\n(D) Division\n(T) Times-tables """)
    menu_input = input("User Input: ")

    while menu_input != "T":
        menu_input = input("Select a valid input:")

        if menu_input == "T":
            times_tables()

def times_tables():
    os.system('cls')
    print("Times-tables\nPress Q to quit")

    


if __name__ == '__main__':
    menu()