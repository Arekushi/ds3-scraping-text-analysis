from src.model import Entity


class Skill(Entity):
    def __int__(self,
                name: str,
                fp_cost: str,
                fp_cost_farron_ring: str):
        self.name = name
        self.fp_cost = fp_cost
        self.fp_cost_farron_ring = fp_cost_farron_ring
