number_list=[]
for number in range(2,41):
    if any((number % n) == 0 for n in range(2, number)):
        continue 
    else:
        number_list.append(number)
print(number_list)
