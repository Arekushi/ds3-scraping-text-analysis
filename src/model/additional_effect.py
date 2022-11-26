from src.model import Entity


class AdditionalEffect(Entity):
    def __int__(self,
                bleed: int,
                poison: int,
                frost: int):
        self.bleed = bleed
        self.poison = poison
        self.frost = frost
