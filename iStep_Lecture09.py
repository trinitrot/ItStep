# დავალება 1

def  find_min_max (int_list):

    if len(int_list) == 0:
        return "the function does not accept empty lists"

    if type(int_list) != list:
        return "the function accepts only lists"

    for i in int_list:
        if type(i) != int:
            return "the function accepts only a list of ints"

    sorted_list = sorted(int_list)
    return sorted_list[0], sorted_list[-1]

# print(find_min_max([654,987,6,5]))


# დავალება 2

def calculate(data, operation):

    if len(data) == 0:
        return "the function does not accept empty lists"

    if type(data) != list:
        return "the function accepts only a lists"

    for i in data:
        if type(i) not in (int, float):
            return "the function accepts only a list of ints"

    if operation not in ("sum", "max", "min", "mult"):
        return 'Function accepts only "sum", "max", "min", "mult" as operation'
    elif operation == "sum":
        return sum(data)
    elif operation == "max":
        return max(data)
    elif operation == "min":
        return min(data)
    else:
        mult = 1

        for i in data:
            mult *= i

        return mult

# print(calculate([]))

# დავალება 3

def safe_divide(a, b):

    try:
        float(a)
        float(b)
    except ValueError:
        return "function accepts only numbers"

    if b == 0:
        return "Cannot divide by zero"
    else:
        return a // b, a % b

# print(safe_divide(45,987))