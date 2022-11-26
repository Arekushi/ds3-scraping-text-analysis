from src.model import Entity


class GuardAbsorption(Entity):
    def __int__(self,
                physical: float,
                magic: float,
                fire: float,
                lightning: float,
                dark: float,
                stability: int):
        self.physical = physical
        self.magic = magic
        self.fire = fire
        self.lightning = lightning
        self.dark = dark
        self.stability = stability
