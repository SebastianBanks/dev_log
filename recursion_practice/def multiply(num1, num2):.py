def multiply(num1, num2):
    if num1 == 0 or num2 == 0:
        return 0

    return num1 + multiply(num1, num2 - 1)

print(multiply(2, 2))