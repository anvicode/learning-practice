from copy import deepcopy
from random import choice

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
        self.__title = title
        self.__title_in_dwarven = title_in_dwarven
        self.__title_in_elvish = title_in_elvish
        self.__title_in_goblin = title_in_goblin
        self.__title_in_human = title_in_human
        self.__type_of_weapon = type_of_weapon
        self.__type_of_damage = type_of_damage
        self.__rarity = rarity
        self.__damage = damage
        self.__sharpening = sharpening
        self.__enchantment = enchantment
        self.__encrustment = encrustment

    # BEGIN getter/setter
    def get_title(self) -> str:
        return self.__title

    def set_title(self, title: str) -> None:
        self.__title = title

    def get_title_in_dwarven(self) -> str:
        return self.__title_in_dwarven

    def set_title_in_dwarven(self, title_in_dwarven: str) -> None:
        self.__title_in_dwarven = title_in_dwarven

    def get_title_in_elvish(self) -> str:
        return self.__title_in_elvish

    def set_title_in_elvish(self, title_in_elvish: str) -> None:
        self.__title_in_elvish = title_in_elvish

    def get_title_in_goblin(self) -> str:
        return self.__title_in_goblin

    def set_title_in_goblin(self, title_in_goblin: str) -> None:
        self.__title_in_goblin = title_in_goblin

    def get_title_in_human(self) -> str:
        return self.__title_in_human

    def set_title_in_human(self, title_in_human: str) -> None:
        self.__title_in_human = title_in_human

    def get_type_of_weapon(self) -> str:
        return self.__type_of_weapon

    def set_type_of_weapon(self, type_of_weapon: str) -> None:
        self.__type_of_weapon = type_of_weapon

    def get_type_of_damage(self) -> str:
        return self.__type_of_damage

    def set_type_of_damage(self, type_of_damage: str) -> None:
        self.__type_of_damage = type_of_damage

    def get_rarity(self) -> str:
        return self.__rarity

    def set_rarity(self, rarity: str) -> None:
        self.__rarity = rarity

    def get_damage(self) -> float:
        return self.__damage

    def set_damage(self, damage: float) -> None:
        self.__damage = damage

    def get_sharpening(self) -> float:
        return self.__sharpening

    def set_sharpening(self, sharpening: float) -> None:
        self.__sharpening = sharpening

    def get_enchantment(self) -> float:
        return self.__enchantment

    def set_enchantment(self, enchantment: float) -> None:
        self.__enchantment = enchantment

    def get_encrustment(self) -> str:
        return self.__encrustment

    def set_encrustment(self, encrustment: str) -> None:
        self.__encrustment = encrustment

    # END getter/setter

    def Sharpen(self, value: float) -> None:
        self.__sharpening += value
        self.__damage += value / 2

    def Enchant(self, value: float) -> None:
        self.__enchantment += value
        self.__damage += value / 2

    def Encrust(self, value: str) -> None:
        self.__encrustment = value


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
print(f"Title: {w1.get_title()}")
print(f"Title in dwarven: {w1.get_title_in_dwarven()}")
print(f"Title in elvish: {w1.get_title_in_elvish()}")
print(f"Title in goblin: {w1.get_title_in_goblin()}")
print(f"Title in human: {w1.get_title_in_human()}")
print(f"Type of weapon: {w1.get_type_of_weapon()}")
print(f"Type of damage: {w1.get_type_of_damage()}")
print(f"Rarity: {w1.get_rarity()}")
print(f"Damage: {w1.get_damage()}")
print(f"Sharpening: {w1.get_sharpening()}")
print(f"Enchantment: {w1.get_enchantment()}")
print(f"Encrustment: {w1.get_encrustment()}")

w1.Sharpen(1)

print(f"{w1.get_title()} has been sharpened.")
print(f"Sharpening is now: {w1.get_sharpening()}")
print(f"Damage is now: {w1.get_damage()}")

w1.Enchant(1)

print(f"{w1.get_title()} has been enchanted.")
print(f"Enchantment is now: {w1.get_enchantment()}")
print(f"Damage is now: {w1.get_damage()}")

w1.Encrust("Azure Stone of Power")

print(f"{w1.get_title()} has been encrusted.")
print(f"Encrustment is now: {w1.get_encrustment()}")


w2 = Weapon(
    "Scourge", "abshoth", "fétha", "song", "etuk", "Edged", "Slashing", "Rare", 15, 0, 0
)


print()
print(f"Title: {w2.get_title()}")
print(f"Title in dwarven: {w2.get_title_in_dwarven()}")
print(f"Title in elvish: {w2.get_title_in_elvish()}")
print(f"Title in goblin: {w2.get_title_in_goblin()}")
print(f"Title in human: {w2.get_title_in_human()}")
print(f"Type of weapon: {w2.get_type_of_weapon()}")
print(f"Type of damage: {w2.get_type_of_damage()}")
print(f"Rarity: {w2.get_rarity()}")
print(f"Damage: {w2.get_damage()}")
print(f"Sharpening: {w2.get_sharpening()}")
print(f"Enchantment: {w2.get_enchantment()}")
print(f"Encrustment: {w2.get_encrustment()}")

w2.Sharpen(10)

print(f"{w2.get_title()} has been sharpened.")
print(f"Sharpening is now: {w2.get_sharpening()}")
print(f"Damage is now: {w2.get_damage()}")

w2.Enchant(5)

print(f"{w2.get_title()} has been enchanted.")
print(f"Enchantment is now: {w2.get_enchantment()}")
print(f"Damage is now: {w2.get_damage()}")

w2.Encrust("Emerald Tear of Crocodile")
print(f"{w2.get_title()} has been encrusted.")
print(f"Encrustment is now: {w2.get_encrustment()}")
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
        self.__name = name
        self.__size = size
        self.__age = age
        self.__is_training = is_training
        self.__biome = biome
        self.__variations = variations
        self.__health = health
        self.__speed = speed

    # BEGIN getter/setter
    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_size(self) -> str:
        return self.__size

    def set_size(self, size: str) -> None:
        self.__size = size

    def get_age(self) -> int:
        return self.__age

    def set_age(self, age: int) -> None:
        self.__age = age

    def get_is_training(self) -> bool:
        return self.__is_training

    def set_is_training(self, is_training: bool) -> None:
        self.__is_training = is_training

    def get_biome(self) -> str:
        return self.__biome

    def set_biome(self, biome: str) -> None:
        self.__biome = biome

    def get_variations(self) -> str:
        return self.__variations

    def set_variations(self, variations: str) -> None:
        self.__variations = variations

    def get_health(self) -> float:
        return self.__health

    def set_health(self, health: float) -> None:
        self.__health = health

    def get_speed(self) -> float:
        return self.__speed

    def set_speed(self, speed: float) -> None:
        self.__speed = speed

    # END getter/setter
    def Move(self, speed: float) -> None:
        self.__speed += speed

    def Stop(self) -> None:
        self.__speed = 0

    def Receive_damage(self, damage: float) -> None:
        self.__health -= damage


a1 = Animal("Fox", "Small", 1, False, "Taiga", "Fox", 100, 0)

print()
print(f"Name: {a1.get_name()}")
print(f"Size: {a1.get_size()}")
print(f"Age: {a1.get_age()}")
print(f"Is training: {a1.get_is_training()}")
print(f"Biome: {a1.get_biome()}")
print(f"Variations: {a1.get_variations()}")
print(f"Health: {a1.get_health()}")
print(f"Speed: {a1.get_speed()}")

a1.Move(10)
print(f"{a1.get_name()}'s speed now {a1.get_speed()}")
a1.Stop()
print(f"{a1.get_name()}'s speed now {a1.get_speed()}")
a1.Receive_damage(50)
print(f"{a1.get_name()}'s health now {a1.get_health()}")

a2 = Animal("Capybara", "Medium", 3, True, "Wetland", "Capybara", 100, 0)


print()
print(f"Name: {a2.get_name()}")
print(f"Size: {a2.get_size()}")
print(f"Age: {a2.get_age()}")
print(f"Is training: {a2.get_is_training()}")
print(f"Biome: {a2.get_biome()}")
print(f"Variations: {a2.get_variations()}")
print(f"Health: {a2.get_health()}")
print(f"Speed: {a2.get_speed()}")

a2.Move(15)
print(f"{a2.get_name()}'s speed now {a2.get_speed()}")
a2.Stop()
print(f"{a2.get_name()}'s speed now {a2.get_speed()}")
a2.Receive_damage(20)
print(f"{a2.get_name()}'s health now {a2.get_health()}")
# END class Animal


# py.1.03 -> py.1.04


class Fish:
    def __init__(
        self, length: float, weight: float, speed: float, water_type: str
    ) -> None:
        self._length = length  # m
        self._weight = weight  # kg
        self._speed = speed  # km/h
        self._water_type = water_type  # fresh or salt

    # BEGIN getter/setter
    def get_length(self) -> float:
        return self._length

    def set_length(self, length: float) -> None:
        self._length = length

    def get_weight(self) -> float:
        return self._weight

    def set_weight(self, weight: float) -> None:
        self._weight = weight

    def get_speed(self) -> float:
        return self._speed

    def set_speed(self, speed: float) -> None:
        self._speed = speed

    def get_water_type(self) -> str:
        return self._water_type

    def set_water_type(self, water_type: str) -> None:
        self._water_type = water_type

    # END getter/setter

    def swim(self, speed: float) -> None:
        self._speed = speed

    def stop_swim(self) -> None:
        self._speed = 0


class Shark(Fish):
    def __init__(
        self,
        length: float,  # m
        weight: float,  # kg
        speed: float,  # km/h
        water_type: str,  # freshwater or saltwater
        is_hunting: bool,  # True or False
        type_of_shark: str,
    ) -> None:
        super().__init__(length, weight, speed, water_type)
        self._is_hunting = is_hunting
        self._type_of_shark = type_of_shark

    # BEGIN getter/setter
    def get_is_hunting(self) -> bool:
        return self._is_hunting

    def set_is_hunting(self, is_hunting: bool) -> None:
        self._is_hunting = is_hunting

    def get_type_of_shark(self) -> str:
        return self._type_of_shark

    def set_type_of_shark(self, type_of_shark: str) -> None:
        self._type_of_shark = type_of_shark

    # END getter/setter

    def hunt(self) -> None:
        self._is_hunting = True
        self._speed = 19

    def stop_hunting(self) -> None:
        self._is_hunting = False

    def ambush(self) -> None:
        if self._is_hunting:
            self._speed = 25
        else:
            self._is_hunting = True
            self._speed = 25


sh1 = Shark(4, 450, 10, "saltwater", False, "Tiger shark")
print()
print(f"Length: {sh1.get_length()}")
print(f"Weight: {sh1.get_weight()}")
print(f"Speed: {sh1.get_speed()}")
print(f"Water type: {sh1.get_water_type()}")
print(f"Is hunting: {sh1.get_is_hunting()}")
print(f"Type of shark: {sh1.get_type_of_shark()}")

sh1.swim(10)
print(f"Speed is {sh1.get_speed()}")
sh1.stop_swim()
print(f"Speed is {sh1.get_speed()}")

sh1.hunt()
print(f"{sh1.get_type_of_shark()} is now hunting")
print(f"Is hunting: {sh1.get_is_hunting()}")
print(f"Speed: {sh1.get_speed()}")

sh1.ambush()
print(f"{sh1.get_type_of_shark()} is in ambush")
print(f"Is hunting: {sh1.get_is_hunting()}")
print(f"Speed: {sh1.get_speed()}")

sh1.stop_hunting()
print(f"{sh1.get_type_of_shark()} is no longer hunting")
print(f"Is hunting: {sh1.get_is_hunting()}")


class Carp(Fish):
    def __init__(
        self,
        length: float,  # m
        weight: float,  # kg
        speed: float,  # km/h
        water_type: str,  # freshwater or saltwater
        type_of_carp: str,
        is_searching_for_food: bool = False,
        is_searching_for_predator: bool = True,
    ) -> None:
        super().__init__(length, weight, speed, water_type)
        self._type_of_carp = type_of_carp
        self._is_searching_for_food = is_searching_for_food
        self._is_searching_for_predator = is_searching_for_predator

    # BEGIN getter/setter
    def get_type_of_carp(self) -> str:
        return self._type_of_carp

    def set_type_of_carp(self, type_of_carp: str) -> None:
        self._type_of_carp = type_of_carp

    def get_is_searching_for_food(self) -> bool:
        return self._is_searching_for_food

    def set_is_searching_for_food(self, is_searching_for_food: bool) -> None:
        self._is_searching_for_food = is_searching_for_food

    def get_is_searching_for_predator(self) -> bool:
        return self._is_searching_for_predator

    def set_is_searching_for_predator(self, is_searching_for_predator: bool) -> None:
        self._is_searching_for_predator = is_searching_for_predator

    # END getter/setter

    def searching_for_seaweed(self) -> None:
        if self._is_searching_for_predator:
            self._is_searching_for_predator = False
            self._is_searching_for_food = True

    def searching_for_predator(self) -> None:
        if self._is_searching_for_food:
            self._is_searching_for_food = False
            self._is_searching_for_predator = True


c1 = Carp(0.5, 5, 6, "freshwater", "Common Carp")
print()
print(f"Length: {c1.get_length()}")
print(f"Weight: {c1.get_weight()}")
print(f"Speed: {c1.get_speed()}")
print(f"Water type: {c1.get_water_type()}")
print(f"Type of carp: {c1.get_type_of_carp()}")
print(f"Is searching for food: {c1.get_is_searching_for_food()}")
print(f"Is searching for predator: {c1.get_is_searching_for_predator()}")

c1.stop_swim()
print(f"Speed is {c1.get_speed()}")
c1.swim(4)
print(f"Speed is {c1.get_speed()}")

c1.searching_for_seaweed()
print(f"{c1.get_type_of_carp()} is now searching for seaweed")
print(f"Is searching for food: {c1.get_is_searching_for_food()}")
print(f"Is searching for predator: {c1.get_is_searching_for_predator()}")

c1.searching_for_predator()
print(f"{c1.get_type_of_carp()} is now searching for predator")
print(f"Is searching for food: {c1.get_is_searching_for_food()}")
print(f"Is searching for predator: {c1.get_is_searching_for_predator()}")


class Aquarium:
    def __init__(
        self,
        length: float,
        width: float,
        height: float,
        water_type: str,
    ) -> None:
        self._length = length  # m
        self._width = width  # m
        self._height = height  # m
        self._water_type = water_type
        self._volume = self._length * self._width * self._height  # m^3
        self._water_level = 0  # %

    # BEGIN getter/setter
    def get_length(self) -> float:
        return self._length

    def get_width(self) -> float:
        return self._width

    def get_height(self) -> float:
        return self._height

    def get_volume(self) -> float:
        return self._volume

    def get_water_type(self) -> str:
        return self._water_type

    def set_water_type(self, water_type: str) -> None:
        self._water_type = water_type

    def get_water_level(self) -> float:
        return self._water_level

    def set_water_level(self, water_level: float) -> None:
        if water_level >= 0 and water_level <= 100:
            self._water_level = water_level

    # END getter/setter

    def fill(self) -> None:
        self._water_level = 100

    def drain(self) -> None:
        self._water_level = 0

    def foo(self) -> None:
        print(self.__class__.__name__)


class Aquarium_for_Shark(Aquarium):
    def __init__(
        self,
        length: float,
        width: float,
        height: float,
        water_type: str,
        salt_level: float,
        fish: list[Shark] = [],
    ) -> None:
        super().__init__(length, width, height, water_type)
        self._salt_level = salt_level  # %
        self._is_current_on = False
        self._fish = fish

    # BEGIN getter/setter
    def get_salt_level(self) -> float:
        return self._salt_level

    def get_is_current_on(self) -> bool:
        return self._is_current_on

    def get_fish(self) -> list[list[str | float]]:
        return [
            [
                i.get_type_of_shark(),
                i.get_length(),
                i.get_weight(),
                i.get_speed(),
                i.get_water_type(),
                i.get_is_hunting(),
            ]
            for i in self._fish
        ]

    # END getter/setter

    def add_salt(self, salt_level: float) -> None:
        self._salt_level += salt_level

    def switch_current(self) -> None:
        if self._is_current_on:
            self._is_current_on = False
        else:
            self._is_current_on = True

    def add_fish(self, fish: Shark) -> None:
        self._fish.append(fish)

    def foo(self) -> None:
        print(self.__class__.__name__)


aq1 = Aquarium_for_Shark(50, 100, 50, "saltwater", 0)


print()
print(f"Length: {aq1.get_length()}")
print(f"Width: {aq1.get_width()}")
print(f"Height: {aq1.get_height()}")
print(f"Volume: {aq1.get_volume()}")
print(f"Water type: {aq1.get_water_type()}")
print(f"Water level: {aq1.get_water_level()}")
print(f"Salt level: {aq1.get_salt_level()}")
print(f"Is current on: {aq1.get_is_current_on()}")
print(f"Fish: {aq1.get_fish()}")
aq1.add_fish(sh1)
aq1.add_fish(Shark(6, 650, 17, "saltwater", False, "Tiger shark"))
aq1.add_fish(Shark(5, 550, 14, "saltwater", False, "Tiger shark"))
print(f"Fish: {aq1.get_fish()}")

aq1.fill()
print(f"Water level: {aq1.get_water_level()}")
aq1.drain()
print(f"Water level: {aq1.get_water_level()}")

aq1.set_water_level(50)
print(f"Water level: {aq1.get_water_level()}")
aq1.add_salt(90)
print(f"Salt level: {aq1.get_salt_level()}")
aq1.switch_current()
print(f"Is current on: {aq1.get_is_current_on()}")


class Aquarium_for_Carp(Aquarium):
    def __init__(
        self,
        length: float,
        width: float,
        height: float,
        water_type: str,
        hardness_of_water: float,
        plants: int,
        fish: list[Carp] = [],
    ) -> None:
        super().__init__(length, width, height, water_type)
        self._hardness_of_water = hardness_of_water  # degrees
        self._plants = plants
        self._fish = fish

    # BEGIN getter/setter
    def get_hardness_of_water(self) -> float:
        return self._hardness_of_water

    def get_plants(self) -> int:
        return self._plants

    def get_fish(self) -> list[list[str | float | bool]]:
        return [
            [
                i.get_type_of_carp(),
                i.get_length(),
                i.get_weight(),
                i.get_speed(),
                i.get_water_type(),
                i.get_is_searching_for_food(),
                i.get_is_searching_for_predator(),
            ]
            for i in self._fish
        ]

    # END getter/setter

    def add_hardness(self, hardness_of_water: float) -> None:
        self._hardness_of_water += hardness_of_water

    def add_plants(self, plants: int) -> None:
        self._plants += plants

    def add_fish(self, fish: Carp) -> None:
        self._fish.append(fish)

    def foo(self) -> None:
        print(self.__class__.__name__)

    def bar(self, *args) -> None:  # type: ignore
        if len(args) == 1:  # type: ignore
            print(*args)  # type: ignore
        elif len(args) == 2:  # type: ignore
            a, b = args  # type: ignore
            if isinstance(a, int) and isinstance(b, int):
                print(a + b)
            elif isinstance(a, float) and isinstance(b, float):
                print(a + b)
            elif isinstance(a, str) and isinstance(b, str):
                print(a + b)
        else:
            print(*args)  # type: ignore


aq2 = Aquarium_for_Carp(20, 50, 20, "freshwater", 0, 0)

print()
print(f"Length: {aq2.get_length()}")
print(f"Width: {aq2.get_width()}")
print(f"Height: {aq2.get_height()}")
print(f"Volume: {aq2.get_volume()}")
print(f"Water type: {aq2.get_water_type()}")
print(f"Water level: {aq2.get_water_level()}")
print(f"Hardness of water: {aq2.get_hardness_of_water()}")
print(f"Plants: {aq2.get_plants()}")
print(f"Fish: {aq2.get_fish()}")
aq2.add_fish(c1)
aq2.add_fish(Carp(0.4, 4, 7, "freshwater", "Common Carp"))
aq2.add_fish(Carp(0.6, 3, 4, "freshwater", "Common Carp"))
print(f"Fish: {aq2.get_fish()}")

aq2.fill()
print(f"Water level: {aq2.get_water_level()}")
aq2.drain()
print(f"Water level: {aq2.get_water_level()}")

aq2.set_water_level(80)
print(f"Water level: {aq2.get_water_level()}")
aq2.add_hardness(20)
print(f"Hardness of water: {aq2.get_hardness_of_water()}")
aq2.add_plants(10)
print(f"Plants: {aq2.get_plants()}")

# BEGIN 1.05 (4.2)
print()
a01 = Aquarium(10, 10, 10, "freshwater")
a02 = Aquarium_for_Shark(10, 10, 10, "saltwater", 0)
a03 = Aquarium_for_Carp(10, 10, 10, "freshwater", 0, 0)
a01.foo()
a02.foo()
a03.foo()

lst = []
for i in range(500):
    lst.append(choice([deepcopy(a02), deepcopy(a03)]))  # type: ignore

print()
print(f"Length: {len(lst)}")
for i in range(len(lst)):
    lst[i].foo()  # type: ignore
    print(id(lst[i]))  # type: ignore

# i have overridden the parent "foo" method in each child class,
# so each object runs its own "foo" method

# END 1.05 (4.2)


# BEGIN 1.05 (4.3)
# there is not ad hoc polymorphism in Python
# but i can use condition statements in the method
# to change the behavior depending on the arguments

print()
a03.bar("bar")  # type: ignore
# => bar

a03.bar("bar", "foo")  # type: ignore
# => barfoo

a03.bar(2, 2)  # type: ignore
# => 4

a03.bar(2, 2, 3)  # type: ignore
# => 2, 2, 3

# END 1.05 (4.3)
