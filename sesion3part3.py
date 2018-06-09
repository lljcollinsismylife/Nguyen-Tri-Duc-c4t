number = [1, 6, 8, 1, 2 ,1 , 5, 6]
chosen_number = int(input("What number?"))

print(chosen_number, " appears ", number.count(chosen_number)," times in my list")



timeappear = 0
for i in number:
    if i == chosen_number:
        timeappear +=1
    else:
        a = 1
print(chosen_number, "appears", timeappear, "times in my list")