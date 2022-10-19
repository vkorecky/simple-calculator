# Program make a simple calculator
import tools


# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    return x / y


def main():
    while True:
        print("Select operation.")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Add from file")
        print("0. Exit")

        # take input from the user
        choice = input("Enter choice(1/2/3/4/5/0): ")

        # check if choice is one of the four options
        if choice in ('1', '2', '3', '4', '5', '0'):
            if choice == '0':
                break

            if choice == '5':
                nums = tools.load_nums_from_file()
                for pair in nums:
                    x = pair[0]
                    y = pair[1]
                    print(x, "+", y, "=", add(x, y))
            else:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))

                if choice == '1':
                    print(x, "+", y, "=", add(x, y))

                elif choice == '2':
                    print(x, "-", y, "=", subtract(x, y))

                elif choice == '3':
                    print(x, "*", y, "=", multiply(x, y))

                elif choice == '4':
                    print(x, "/", y, "=", divide(x, y))

        else:
            print("Invalid Input")


if __name__ == "__main__":
    main()
