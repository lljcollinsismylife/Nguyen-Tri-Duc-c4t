from turtle import*

speed(0)
color = ["red", "blue", "brown", "yellow", "gray"]

for i in range(5):
    pencolor(color[i])
    side = i + 3
    for _ in range(side):
        forward(100)
        left(360 / side)
mainloop()