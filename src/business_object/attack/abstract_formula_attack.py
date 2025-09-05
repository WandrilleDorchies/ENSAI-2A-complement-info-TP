from abc import abstractmethod

from business_object.attack.abstract_attack import AbstractAttack


class AbstractFormulaAttack(AbstractAttack):
    @abstractmethod
    def get_attack_stat(self, APkm, APkm):
        pass

    @abstractmethod
    def get_defense_stat(self, APkm, APkm):
        pass

    def compute_damage(self, APkm, APkm):
        pass
