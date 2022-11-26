from src.model import Entity


class Attribute(Entity):
    def __int__(self,
                strenght,
                dexterity,
                intelligence,
                faith):
        self.strenght = strenght
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.faith = faith
