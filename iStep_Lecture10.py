# დავალება 1

def sum_of_digits(n):
    if type(n) is not int :
        raise TypeError("function accepts only integers")
    elif n < 0:
        raise ValueError("function does not accept negative numbers")

    if n < 10:
        return n

    return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(0))



# დავალება 2

is_even = lambda n: n % 2 == 0

print(is_even(456))



# დავალება 3

students = [("Luka", 15, 85), ("Ana", 14, 92), ("Giorgi", 16, 78), ("Nino", 15, 95)]

students_sorted = sorted(students, key=lambda x: (x[1], x[2]))

print(students_sorted)



# დავალება 4

words = ["banana", "apple", "kiwi", "watermelon", "cherry"]

words_sorted = sorted(words, key=lambda x: len(x), reverse=True)

print(words_sorted)



# დავალება 5

words_upper = list(map(lambda x: x[0].upper() + x[1:], words))

print(words_upper)



# დავალება 6

numbers = [5, 12, 7, 18, 3, 24, 9]

numbers_filtered = list(filter(lambda x: x > 10 and x % 3 == 0, numbers))

print(numbers_filtered)

