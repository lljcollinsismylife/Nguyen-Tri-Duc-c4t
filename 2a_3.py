# Part a

print(*range(20))
number = int(input("enter a positive interger:" ))
print(*range(number))

# part b
listofnumber = [1, 0]

print(*(listofnumber * 10))

time = int(input("How many time do u want the list to repeat?:"))

for i in range(1, time + 1)
    if i % 2 == 1:
        print(1, end=" ")
    else:
        print(0, end=" ")

