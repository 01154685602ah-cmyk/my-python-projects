def calc(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    return "Unknown operation"

while True:
    try:
        a = float(input("First number: "))
        op = input("Operation (+ - * /): ")
        b = float(input("Second number: "))
        print("Result:", calc(a, b, op))
    except ValueError:
        print("Please enter numbers only.")
    if input("Again? (y/n): ") != "y":
        break
