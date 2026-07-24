# დავალება 1

total = 0
next_int = 1

while next_int != 0:
    try:
        next_int = int(input("შეიყვანენთ მთელი რიცხვი: "))
        total += next_int
    except ValueError:
        print("შეიყვანეთ მხოლოდ მთელი რიცხვი")

print("შეყვანილი რიცხვების ჯამია:", total)

# დავალება 2

number_to_guess = 98

while True:
    try:
        guessed = float(input("გამოიცანით ჩაფიქრებული რიცხვი: "))
        if guessed > number_to_guess:
            print("Too high")
        elif guessed < number_to_guess:
            print("Too low")
        else:
            break
    except ValueError:
        print("შეიყვანეთ მხოლოდ რიცხვი")

# დავალება 3

text = input("შეიყვანეთ ქართული ტექსტი: ")
vowels = 0

for i in text:
    if i in ("ა", "ე", "ი", "ო", "უ"):
        vowels += 1

print(vowels)

# დავალება 4

correct_pin = "1234"
wrong_pin_counter = 0
balance = 0

while wrong_pin_counter < 3:
    entered = input("შეიყვანე PIN: ")
    if entered == correct_pin:
        break
    else:
        wrong_pin_counter += 1
        print("არასწორი PIN, სცადე კიდევ ერთხელ")

if wrong_pin_counter == 3:
    print("---მომხმარებელი დაბლოკილია---")
else:
    while True:
        print("\n1) ბალანსის ნახვა \n2). თანხის შეტანა \n3) თანხის გატანა \n4) გამოსვლა")
        choice = input("აირჩიე: ")
        if choice == "4":
            break
        elif choice == "3":
            try:
                withdrawal = float(input("მიუთითე გასატანი თანხის რაოდენობა: "))
                if withdrawal > balance:
                    print("ბალანსზე არ არის საკმარისი თანხა")
                    continue
                elif withdrawal <= 0:
                    print("მიუთითე მხოლოოდ დადებითი რიცხრი")
                    continue
            except ValueError:
                print("შეიყვანე მხოლოდ თანხის რაოდენობა")
                continue
            print(f"გთხოვ აიღოოთ {withdrawal} ლარი")
            balance -= withdrawal
        elif choice == "2":
            try:
                top_up = float(input("შეიყვანე შესატანი თანხის რაოდენობა: "))
                if top_up <= 0:
                    print("მიუთითე მხოლოოდ დადებითი რიცხრი")
                    continue
            except ValueError:
                print("შეიყვანე მხოლოდ თანხის რაოდენობა")
                continue
            print(f"შენს ანგარიშზე ჩარიცხა {top_up} ლარი")
            balance += top_up
        elif choice == "1":
            print(f"შენს ანგარიშზე არის {balance} ლარი")
        else:
            print("არასწორი მნიშნველობა, შეიყვანე მხოლოდ: 1,2,3 ან 4")