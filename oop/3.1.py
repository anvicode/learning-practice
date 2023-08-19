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


# Task 3
class PassengerPlane:
    def __init__(
        self, brand: str, model: str, capacity: int, altitude: int, speed: int
    ) -> None:
        self.brand: str = brand
        self.model: str = model
        self.capacity: int = capacity
        self.altitude: int = altitude
        self.speed: int = speed

    def takeoff(self) -> None:
        if self.altitude == 0:
            if self.speed >= 400:
                print(f"Plane {self.brand} {self.model} is taking off")
            else:
                print(
                    f"Plane {self.brand} {self.model} has not enough speed for takeoff"
                )
        else:
            print(f"Plane {self.brand} {self.model} is already in the air")

    def landing(self) -> None:
        if self.altitude > 0:
            if self.altitude <= 50:
                if self.speed <= 100:
                    print(f"Plane {self.brand} {self.model} is landing")
                    self.altitude = 0
                    self.speed = 0
                    print(f"Plane {self.brand} {self.model} has landed")
                else:
                    print(
                        f"Plane {self.brand} {self.model} speed is too high for landing"
                    )
            else:
                print(f"Plane {self.brand} {self.model} altitude is too high")
        else:
            print(f"Plane {self.brand} {self.model} is already on the ground")

    def change_altitude(self, value: int) -> None:
        if self.altitude + value > 0:
            self.altitude += value
            print(f"Altitude has changed. Current altitude {self.altitude}")
        else:
            print("Altitude cannot be negative")

    def change_speed(self, value: int) -> None:
        if self.speed + value > 0:
            self.speed += value
            print(f"Speed has changed. Current speed {self.speed}")
        else:
            print("Speed cannot be negative")

    def get_info(self) -> None:
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Capacity: {self.capacity}")
        print(f"Altitude: {self.altitude}")
        print(f"Speed: {self.speed}")


print("\nTask 3 ----------------------")
p1: PassengerPlane = PassengerPlane(
    brand="Boeing", model="747", capacity=500, altitude=0, speed=0
)
p1.get_info()
p1.takeoff()
p1.landing()
p1.change_speed(value=300)
p1.change_speed(value=-10)
p1.change_speed(value=-290)
p1.takeoff()
p1.change_speed(value=111)
p1.takeoff()
p1.change_altitude(value=100)
p1.change_altitude(value=-100)
p1.change_altitude(value=200)
p1.landing()
p1.change_speed(value=-111)
p1.landing()
p1.change_speed(value=-191)
p1.change_altitude(value=-200)
p1.change_altitude(value=-50)
p1.landing()
p1.get_info()


# Task 4


class MusicAlbum:
    def __init__(
        self, artist: str, title: str, genre: str, tracklist: list[str] = []
    ) -> None:
        self.artist: str = artist
        self.title: str = title
        self.genre: str = genre
        self.tracklist: list[str] = tracklist

    def add_track(self, ind: int, track: str) -> None:
        self.tracklist.insert(ind - 1, track)
        print(f'Track "{track}" is added')

    def del_track(self, track: str) -> None:
        if track in self.tracklist:
            self.tracklist.remove(track)
            print(f'Track "{track}" is deleted')
        else:
            print(f'Track "{track}" does not exist')

    def play_track(self, track: str) -> None:
        if track in self.tracklist:
            t: str = "".join([i for i in self.tracklist if i == track])
            print(f'Track "{t}" is playing 🎶 🎶 🎶')
        else:
            print(f'Track "{track}" does not exist')

    def get_info(self) -> None:
        print(f"Artist: {self.artist}")
        print(f"Title: {self.title}")
        print(f"Genre: {self.genre}")
        print("Track list: \n\t{}".format("\n\t".join(self.tracklist)))


print("\nTask 4 ----------------------")
a1: MusicAlbum = MusicAlbum(
    artist="Pink Floyd",
    title="The Dark Side of the Moon",
    genre="Progressive Rock",
    tracklist=[
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse",
    ],
)
a1.get_info()
a1.add_track(ind=10, track="Comfortably Numb")
a1.get_info()
a1.del_track(track="Brain Damage")
a1.get_info()
a1.play_track(track="Time")
a1.play_track(track="The Great Gig in the Sky")
a1.get_info()
