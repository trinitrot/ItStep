# დავალება 1

def find_min_max(int_list):
    minimum = int_list[0]
    maximum = int_list[0]

    for n in int_list:
        if n < minimum:
            minimum = n

        if n > maximum:
            maximum = n

    return minimum, maximum

# print(find_min_max([654, 987, 6, 5]))


# დავალება 2

def calculate(data, operation):
    if operation not in ("sum", "max", "min", "mult"):
        return 'Function accepts only "sum", "max", "min", "mult" as operation'

    if operation == "sum":
        total = 0

        for n in data:
            total += n

        return total

    if operation == "min":
        minimum = data[0]

        for n in data:
            if n < minimum:
                minimum = n

        return minimum

    if operation == "max":
        maximum = data[0]

        for n in data:
            if n > maximum:
                maximum = n

        return maximum

    if operation == "mult":
        multiplication = 1

        for n in data:
            multiplication *= n

        return multiplication

# print(calculate([2, 3, 6], "sum"))


# დავალება 3

def safe_divide(a, b):
    if type(a) != int or type(b) != int:
        return "function accepts only integers"

    if b == 0:
        return "Cannot divide by zero"

    return a // b, a % b

# print(safe_divide(45, 0.3))