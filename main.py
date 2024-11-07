import random


def main_menu():
    # Purpose: Display the menu options and get a valid choice from the user.
    # Parameters: None
    # Return: Integer representing the user's choice.
    print("\nWelcome to the ASCII Art Program!")
    print("Choose an option:")
    print("1. Display a circle")
    print("2. Display a set of lines")
    print("3. Display a random design")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")
    while choice.isdigit() != True or int(choice) < 1 or int(choice) > 4:
        choice = input("Invalid input. Enter a choice (1-4): ")

    return int(choice)


def display_circle():
    # Purpose: Display an ASCII approximation of a circle.
    # Parameters: None
    # Return: None
    print("   _____  ")
    print(" /       \\")
    print("|         |")
    print(" \\ _____ / ")


def display_lines(num_lines, character, repeat_count):
    # Purpose: Display a specified number of lines with repeated characters.
    # Parameters:
    #     - num_lines: Integer, number of lines to display.
    #     - character: String, character(s) to use in the line.
    #     - repeat_count: Integer, number of times to repeat the character(s).
    # Return: None
    count = 0
    while count != num_lines:
        print(character * repeat_count)
        count += 1


def design_1():
    # Purpose: Display a predefined ASCII art design.
    # Parameters: None
    # Return: None
    print(r"""\,--------'()'--o
(_    ___    /~"
 (_)_)  (_)_)""")


def design_2():
    # Purpose: Display a symmetrical diamond-like ASCII art design.
    # Parameters: None
    # Return: None
    i = 0
    while i != 5:
        print(" " * i + "*" + " " * (8 - 2 * i) + "*")
        i += 1
    i = 3
    while i != -1:
        print(" " * i + "*" + " " * (8 - 2 * i) + "*")
        i -= 1


def design_3():
    # Purpose: Display a box-like ASCII art design.
    # Parameters: None
    # Return: None
    print("[--]")
    print("|   |")
    print("|   |")
    print("|   |")
    print("[--]")


def display_random_design():
    # Purpose: Display one of the three random ASCII designs.
    # Parameters: None
    # Return: None
    designs = [design_1, design_2, design_3]
    random_index = random.randint(0, 2)
    designs[random_index]()


def main():
    # Purpose: Coordinate the program by displaying the menu, getting user’s choice, and calling appropriate functions.
    # Parameters: None
    # Return: None
    choice = main_menu()
    while choice != 4:
        if choice == 1:
            display_circle()
        elif choice == 2:
            num_lines = int(input("How many lines? "))
            character = input("What character(s) to use? ")
            repeat_count = int(input("How many times to repeat? "))
            display_lines(num_lines, character, repeat_count)
        elif choice == 3:
            display_random_design()

        # Call the menu again to continue the loop
        choice = main_menu()

    print("Goodbye!")


# Run the program
if __name__ == "__main__":
    main()
