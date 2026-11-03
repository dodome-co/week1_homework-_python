name = input("名前を入力してください:")
birth_day =input("xxxx/xx/xxの形で生年月日を入力してください:")

print(name)
birth_day_number =birth_day.split("/")
total_birth_day_number = int(birth_day_number[0])+int(birth_day[1])+int(birth_day_number[2])
for char in name:
    char=[]
lucky_number = len(char) + total_birth_day_number

#・や「　」を数えないコマンドがわからない

if lucky_number % 6 == 0:
    print(f"{name}さんの運勢：大吉")
elif lucky_number % 3 == 0:
    print(f"{name}さんの運勢：中吉")
elif lucky_number % 2 == 0:
    print(f"{name}さんの運勢：吉")
else:
    print(f"{name}さんの運勢：凶")
