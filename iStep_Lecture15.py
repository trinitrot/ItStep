# დავალება 1

with open("data.txt","r") as file:
    text = file.read()

print(f"{len(text.split('\n'))} სტრიქონი")
print(f"{len(text.split())} სიტყვა")
print(f"{len(text)} სიმბოლო")


# დავალება 2

while True:
    text = input("შეიყვანე ტექსტი: ")

    if text == "exit":
        break

    with open("journal.txt","a") as file:
        file.write(text + "\n")