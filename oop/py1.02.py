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
    ) -> None:
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.hair_color = hair_color
        self.eye_color = eye_color


Dwarf_Johnny = Dwarf("Johnny", 29, "male", 102, 85, "black", "hazel")

print(f"Dwarf: {Dwarf_Johnny.name}")
print(f"Age: {Dwarf_Johnny.age}")
print(f"Gender: {Dwarf_Johnny.gender}")
print(f"Height: {Dwarf_Johnny.height}")
print(f"Weight: {Dwarf_Johnny.weight}")
print(f"Hair color: {Dwarf_Johnny.hair_color}")
print(f"Eye color: {Dwarf_Johnny.eye_color}")

Dwarf_Stella = Dwarf("Stella", 25, "female", 90, 50, "brown", "hazel")

print()
print(f"Dwarf: {Dwarf_Stella.name}")
print(f"Age: {Dwarf_Stella.age}")
print(f"Gender: {Dwarf_Stella.gender}")
print(f"Height: {Dwarf_Stella.height}")
print(f"Weight: {Dwarf_Stella.weight}")
print(f"Hair color: {Dwarf_Stella.hair_color}")
print(f"Eye color: {Dwarf_Stella.eye_color}")


""" 1.3 BEGIN """
d2 = Dwarf("Lily", 25, "female", 90, 50, "brown", "hazel")
d2.name = "Lily"

print()
print(d2.name)  # d2.name = "Lily"

d3 = d2  # assign d2 to d3

d3.name = "Hope"  # change d3.name to "Hope"

print(d2.name)  # must be "Lily", but it is "Hope"
print(d3.name)  # Hope
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

w2 = Weapon(
    "Scourge", "abshoth", "fétha", "song", "etuk", "Edged", "Slashing", "Rare", 15
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
    ) -> None:
        self.name = name
        self.size = size
        self.age = age
        self.is_training = is_training
        self.biome = biome
        self.variations = variations


a1 = Animal("Fox", "Small", 1, False, "Taiga", "Fox")

print()
print(f"Name: {a1.name}")
print(f"Size: {a1.size}")
print(f"Age: {a1.age}")
print(f"Is training: {a1.is_training}")
print(f"Biome: {a1.biome}")
print(f"Variations: {a1.variations}")

a2 = Animal("Capybara", "Medium", 3, True, "Wetland", "Capybara")


print()
print(f"Name: {a2.name}")
print(f"Size: {a2.size}")
print(f"Age: {a2.age}")
print(f"Is training: {a2.is_training}")
print(f"Biome: {a2.biome}")
print(f"Variations: {a2.variations}")
# END class Animal
