import turtle

#画正方形的函数
def draw_square(some_turtle):
    turn =10
    for times in range(0, 19):
        turn = turn + 0              #更换每一次的角度
        for speed in range(0,4):
            some_turtle.forward(100)
            some_turtle.right(90)
        some_turtle.right(turn)

def draw_circle(c1):
    n = 50
    for times in range(1, 7):
        c1.circle(n)       #半径
        n = n + 10

#绘画函数
def draw_art():
    window = turtle.Screen() #添加一个窗口
    window.bgcolor("white")    #窗口颜色是红色
    #Create the turtle Brad - Draws a aquare
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("black")
    brad.speed(20)
    #画三角的函数
    circle = turtle.Turtle()
    circle.shape("arrow")
    circle.color("blue")
    circle.speed(20)

    draw_square(brad)
    draw_circle(circle)

    window.exitonclick()     #窗口点击关闭

draw_art()