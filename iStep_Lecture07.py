# დავალება 1

numbers = [12, 5, 8, 20, 3, 15]
count = 0

print(f"ლისტის მაქსიმალური წევრია: {max(numbers)}")
print(f"ლისტის მინიამლური წევრია: {min(numbers)}")

for i in numbers:
    if i > 10:
        count += 1
print(f"10-ზე მეტი მნიშვნელობა აქვს ლისტის {count} წევრს")

even_list = []

for i in numbers:
    if i % 2 == 0:
        even_list.append(i)
print(f"ლისტის ლუწი წევრებია {even_list}")

# დავალება 2

student = ("Giorgi", 17, "Python", 95)

print(student[0])
print(student[1])

if student[3] > 90:
    print("მეტია 90-ზე")
else:
    print("ნაკლებია დან ტოლი 90-ის")

student_new = student + ("Tbilisi",)
print(student_new)

# დავალება 3

products = [ ("Apple", 2.5), ("Banana", 1.2), ("Orange", 3.0), ("Milk", 4.5) ]
products_sum = 0.0
products_pricey = products[0]

print("პროდუქტების სია:", [i for i,j in products])

for i in products:
    products_sum += i[1]

print("პროდუქტების ფასების ჯამი:", products_sum)

for i in products:
    if i[1] > products_pricey[1]:
        products_pricey = i

print("ყველაზე ძვირი პროდუქტი:", products_pricey[0])

products_new = [(i,j) for i,j in products if j > 3]
print("ახალი ლისტი:", products_new)