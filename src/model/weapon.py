from typing import List
from src.enumeration import WeaponCategory, DamageType
from src.model import Skill, AttackPower, GuardAbsorption, \
    AdditionalEffect, Miscellaneous, Attribute, Entity


class Weapon(Entity):
    def __int__(self,
                name: str,
                category: WeaponCategory,
                attack_type: List[DamageType],
                purchasing_value: int,
                soul_value: int,
                skill: Skill,
                attack_power: AttackPower,
                guard_absorption: GuardAbsorption,
                additional_effects: AdditionalEffect,
                miscellaneous: Miscellaneous,
                attribute_bonus: Attribute,
                attribute_requirement: Attribute,
                game_description: str,
                availability: str,
                characteristics: str,
                moveset: List[List[str]],
                notes: List[str],
                trivia: List[str]):
        self.name = name
        self.category = category
        self.attack_type = attack_type
        self.purchasing_value = purchasing_value
        self.soul_value = soul_value
        self.skill = skill
        self.attack_power = attack_power
        self.guard_absorption = guard_absorption
        self.additional_effects = additional_effects
        self.miscellaneous = miscellaneous
        self.attribute_bonus = attribute_bonus
        self.attribute_requirement = attribute_requirement
        self.game_description = game_description
        self.availability = availability
        self.characteristics = characteristics
        self.moveset = moveset
        self.notes = notes
        self.trivia = trivia
