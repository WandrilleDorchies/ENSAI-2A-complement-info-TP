from business_object.attack.abstract_attack import AbstractAttack
from business_object.pokemon.abstract_pokemon import AbstractPokemon


class FixedDamageAttack(AbstractAttack):
    def compute_damage(self, APkm1: AbstractPokemon, Apkm2: AbstractPokemon):
        return self._power
