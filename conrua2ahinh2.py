from turtle import*

speed(0)
color = ["blue", "red", "blue", "red", "blue"]
for i in range(5):
     for x in range(i+2):
         pencolor([color])
         fotward(100)
         ledt(360 / (i+2))



mainloop()

