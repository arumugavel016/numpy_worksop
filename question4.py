#write a program to find the sum of digits of a given number'
def sum_of_digits_iterative(n):
    n = abs(n)  # Ensure the number is positive
    sum_digits = 0
    while n > 0:
        sum_digits += n % 10
        n //= 10
    return sum_digits

number = 12345
print(f"Sum of digits of {number} (iterative): {sum_of_digits_iterative(number)}")
