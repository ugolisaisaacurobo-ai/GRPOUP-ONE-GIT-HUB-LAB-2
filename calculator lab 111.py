
# Global variables for history, memory, and last result
history = []
memory = 0
last_result = None

def get_number(prompt):
    """
    Prompt the user for a number or 'ANS'. Validate input and return a float.
    """
    global last_result
    while True:
        num_str = input(prompt).strip()
        if num_str.upper() == 'ANS':
            if last_result is None:
                print("No previous result to use for ANS.")
                continue
            return last_result
        try:
            value = float(num_str)
            return value
        except ValueError:
            print("Invalid input. Please enter a number or 'ANS'.")

def calculate():
    """
    Perform a multi-step calculation, update history and last_result.
    """
    global last_result, history

    # Get initial number (allow ANS)
    num = get_number("Enter a number (or ANS for last result): ")
    result = num
    expr = str(result)

    while True:
        op = input("Enter operation (+, -, *, /, %, ** for exponent, sqrt, or = to finish): ").strip()
        if op == '=':
            break
        if op.lower() == 'sqrt':
            if result < 0:
                print("Error: Math error.")
                continue
            result = math.sqrt(result)
            expr = f"√({expr})"
            print(f"Current result: {result}")
            continue
        if op in ('+', '-', '*', '/', '%', '**'):
            next_num = get_number("Enter next number (or ANS): ")
            # Handle division/modulus by zero
            if (op == '/' or op == '%') and next_num == 0:
                print("Error: undefined.")
                continue
            # Perform operation
            if op == '+':
                result = result + next_num
            elif op == '-':
                result = result - next_num
            elif op == '*':
                result = result * next_num
            elif op == '/':
                result = result / next_num
            elif op == '%':
                result = result % next_num
            elif op == '**':
                result = result ** next_num
            expr = f"{expr} {op} {next_num}"
            print(f"Current result: {result}")
        else:
            print("Invalid operation. Try again.")

    print(f"Result: {result}")
    last_result = result
    history.append(f"{expr} = {result}")

def view_history():
    """Display the calculation history."""
    if history:
        print("Calculation History:")
        for entry in history:
            print(entry)
    else:
        print("History is empty, feel free to perfom calculation.")

def clear_history():
    """Clear the calculation history."""
    global history
    history = []
    print("History cleared.")

def memory_menu():
    """
    Memory operations: M+, M-, MR, MC, or return to main menu.
    """
    global memory, last_result
    while True:
        choice = input("Memory - Enter M+, M-, MR, MC, or B to go back: ").strip().upper()
        if choice == 'M+':
            if last_result is None:
                print("No last result to add to memory.")
            else:
                memory += last_result
                print(f"Added {last_result} to memory.")
        elif choice == 'M-':
            if last_result is None:
                print("No last result to subtract from memory.")
            else:
                memory -= last_result
                print(f"Subtracted {last_result} from memory.")
        elif choice == 'MR':
            print(f"Memory = {memory}")
        elif choice == 'MC':
            memory = 0.0
            print("Memory cleared.")
        elif choice == 'B':
            break
        else:
            print("Invalid memory command.")

def main():
    """Main program loop with menu options."""
    while True:
        print("Weclome!!!")
        print("\nPlease select an operation from the following options:")
        print("1. Calculate")
        print("2. View History")
        print("3. Clear History")
        print("4. Memory Functions")
        print("5. Quit")
        choice = input("Select an option (1-5): ").strip()

        if choice == '1':
            calculate()
        elif choice == '2':
            view_history()
        elif choice == '3':
            clear_history()
        elif choice == '4':
            memory_menu()
        elif choice == '5':
            print("Leaving so soon? :( Goodbye!! ")
            break
        else:
            print("Invalid selection. Please choose 1-5.")

if __name__ == "__main__":
    main()