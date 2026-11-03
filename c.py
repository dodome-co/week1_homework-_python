for i in range(2,40):
    if any((i % n) == 0 for n in range(2, i)):
        continue 
    else:
        print(i)
#リストで表示する方法がわからない




