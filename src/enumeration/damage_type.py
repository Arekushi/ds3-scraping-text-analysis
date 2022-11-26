from enum import Enum


class DamageType(str, Enum):
    BLEED = 'bleed'
    FIRE = 'fire'
    LIGHTNING = 'lightning'
    MAGIC = 'magic'
    POISON = 'poison'
    TOXIC = 'toxic'
    REGULAR = 'regular'
    SLASH = 'slash'
    STRIKE = 'strike'
    THRUST = 'thrust'
