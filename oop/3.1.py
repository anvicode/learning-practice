# Task 1


class Animal:
    def __init__(self, name: str, type: str, age: int, sound: str) -> None:
        self.name: str = name
        self.type: str = type
        self.age: int = age
        self.sound: str = sound

    def get_sound(self) -> None:
        print(f'"{self.sound}"')

    def get_info(self) -> None:
        print(f"Name: {self.name}")
        print(f"Type: {self.type}")
        print(f"Age: {self.age}")
        print(f"Sound: {self.sound}")


c1: Animal = Animal(name="Cat", type="Domestic", age=2, sound="Meow")

print("Task 1 ----------------------")
c1.get_info()
c1.get_sound()
c1.get_sound()


# Task 2


class Book:
    def __init__(self, title: str, author: str, pages: int) -> None:
        self.title: str = title
        self.author: str = author
        self.pages: int = pages

    def get_page(self, page: int) -> None:
        if page > 0 and page <= self.pages:
            print(f"Page {page} is opened")
        else:
            print(f"Page {page} does not exist")

    def get_info(self) -> None:
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")


b1: Book = Book(title="SICP", author="Wizards", pages=600)

print("\nTask 2 ----------------------")
b1.get_info()
b1.get_page(page=0)
b1.get_page(page=600)
b1.get_page(page=601)
