"""問題
classでPokemonの属性を定義します。

属性はname,hp,attack,deffense,speedです。
１体目の属性は、それぞれ順に、ピカチュウ、60、40、40、 70です。
２体目の属性は、同様に、コラッタ、80、 50、 30、 60です。

「やせいのコラッタがとびだしてきた！」
「いけ！ピカチュウ！」
と表示します。
次に素早さを比較し、
「XXはXXよりすばやさがうえだ」
と表示します。

メソッドで「たいあたり(taiatari)」を定義します。
ダメージは「自分の attack − 相手の defense」。
相手の hp からダメージを引き（0 より小さくはしない）、実行例のように結果を表示します。

すばやさの早い方をfirst、遅い方をsecoundとし、
順番に攻撃するようにします。

各ターンの最初に、--- ターン1 --- のようにターン数を表示します。
１体目→２体目の順に交互に攻撃します。
「【１（ポケモンの名前）】のたいあたり！【２（ポケモンの名前）】に【３（数字）】のダメージ！（【２】のHP：【４（数字）】）」
と表示します。
コラッタが勝利した場合「ピカチュウはたおれた！めのまえがまっくらになった」と表示します。
ピカチュウが勝利した場合「コラッタはたおれた！ピカチュウはけいけんちをかくとくした」と表示します。

"""

class Pokemon:
    def __init__(self, name,hp,attack, defense,speed):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed

    def taiatari(self,opponent):
        damage = self.attack - opponent.defense
        opponent.hp -= damage
        opponent.hp = max(opponent.hp, 0)

        return damage


pikachu = Pokemon("ピカチュウ", 60, 40,40, 70)
koratta = Pokemon("コラッタ", 80, 50, 30, 60)


print(f"やせいの{koratta.name}がとびだしてきた")
print(f"いけ！{pikachu.name}！")

if pikachu.speed > koratta.speed:
    first = pikachu
    secound = koratta
    print(f"{pikachu.name}は{koratta.name}よりすばやさがうえだ")
else:
    first = koratta
    secound = pikachu
    print(f"{koratta.name}は{pikachu.name}よりすばやさがうえだ")

turn = 1
while True:
    print(f"--- ターン{turn} ---")
    if secound.hp > 0:
        damage= first.taiatari(secound)
        print(f"{first.name} のたいあたり！ {secound.name} に{damage}のダメージ！（{secound.name}のHP：{secound.hp}）")
    if first.hp > 0:
        damage = secound.taiatari(first)
        print(f"{secound.name} のたいあたり！ {first.name} に{damage}のダメージ！（{first.name}のHP：{first.hp}）")
    
    if koratta.hp <= 0:
        print(f"{koratta.name}はたおれた！{pikachu.name}はけいけんちをかくとくした")
        break
    if pikachu.hp <= 0:
        print(f"{pikachu.name}はたおれた！めのまえがまっくらになった")
        break
    
    turn += 1
