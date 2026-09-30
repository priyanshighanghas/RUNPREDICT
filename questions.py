"""CSE1021-aligned practice questions."""

import random
from algorithms import factorial, fibonacci, reverse_number, gcd, sum_to_n


def get_question(level):
    if level == 1:
        return basic_question()
    if level == 2:
        return control_question()
    if level == 3:
        return algorithm_question()
    return collection_question()


def basic_question():
    choice = random.randint(1, 2)

    if choice == 1:
        a = random.randint(2, 8)
        b = random.randint(3, 9)
        code = (
            "a = " + str(a) + "\n"
            "b = " + str(b) + "\n"
            "a, b = b, a\n"
            "print(a)\n"
            "print(b)"
        )
        answer = str(b) + "\n" + str(a)
        hint = "Tuple assignment swaps the two values."
        topic = "Variables and tuple assignment"
    else:
        a = random.randint(2, 8)
        b = random.randint(5, 15)
        value = a * 2 + b
        code = (
            "a = " + str(a) + "\n"
            "b = " + str(b) + "\n"
            "c = a * 2 + b\n"
            "print(c)"
        )
        answer = str(value)
        hint = "Do multiplication before addition."
        topic = "Expressions and operator precedence"

    return code, answer, hint, topic


def control_question():
    choice = random.randint(1, 2)

    if choice == 1:
        n = random.randint(4, 7)
        answer = str(sum_to_n(n))
        code = (
            "n = " + str(n) + "\n"
            "total = 0\n"
            "i = 1\n"
            "while i <= n:\n"
            "    total = total + i\n"
            "    i = i + 1\n"
            "print(total)"
        )
        hint = "Add the values of i from 1 to n."
        topic = "While loop and summation"
    else:
        n = random.randint(5, 9)
        total = 0
        for i in range(1, n + 1):
            if i % 2 == 0:
                total = total + i
        answer = str(total)
        code = (
            "total = 0\n"
            "for i in range(1, " + str(n + 1) + "):\n"
            "    if i % 2 == 0:\n"
            "        total = total + i\n"
            "print(total)"
        )
        hint = "Only even values of i are added."
        topic = "For loop and conditional statement"

    return code, answer, hint, topic


def algorithm_question():
    choice = random.randint(1, 4)

    if choice == 1:
        n = random.randint(3, 6)
        answer = str(factorial(n))
        code = (
            "n = " + str(n) + "\n"
            "fact = 1\n"
            "for i in range(1, n + 1):\n"
            "    fact = fact * i\n"
            "print(fact)"
        )
        hint = "Multiply all integers from 1 through n."
        topic = "Factorial"
    elif choice == 2:
        n = random.randint(4, 7)
        answer = str(fibonacci(n))
        code = (
            "a = 0\n"
            "b = 1\n"
            "for i in range(" + str(n) + "):\n"
            "    a, b = b, a + b\n"
            "print(a)"
        )
        hint = "At each step, a becomes the old value of b."
        topic = "Fibonacci sequence"
    elif choice == 3:
        n = random.randint(123, 987)
        answer = str(reverse_number(n))
        code = (
            "n = " + str(n) + "\n"
            "reverse = 0\n"
            "while n > 0:\n"
            "    digit = n % 10\n"
            "    reverse = reverse * 10 + digit\n"
            "    n = n // 10\n"
            "print(reverse)"
        )
        hint = "Use % to take the last digit and // to remove it."
        topic = "Reverse a number"
    else:
        a = random.randint(12, 30)
        b = random.randint(6, 18)
        answer = str(gcd(a, b))
        code = (
            "a = " + str(a) + "\n"
            "b = " + str(b) + "\n"
            "while b != 0:\n"
            "    a, b = b, a % b\n"
            "print(a)"
        )
        hint = "Repeat the remainder operation until b becomes 0."
        topic = "GCD"

    return code, answer, hint, topic


def collection_question():
    choice = random.randint(1, 4)

    if choice == 1:
        items = [3, 5, 3, 2, 5, 7]
        result = []
        for x in items:
            if x not in result:
                result.append(x)
        code = (
            "items = [3, 5, 3, 2, 5, 7]\n"
            "result = []\n"
            "for x in items:\n"
            "    if x not in result:\n"
            "        result.append(x)\n"
            "print(result)"
        )
        answer = str(result)
        hint = "Add a value only when it is not already in result."
        topic = "List and duplicate removal"
    elif choice == 2:
        numbers = [2, 4, 2, 5, 2, 7]
        count = numbers.count(2)
        code = (
            "numbers = [2, 4, 2, 5, 2, 7]\n"
            "count = 0\n"
            "for x in numbers:\n"
            "    if x == 2:\n"
            "        count = count + 1\n"
            "print(count)"
        )
        answer = str(count)
        hint = "Increase count whenever x is 2."
        topic = "Array/list counting"
    elif choice == 3:
        data = (4, 7, 2)
        code = (
            "data = (4, 7, 2)\n"
            "print(data[1])"
        )
        answer = "7"
        hint = "List and tuple indexing starts at 0."
        topic = "Tuple indexing"
    else:
        code = (
            "student = {'name': 'Ravi', 'marks': 18}\n"
            "print(student['marks'])"
        )
        answer = "18"
        hint = "The key 'marks' stores the value 18."
        topic = "Dictionary access"

    return code, answer, hint, topic
