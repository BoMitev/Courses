from pokemon import Pokemon

class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"

        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        pokemons = [x.name for x in self.pokemons]

        if pokemon_name in pokemons:
            self.pokemons.pop(pokemons.index(pokemon_name))
            return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        text = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n" \
        '\n'.join([f"- {x.pokemon_details()}" for x in self.pokemons])
        return text


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
