Program make a simple calculator

def add(x, y):         # This function adds two numbers
    return x + y
def subtract(x, y):    # This function subtracts two numbers
    return x - y
def multiply(x, y):    # This function multiplies two numbers
    return x * y
def divide(x, y):      # This function divides two numbers
    return x / y

print("Select operation.")
print("a.Add")
print("b.Subtract")
print("c.Multiply")
print("d.Divide")

while True:
    choice = input("Enter choice(a/b/c/d): ")    # Take input from the user
    if choice in ('a', 'b', 'c', 'd'):           # Check if choice is one of the four options
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 'a':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == 'b':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == 'c':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == 'd':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")
