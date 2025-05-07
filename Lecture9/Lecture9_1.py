# UPRM CIIC 3015 Spring 2025
# Lecture 9: Classes

# Live Coding Example 8_1

class Character:
    max_inventory_size = 4
    def __init__(self, name, strength, defense):
        self.name = name
        self.strength = strength
        self.defense = defense
        self.health = 100
        self.alive = True
        self.inventory = []

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return f"Character name = {self.name}"

    def introduce(self):
        print(f"Hi! My name is {self.name}")

    def attack(self, victim):
        damage = self.strength - victim.defense
        if damage >= victim.health:
            victim.health -= damage
        else:
            victim.health = 0
            victim.alive = False
    def store_item(self, item):
        if len(self.inventory) < self.max_inventory_size:
            self.inventory.append(item)
            print(f"Added item {item} to Character {self}")
        else:
            print(f"Cannot add {item} to {self} inventory full")

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)

class SkyCharacter(Character):

    def __init__(self,name, strength, defense, max_alt):
        Character.__init__(self, name, strength, defense)
        self.max_altitude = max_alt

    def perform_action(self):
        print("I can fly")




bienve = Character('Bienve', 50, 10)




