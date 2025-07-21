num1 = float(input("Enter first number: "))
operator = input("Enter operation (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Perform calculation
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Cannot divide by zero."
else:
    result = "Invalid operator!"

# Show result
print("Result:", result)