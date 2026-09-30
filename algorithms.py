"""Basic algorithms used by RUNPREDICT."""


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a


def reverse_number(n):
    reverse = 0
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10
    return reverse


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total
