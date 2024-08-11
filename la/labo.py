def arithmetic_multiplication(n):
    digits = [int(i) for i in str(n)]
    product = 1
    for digit in digits:
        product *= digit
    return product

print(arithmetic_multiplication(349))  # Output: 108
