from tkinter import *

sx = 20
sy = 20

def askFuncType():
    global funcType

    funcType = str(input("Function type (linear: y = a x + b, quadratical: y = a x^2 + b x + c): L/Q: "))

def askScale():
    global sx, sy

    sx = int(input("Scale X (How many digits will be between the spacers; 20 is default): INT: "))
    sy = int(input("Scale Y (How many digits will be between the spacers; 20 is default): INT: "))

def drawGraph():
    global xAxis, yAxis, newScale
#main grapher window
    graph = Tk()

    if funcType == "Q":
        equation = "y = {} x^2 + {} x + {}".format(a, b ,c)
    elif funcType == "L":
        equation = "y = {} x + {}".format(a, b)

    scaletext = "sx = {}, sy = {}".format(sx, sy)

    if funcType == "Q":
        graph.title("Grapher [OlekAS13] | " + equation + " | QUADRATICAL")
    elif funcType == "L":
        graph.title("Grapher [OlekAS13] | " + equation + " | LINEAR")

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

    #spacers
    for xSpace in range(0, 800, sx):
        canv.create_line(xSpace, 395, xSpace, 405, fill="black")

    for ySpace in range(0, 800, sy):
        canv.create_line(395, ySpace, 405, ySpace, fill="black")

    #buttons
    #Button(graph, text="New scale", comman=askScale, width=10, background="white", highlightbackground="gray",).pack()


    i = 0
    x = -400 / sx


    if funcType == "Q":
        while i <= 801:
            y = a * pow(x, 2) + b * x + c

            px = x * sx + 400
            py = -y * sy + 400
            
            canv.create_rectangle((px, py) * 2, outline="blue")

            x += 0.01
            i += 0.01
        
        canv.pack()

    elif funcType == "L":
        while i <= 801:
            y = a * x + b

            px = x * sx + 400
            py = -y * sy + 400
            
            canv.create_rectangle((px, py) * 2, outline="blue")

            x += 0.01
            i += 0.01
        
        canv.pack()

    graph.mainloop()


def main():
    global a, b, c

    askFuncType()

    if funcType == "Q":
        askScale()

        print("y = a x^2 + b x + c")

        #inputs
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))

        print("y =", a, "x^2 +", b, "x +", c)
        
        drawGraph()
        
    elif funcType == "L":
        askScale()

        print("y = a x + b")

        #inputs
        a = float(input("a = "))
        b = float(input("b = "))

        print("y =", a, "x +", b)
        
        drawGraph()

    else:
        print("Please specify a correct function type.")
        main()


main()


#By OlekAS13
#Nov 11 2024 1:52