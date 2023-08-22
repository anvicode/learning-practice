""" 1.1
Classes for editing modes in emacs and variety of major and minor instances of modes.
- emacs
    - class
        - major editing mode
            - instance
                - Lisp mode
                - Python mode
                - Haskell mode
    - class
        - minor editing modes
            - instance
                - Eldoc mode
                - Flyspell mode
                - Auto-fill mode

Class sidebar icons is a template for variety of instances of icons and 
class bottom panel is a template for variety of instances of bottom panels
- vs code
    - class
        - sidebar icons
            - instance
                - search
                - debug
                - test
    - class
        - bottom panel
            - instance
                - input data
                - terminal
                - debug console

Class tab is a template for variety of instances of tabs and 
class bookmark is a template for variety of instances of bookmarks
- brave browser
    - class
        - tab
            - instance
                - new tab (url)
    - class
        - bookmark
            - instance
                - new bookmark (url)
"""

""" 1.2 """


# py.1.02 -> py.1.03
# py.1.03 -> add constructors to classes and three methods for each class
# py.1.03 -> i need to add new class attributes based on methods
# when designing classes: methods first


# BEGIN class Dwarf
class Dwarf:
    def __init__(
        self,
        name: str,
        age: int,
        gender: str,
        height: float,
        weight: float,
        hair_color: str,
        eye_color: str,
        speed: float,
        health: float,
        hunger: float,
        thirst: float,
    ) -> None:
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__height = height
        self.__weight = weight
        self.__hair_color = hair_color
        self.__eye_color = eye_color
        self.__speed = speed
        self.__health = health
        self.__hunger = hunger
        self.__thirst = thirst

    # BEGIN getter/setter
    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_age(self) -> int:
        return self.__age

    def set_age(self, age: int) -> None:
        self.__age = age

    def get_gender(self) -> str:
        return self.__gender

    def set_gender(self, gender: str) -> None:
        self.__gender = gender

    def get_height(self) -> float:
        return self.__height

    def set_height(self, height: float) -> None:
        self.__height = height

    def get_weight(self) -> float:
        return self.__weight

    def set_weight(self, weight: float) -> None:
        self.__weight = weight

    def get_hair_color(self) -> str:
        return self.__hair_color

    def set_hair_color(self, hair_color: str) -> None:
        self.__hair_color = hair_color

    def get_eye_color(self) -> str:
        return self.__eye_color

    def set_eye_color(self, eye_color: str) -> None:
        self.__eye_color = eye_color

    def get_speed(self) -> float:
        return self.__speed

    def set_speed(self, speed: float) -> None:
        self.__speed = speed

    def get_health(self) -> float:
        return self.__health

    def set_health(self, health: float) -> None:
        self.__health = health

    def get_hunger(self) -> float:
        return self.__hunger

    def set_hunger(self, hunger: float) -> None:
        self.__hunger = hunger

    def get_thirst(self) -> float:
        return self.__thirst

    def set_thirst(self, thirst: float) -> None:
        self.__thirst = thirst

    # END getter/setter

    def Speak(self, speech: str) -> str:
        return f"{self.get_name()} is speaking: {speech}"

    def Move(self, speed: float) -> None:
        self.__speed = speed
        self.__weight -= 0.5
        self.__hunger += 1
        self.__thirst += 2

    def Stop(self) -> None:
        self.__speed = 0

    def Eat(self) -> None:
        if self.__health < 100:
            self.__health += 1
        self.__weight += 0.5
        self.__hunger -= 1

    def Drink_water(self) -> None:
        if self.__health < 100:
            self.__health += 1
        self.__thirst -= 1

    def Receive_damage(self, damage: float) -> None:
        self.__health -= damage


Dwarf_Johnny = Dwarf("Johnny", 29, "male", 102, 85, "black", "hazel", 0, 100, 0, 0)

print(f"Dwarf: {Dwarf_Johnny.get_name()}")
print(f"Age: {Dwarf_Johnny.get_age()}")
print(f"Gender: {Dwarf_Johnny.get_gender()}")
print(f"Height: {Dwarf_Johnny.get_height()}")
print(f"Weight: {Dwarf_Johnny.get_weight()}")
print(f"Hair color: {Dwarf_Johnny.get_hair_color()}")
print(f"Eye color: {Dwarf_Johnny.get_eye_color()}")
print(f"Health: {Dwarf_Johnny.get_health()}")
print(f"Hunger: {Dwarf_Johnny.get_hunger()}")
print(f"Thirst: {Dwarf_Johnny.get_thirst()}")
print(f"{Dwarf_Johnny.Speak('Hello')}")

Dwarf_Johnny.Move(100)
print(f"{Dwarf_Johnny.get_name()}'s state has changed:")
print(f"Speed: {Dwarf_Johnny.get_speed()}")
print(f"Weight: {Dwarf_Johnny.get_weight()}")
print(f"Hunger: {Dwarf_Johnny.get_hunger()}")
print(f"Thirst: {Dwarf_Johnny.get_thirst()}")
Dwarf_Johnny.Stop()
Dwarf_Johnny.Receive_damage(10)
print(f"{Dwarf_Johnny.get_name()}'s state has changed:")
print(f"Speed: {Dwarf_Johnny.get_speed()}")
Dwarf_Johnny.Eat()
Dwarf_Johnny.Drink_water()
print(f"{Dwarf_Johnny.get_name()}'s state has changed:")
print(f"Health: {Dwarf_Johnny.get_health()}")
print(f"Hunger: {Dwarf_Johnny.get_hunger()}")
print(f"Thirst: {Dwarf_Johnny.get_thirst()}")


Dwarf_Stella = Dwarf("Stella", 25, "female", 90, 50, "brown", "hazel", 0, 100, 0, 0)

print()
print(f"Dwarf: {Dwarf_Stella.get_name()}")
print(f"Age: {Dwarf_Stella.get_age()}")
print(f"Gender: {Dwarf_Stella.get_gender()}")
print(f"Height: {Dwarf_Stella.get_height()}")
print(f"Weight: {Dwarf_Stella.get_weight()}")
print(f"Hair color: {Dwarf_Stella.get_hair_color()}")
print(f"Eye color: {Dwarf_Stella.get_eye_color()}")
print(f"Health: {Dwarf_Stella.get_health()}")
print(f"Hunger: {Dwarf_Stella.get_hunger()}")
print(f"Thirst: {Dwarf_Stella.get_thirst()}")
print(f"{Dwarf_Stella.Speak(f'Hello, {Dwarf_Johnny.get_name()}!')}")


""" 1.3 BEGIN """
d2 = Dwarf("Lily", 25, "female", 90, 50, "brown", "hazel", 0, 100, 0, 0)
# d2.name = "Lily"
d2.set_name("Lily")

print()
print(d2.get_name())  # d2.name = "Lily"

d3 = d2  # assign d2 to d3

# d3.name = "Hope"  # change d3.name to "Hope"
d3.set_name("Hope")  # change d3.name to "Hope"

print(d2.get_name())  # must be "Lily", but it is "Hope"
print(d3.get_name())  # Hope
""" 1.3 END """
# END class Dwarf


# BEGIN class Weapon
class Weapon:
    def __init__(
        self,
        title: str,
        title_in_dwarven: str,
        title_in_elvish: str,
        title_in_goblin: str,
        title_in_human: str,
        type_of_weapon: str,
        type_of_damage: str,
        rarity: str,
        damage: float,
        sharpening: float,
        enchantment: float,
        encrustment: str = "None",
    ) -> None:
        self.title = title
        self.title_in_dwarven = title_in_dwarven
        self.title_in_elvish = title_in_elvish
        self.title_in_goblin = title_in_goblin
        self.title_in_human = title_in_human
        self.type_of_weapon = type_of_weapon
        self.type_of_damage = type_of_damage
        self.rarity = rarity
        self.damage = damage
        self.sharpening = sharpening
        self.enchantment = enchantment
        self.encrustment = encrustment

    def Sharpen(self, value: float) -> None:
        self.sharpening += value
        self.damage += value / 2

    def Enchant(self, value: float) -> None:
        self.enchantment += value
        self.damage += value / 2

    def Encrust(self, value: str) -> None:
        self.encrustment = value


w1 = Weapon(
    "Morningstar",
    "sanád-vîr",
    "rifa-ila",
    "smungras-ex",
    "sabu-ama",
    "Edged",
    "Piercing",
    "Rare",
    11,
    0,
    0,
)

print()
print(f"Title: {w1.title}")
print(f"Title in dwarven: {w1.title_in_dwarven}")
print(f"Title in elvish: {w1.title_in_elvish}")
print(f"Title in goblin: {w1.title_in_goblin}")
print(f"Title in human: {w1.title_in_human}")
print(f"Type of weapon: {w1.type_of_weapon}")
print(f"Type of damage: {w1.type_of_damage}")
print(f"Rarity: {w1.rarity}")
print(f"Damage: {w1.damage}")
print(f"Sharpening: {w1.sharpening}")
print(f"Enchantment: {w1.enchantment}")
print(f"Encrustment: {w1.encrustment}")

w1.Sharpen(1)

print(f"{w1.title} has been sharpened.")
print(f"Sharpening is now: {w1.sharpening}")
print(f"Damage is now: {w1.damage}")

w1.Enchant(1)

print(f"{w1.title} has been enchanted.")
print(f"Enchantment is now: {w1.enchantment}")
print(f"Damage is now: {w1.damage}")

w1.Encrust("Azure Stone of Power")

print(f"{w1.title} has been encrusted.")
print(f"Encrustment is now: {w1.encrustment}")


w2 = Weapon(
    "Scourge", "abshoth", "fétha", "song", "etuk", "Edged", "Slashing", "Rare", 15, 0, 0
)


print()
print(f"Title: {w2.title}")
print(f"Title in dwarven: {w2.title_in_dwarven}")
print(f"Title in elvish: {w2.title_in_elvish}")
print(f"Title in goblin: {w2.title_in_goblin}")
print(f"Title in human: {w2.title_in_human}")
print(f"Type of weapon: {w2.type_of_weapon}")
print(f"Type of damage: {w2.type_of_damage}")
print(f"Rarity: {w2.rarity}")
print(f"Damage: {w2.damage}")
print(f"Sharpening: {w2.sharpening}")
print(f"Enchantment: {w2.enchantment}")
print(f"Encrustment: {w2.encrustment}")

w2.Sharpen(10)

print(f"{w2.title} has been sharpened.")
print(f"Sharpening is now: {w2.sharpening}")
print(f"Damage is now: {w2.damage}")

w2.Enchant(5)

print(f"{w2.title} has been enchanted.")
print(f"Enchantment is now: {w2.enchantment}")
print(f"Damage is now: {w2.damage}")

w2.Encrust("Emerald Tear of Crocodile")
print(f"{w2.title} has been encrusted.")
print(f"Encrustment is now: {w2.encrustment}")
# END class Weapon


# BEGIN class Animal
class Animal:
    def __init__(
        self,
        name: str,
        size: str,
        age: int,
        is_training: bool,
        biome: str,
        variations: str,
        health: float,
        speed: float,
    ) -> None:
        self.name = name
        self.size = size
        self.age = age
        self.is_training = is_training
        self.biome = biome
        self.variations = variations
        self.health = health
        self.speed = speed

    def Move(self, speed: float) -> None:
        self.speed += speed

    def Stop(self) -> None:
        self.speed = 0

    def Receive_damage(self, damage: float) -> None:
        self.health -= damage


a1 = Animal("Fox", "Small", 1, False, "Taiga", "Fox", 100, 0)

print()
print(f"Name: {a1.name}")
print(f"Size: {a1.size}")
print(f"Age: {a1.age}")
print(f"Is training: {a1.is_training}")
print(f"Biome: {a1.biome}")
print(f"Variations: {a1.variations}")
print(f"Health: {a1.health}")
print(f"Speed: {a1.speed}")

a1.Move(10)
print(f"{a1.name}'s speed now {a1.speed}")
a1.Stop()
print(f"{a1.name}'s speed now {a1.speed}")
a1.Receive_damage(50)
print(f"{a1.name}'s health now {a1.health}")

a2 = Animal("Capybara", "Medium", 3, True, "Wetland", "Capybara", 100, 0)


print()
print(f"Name: {a2.name}")
print(f"Size: {a2.size}")
print(f"Age: {a2.age}")
print(f"Is training: {a2.is_training}")
print(f"Biome: {a2.biome}")
print(f"Variations: {a2.variations}")
print(f"Health: {a2.health}")
print(f"Speed: {a2.speed}")

a2.Move(15)
print(f"{a2.name}'s speed now {a2.speed}")
a2.Stop()
print(f"{a2.name}'s speed now {a2.speed}")
a2.Receive_damage(20)
print(f"{a2.name}'s health now {a2.health}")
# END class Animal
