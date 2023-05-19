""" class Trainer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.pokemon = []
        self.friends = {}

    def talk(self):
        print("Pikachu! I choose you!")

    def attack_pokemon(self, pokemon, target_pokemon):
        print(f"{self.name}'s {pokemon.name} attacks {target_pokemon.name}!")
        pokemon.tackle(target_pokemon)
        if target_pokemon.is_fainted():
            print(f"{target_pokemon.name} has fainted.")
            pokemon.level_up()
            print(f"{pokemon.name} leveled up! New level: {pokemon.level}")


class Pokemon:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.health = self.level * 10
        self.attack = self.level * 2

    def tackle(self, target_pokemon):
        target_pokemon.health -= self.attack

    def is_fainted(self):
        return self.health <= 0

    def level_up(self):
        self.level += 1
        self.health = self.level * 10
        self.attack = self.level * 2


# Create a trainer object using object literals
trainer = Trainer("Ash", 20)

# Initialize/add the trainer object properties
trainer.pokemon = [
    Pokemon("Pikachu", 5),
    Pokemon("Charizard", 10),
    Pokemon("Bulbasaur", 3)
]
trainer.friends = {
    "Brock": ["Onix", "Geodude"],
    "Misty": ["Starmie", "Psyduck"]
}

# Access the trainer object properties using dot notation
print(trainer.name)
print(trainer.age)
print(trainer.pokemon)
print(trainer.friends)

# Invoke the trainer talk method
trainer.talk()

# Invoke the tackle method of one pokemon object
pokemon1 = trainer.pokemon[0]
pokemon2 = trainer.pokemon[1]
pokemon1.tackle(pokemon2)
if pokemon2.is_fainted():
    print(f"{pokemon2.name} has fainted.")
    pokemon1.level_up()
    print(f"{pokemon1.name} leveled up! New level: {pokemon1.level}")

# Invoke the attack_pokemon method to attack another Pokemon
pokemon3 = trainer.pokemon[2]
trainer.attack_pokemon(pokemon3, pokemon1)
 """


class Trainer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.pokemon = []
        self.friends = {}

    def talk(self):
        print("Pikachu! I choose you!")

    def attack_pokemon(self, pokemon, target_pokemon):
        print(f"{self.name}'s {pokemon.name} attacks {target_pokemon.name}!")
        pokemon.tackle(target_pokemon)
        if target_pokemon.is_fainted():
            print(f"{target_pokemon.name} has fainted.")
            pokemon.level_up()
            print(f"{pokemon.name} leveled up! New level: {pokemon.level}")
        pokemon.show_status()


class Pokemon:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.health = self.level * 10
        self.attack = self.level * 2

    def tackle(self, target_pokemon):
        target_pokemon.health -= self.attack

    def is_fainted(self):
        return self.health <= 0

    def level_up(self):
        self.level += 1
        self.health = self.level * 10
        self.attack = self.level * 2

    def show_status(self):
        print(f"Name: {self.name}")
        print(f"Level: {self.level}")
        print(f"Health: {self.health}")
        print(f"Attack: {self.attack}")
        print("---------------")


# Create a trainer object using object literals
trainer = Trainer("Ash", 20)

# Initialize/add the trainer object properties
trainer.pokemon = [
    Pokemon("Pikachu", 5),
    Pokemon("Charizard", 10),
    Pokemon("Bulbasaur", 3)
]
trainer.friends = {
    "Brock": ["Onix", "Geodude"],
    "Misty": ["Starmie", "Psyduck"]
}

# Access the trainer object properties using dot notation
print(trainer.name)
print(trainer.age)
print(trainer.pokemon)
print(trainer.friends)

# Invoke the trainer talk method
trainer.talk()

# Invoke the tackle method of one pokemon object
pokemon1 = trainer.pokemon[0]
pokemon2 = trainer.pokemon[1]
pokemon1.tackle(pokemon2)
if pokemon2.is_fainted():
    print(f"{pokemon2.name} has fainted.")
    pokemon1.level_up()
    print(f"{pokemon1.name} leveled up! New level: {pokemon1.level}")
pokemon1.show_status()

# Invoke the attack_pokemon method to attack another Pokemon
pokemon3 = trainer.pokemon[2]
trainer.attack_pokemon(pokemon3, pokemon1)
