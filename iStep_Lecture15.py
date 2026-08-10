# დავალება 1

with open("data.txt","r") as file:
    text = file.read()

print(f"სტრიქონები {len(text.split('\n'))}")
print(f"სიტყვები {len(text.split())}")
print(f"სიმოლოები {len(text)}")


# დავალება 2

while True:
    text = input("შეიყვანე ტექსტი: ")

    if text == "exit":
        break

    with open("journal.txt","a") as file:
        file.write(text + "\n")