def show_welcome():
    print("=" * 45)
    print("          PYTHON CALCULATOR v3.0")
    print("             Welcome, Ashok!")
    print("=" * 45)


def show_menu():
    print()
    print("MAIN MENU")
    print("-" * 20)
    print("1. Calculate")
    print("2. View History")
    print("3. Clear History")
    print("4. View Statistics")
    print("5. Exit")
    print()


def show_operations():
    print()
    print("AVAILABLE OPERATIONS")
    print("-" * 25)
    print("+  Addition")
    print("-  Subtraction")
    print("*  Multiplication")
    print("/  Division")
    print()


def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2

    elif operation == "-":
        return num1 - num2

    elif operation == "*":
        return num1 * num2

    elif operation == "/":
        if num2 == 0:
            return None
        return num1 / num2

    else:
        return None


def show_history(history):
    print()
    print("=" * 45)
    print("             CALCULATION HISTORY")
    print("=" * 45)

    if not history:
        print("No calculations yet.")
    else:
        for number, calculation in enumerate(history, start=1):
            print(f"{number}. {calculation}")

    print("=" * 45)


def clear_history(history):
    history.clear()

    print()
    print("Calculation history has been cleared.")


def show_statistics(calculation_count, history):
    print()
    print("=" * 45)
    print("              CALCULATOR STATISTICS")
    print("=" * 45)

    print("Total successful calculations:", calculation_count)
    print("Calculations currently in history:", len(history))
    print("Maximum history size: 10")

    print("=" * 45)


def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please enter a valid number.")


def perform_calculation(history):
    show_operations()

    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")

    operation = input(
        "Choose an operation (+, -, *, /): "
    ).strip()

    result = calculate(num1, num2, operation)

    if result is None:

        if operation == "/" and num2 == 0:
            print()
            print("Error: You cannot divide by zero.")

        else:
            print()
            print("Error: Invalid operation.")

        return False

    print()
    print("=" * 45)
    print("Result:", result)
    print("=" * 45)

    calculation = f"{num1} {operation} {num2} = {result}"

    history.append(calculation)

    # Keep only the last 10 calculations
    if len(history) > 10:
        history.pop(0)

    print("Calculation saved to history.")

    return True


def main():
    show_welcome()

    history = []
    calculation_count = 0

    while True:

        show_menu()

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":

            successful = perform_calculation(history)

            if successful:
                calculation_count += 1

        elif choice == "2":

            show_history(history)

        elif choice == "3":

            clear_history(history)

        elif choice == "4":

            show_statistics(
                calculation_count,
                history
            )

        elif choice == "5":

            print()
            print("=" * 45)
            print("Goodbye, Ashok!")
            print(
                "You completed",
                calculation_count,
                "successful calculation(s)."
            )
            print("=" * 45)

            break

        else:

            print()
            print("Invalid choice.")
            print("Please choose a number from 1 to 5.")


main()