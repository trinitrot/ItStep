import json
from dataclasses import dataclass, asdict


@dataclass
class Book:
    id: int
    title: str
    author: str
    year: int
    available: bool

# book1 = Book(1,"Code", "Tata", 2008, True)
# print(f"{book1.title}, {book1.author}")

# save books
def save_books(books):
    data = []

    for book in books:
        data.append(asdict(book))

    with open("books.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

    print("მონაცემები შენახულია!")


# retrieve books from file
def load_books():
    try:
        with open("books.json", "r", encoding="utf-8") as file:
            data = json.load(file)

    except FileNotFoundError:
        print("ფაილი არ არსებობს")
        return []

    except json.JSONDecodeError:
        print("ფაილი არსებობს, თუმცა წაიკითხვისას დაფიქსირდა შეცდომა")
        return []

    books = []

    for item in data:
        book = Book(
            item["id"],
            item["title"],
            item["author"],
            item["year"],
            item["available"]
        )
        books.append(book)

    return books

# inserting ა new book
def add_book(books):
    title = input("შეიყვანე სახელი: ").strip()
    author = input("შეიყვანე ავტორი: ").strip()

    if not title or not author:
        print("სახელი და ავტორი აუცილებლად შევსებული უნდა იყოს")
        return

    try:
        year = int(input("შეიყვანე წელი: "))
    except ValueError:
        print("წელი უნდა იყოს რიცხვი")
        return

    new_id = 1

    for book in books:
        if book.id >= new_id:
            new_id = book.id + 1

    new_book = Book(new_id, title, author, year, True)
    books.append(new_book)

    print("წიგნი შენახულია")
    print(f"ID: {new_book.id}")
    print(f"Title: {new_book.title}")
    print(f"Author: {new_book.author}")
    print(f"Year: {new_book.year}")
    print(f"Available: {new_book.available}")


# display all books
def show_books(books):
    if len(books) == 0:
        print("წიგნები ჯერ არ არის დამატებული")
        return

    for book in books:
        if book.available:
            status = "ხელმისაწვდომი"
        else:
            status = "გაცემული"

        print(f"ID: {book.id} | {book.title} | "
              f"{book.author} | {book.year} | {status}")


# serach book by the name
def search_book(books):
    search = input("შეიყვანე წიგნის სახელი: ").strip().lower()
    found = False

    if not search:
        print("შეიყვანე წიგნის სახელი")
        return

    for book in books:
        if search in book.title.lower():
            found = True

            if book.available:
                status = "ხელმისაწვდომი"
            else:
                status = "გაცემული"

            print(f"ID: {book.id} | {book.title} | "
                  f"{book.author} | {book.year} | {status}")

    if not found:
        print("წიგნი ვერ მოიძებნა")


# borrow a book
def borrow_book(books):
    try:
        book_id = int(input("შეიყვანე წიგნის ID: "))
    except ValueError:
        print("ID უნდა იყოს რიცხვი")
        return

    for book in books:
        if book.id == book_id:
            if book.available:
                book.available = False
                print("წიგნი გაიცა!")
            else:
                print("წიგნი უკვე გაცემულია!")
            return

    print("წიგნი ვერ მოიძებნა!")


# return a book
def return_book(books):
    try:
        book_id = int(input("შეიყვანე წიგნის ID: "))
    except ValueError:
        print("ID უნდა იყოს რიცხვი")
        return

    for book in books:
        if book.id == book_id:
            book.available = True
            print("წიგნი დაბრუნებულია!")
            return

    print("წიგნი ვერ მოიძებნა!")


# library stats
def statistics(books):
    total = len(books)
    available = 0

    for book in books:
        if book.available:
            available += 1

    borrowed = total - available

    print(f"სულ წიგნები: {total}")
    print(f"ხელმისაწვდომი: {available}")
    print(f"გაცემული: {borrowed}")


def main():
    books = load_books()

    while True:
        print()
        print("1. წიგნის დამატება")
        print("2. ყველა წიგნის ნახვა")
        print("3. წიგნის ძებნა სახელით")
        print("4. წიგნის გატანა")
        print("5. წიგნის დაბრუნება")
        print("6. სტატისტიკა")
        print("7. მონაცემების შენახვა")
        print("8. გამოსვლა")

        choice = input("აირჩიე მოქმედება: ")

        if choice == "1":
            add_book(books)
        elif choice == "2":
            show_books(books)
        elif choice == "3":
            search_book(books)
        elif choice == "4":
            borrow_book(books)
        elif choice == "5":
            return_book(books)
        elif choice == "6":
            statistics(books)
        elif choice == "7":
            save_books(books)
        elif choice == "8":
            print("გამოსვლა")
            break
        else:
            print("მიუთითეთ კოდი ჩამონათვალიდან")

main()