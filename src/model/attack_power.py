from src.model import Entity


class AttackPower(Entity):
    def __int__(self,
                physical: int,
                magic: int,
                fire: int,
                lightning: int,
                dark: int,
                critical: int):
        self.physical = physical
        self.magic = magic
        self.fire = fire
        self.lightning = lightning
        self.dark = dark
        self.critical = critical
