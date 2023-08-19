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


# BEGIN class Dwarf
class Dwarf:
    name = "Johnny"
    age = 29
    gender = "male"
    height = 102
    weight = 85
    hair_color = "black"
    eye_color = "hazel"


Dwarf_Johnny = Dwarf()

print(f"Dwarf: {Dwarf_Johnny.name}")
print(f"Age: {Dwarf_Johnny.age}")
print(f"Gender: {Dwarf_Johnny.gender}")
print(f"Height: {Dwarf_Johnny.height}")
print(f"Weight: {Dwarf_Johnny.weight}")
print(f"Hair color: {Dwarf_Johnny.hair_color}")
print(f"Eye color: {Dwarf_Johnny.eye_color}")

Dwarf_Stella = Dwarf()

Dwarf_Stella.name = "Stella"
Dwarf_Stella.age = 25
Dwarf_Stella.gender = "female"
Dwarf_Stella.height = 90
Dwarf_Stella.weight = 50
Dwarf_Stella.hair_color = "brown"
Dwarf_Stella.eye_color = "hazel"

print()
print(f"Dwarf: {Dwarf_Stella.name}")
print(f"Age: {Dwarf_Stella.age}")
print(f"Gender: {Dwarf_Stella.gender}")
print(f"Height: {Dwarf_Stella.height}")
print(f"Weight: {Dwarf_Stella.weight}")
print(f"Hair color: {Dwarf_Stella.hair_color}")
print(f"Eye color: {Dwarf_Stella.eye_color}")


""" 1.3 BEGIN """
d2 = Dwarf()
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
    title = "Morningstar"
    title_in_dwarven = "sanád-vîr"
    title_in_elvish = "rifa-ila"
    title_in_goblin = "smungras-ex"
    title_in_human = "sabu-ama"
    type_of_weapon = "Edged"
    type_of_damage = "Piercing"
    rarity = "Common"
    damage = 11


w1 = Weapon()

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

w2 = Weapon()

w2.title = "Scourge"
w2.title_in_dwarven = "abshoth"
w2.title_in_elvish = "fétha"
w2.title_in_goblin = "song"
w2.title_in_human = "etuk"
w2.type_of_weapon = "Edged"
w2.type_of_damage = "Slashing"
w2.rarity = "Rare"
w2.damage = 15

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
    name = "Fox"
    size = "Small"
    age = 1
    is_training = False
    biome = "Taiga"
    variations = "Fox"


a1 = Animal()

print()
print(f"Name: {a1.name}")
print(f"Size: {a1.size}")
print(f"Age: {a1.age}")
print(f"Is training: {a1.is_training}")
print(f"Biome: {a1.biome}")
print(f"Variations: {a1.variations}")

a2 = Animal()

a2.name = "Capybara"
a2.size = "Medium"
a2.age = 3
a2.is_training = False
a2.biome = "Wetland"
a2.variations = "Capybara"

print()
print(f"Name: {a2.name}")
print(f"Size: {a2.size}")
print(f"Age: {a2.age}")
print(f"Is training: {a2.is_training}")
print(f"Biome: {a2.biome}")
print(f"Variations: {a2.variations}")
# END class Animal
