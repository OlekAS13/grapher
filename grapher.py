from tkinter import *

print("y = a x^2 + b x + c")

sx = 20
sy = 20

#inputs
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

print("y =", a, "x^2 +", b, "x +", c)



#main grapher window
graph = Tk()

equation = "y = {} x^2 + {} x + {}".format(a, b ,c)
scaletext = "sx = {}, sy = {}".format(sx, sy)

graph.title("Grapher [OlekAS13] | " + equation)

canv = Canvas(graph, width=801, height=801, background="white")

#sliderX = Scale(graph, from_=0, to=100)
#sliderY = Scale(graph, from_=0, to=100)
#sliderX.pack()
#sliderY.pack()

canv.create_text(796, 796, text=equation, anchor="se", justify="right")
canv.create_text(5, 796, text=scaletext, anchor="sw", justify="left")

xAxis = canv.create_line(0, 400, 800, 400, fill="black")
yAxis = canv.create_line(400, 0, 400, 800, fill="black")

#x cosmetics
canv.create_text(795, 400, text=">")
canv.create_text(795, 415, text="x", anchor="n", justify="left")

#y cosmetics
canv.create_text(400, 7, text="^")
canv.create_text(385, 5, text="y")


#middle
canv.create_text(385, 415, text="0")

#x 1
canv.create_text(400 + sx, 415, text="1")
#y 1
canv.create_text(385, 400 - sy, text="1")



for xSpace in range(0, 800, sx):
    canv.create_line(xSpace, 395, xSpace, 405, fill="black")

for ySpace in range(0, 800, sy):
    canv.create_line(395, ySpace, 405, ySpace, fill="black")


i = 0
x = -400 / sx



while i <= 801:

    y = a * pow(x, 2) + b * x + c

    px = x * sx + 400
    py = -y * sy + 400
    
    canv.create_rectangle((px, py) * 2, outline="blue")

    x += 0.01
    i += 0.01

    #print(i)

canv.pack()
graph.mainloop()

#By OlekAS13
#Nov 11 2024 1:52