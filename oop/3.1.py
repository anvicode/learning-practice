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
