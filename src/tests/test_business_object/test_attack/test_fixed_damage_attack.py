from business_object.attack.fixed_damage_attack import FixedDamageAttack
from business_object.pokemon.attacker_pokemon import AttackerPokemon


# a = FixedDamageAttack()
def test_fixed_damage_attack_power():
    fdattack = FixedDamageAttack(power=10)
    res = fdattack.compute_damage(AttackerPokemon(), AttackerPokemon())
    assert res == 10
