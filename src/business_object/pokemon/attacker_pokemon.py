from abstract_pokemon import AbstractPokemon


class AttackPokemon(AbstractPokemon):
    @classmethod
    def get_pokemon_attack_coef(self) -> float:
        multiplier = 1 + (self.speed_current + self.attack_current) / 200
        return multiplier
        