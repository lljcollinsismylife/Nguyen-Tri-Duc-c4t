from turtle import*
speed(0)
pencolor("red")
right(30)

for _ in range(4):
    for i in range(4):
        forward(100)
        multi = i % 2 + 1
        left(60 * multi)
    left(90)

mainloop()