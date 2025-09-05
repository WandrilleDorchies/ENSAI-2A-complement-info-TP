from abc import ABC, abstractmethod

from business_object.pokemon.abstract_pokemon import AbstractPokemon


class AbstractAttack(ABC):
    """
    Abstract Attack
    """

    def __init__(self, name: str = "Attack", power: int = 0, description: str = "Description"):
        self._name = name
        self._power = power
        self._description = description

    @abstractmethod
    def compute_damage(self, Pokemon1: AbstractPokemon, Pokemon2: AbstractPokemon) -> int:
        pass

    # getters
    @property
    def power(self):
        return self._power
