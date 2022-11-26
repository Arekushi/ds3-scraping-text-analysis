from src.model import Entity


class Miscellaneous(Entity):
    def __int__(self,
                range_value: float,
                spell_buff: float,
                durability: float,
                weight: float):
        self.range_value = range_value
        self.spell_buff = spell_buff
        self.durability = durability
        self.weight = weight
