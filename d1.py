class Fighter:
    def __init__(self, name,hp,attack, defense,):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def super_siyan(self):
        return self.attack * 2

goku = ("悟空", 1000, 100, 50)
vegita = ("ベジータ", 1000, 80, 100)
