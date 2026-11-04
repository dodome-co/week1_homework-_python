class Fighter:
    def __init__(self, name,hp,attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def super_saiyan(self):
        self.attack = self.attack * 2
    

    def punch(self,opponent):
        damage = self.attack - opponent.defense
        opponent.hp -= damage
        if opponent.hp < 0:
            opponent.hp = 0

        return damage
        
goku = Fighter("悟空", 1000, 100, 50)
vegita = Fighter("ベジータ", 1000, 80, 100)


turn = 1
goku.super_saiyan()
print(f"{goku.name}はスーパーサイヤ人に変身した！")

while True:
    print(f"--- ターン{turn} ---")
    if vegita.hp > 0:
        damage= goku.punch(vegita)
        print(f"{goku.name} の攻撃！ {vegita.name} に{damage}のダメージ！（{vegita.name}のHP：{vegita.hp}）")
        if vegita.hp <= 0:
            print(f"{vegita.name}は倒れた！{goku.name}の勝利")
            break
    if goku.hp > 0:
        damage = vegita.punch(goku)
        print(f"{vegita.name} の攻撃！ {goku.name} に{damage}のダメージ！（{goku.name}のHP：{goku.hp}）")
        if goku.hp <= 0:
            print(f"{goku.name}は倒れた！{vegita.name}の勝利")
            break
    turn += 1
