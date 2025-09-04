import random
from turtle import Screen,Turtle
width,height=400,400
colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "black",'indigo']
def n():
    count=0
    while True:
        count=input('How Many Turtle You Want To Race:')
        if count.isdigit():
            count=int(count)
        else:
            print('Please enter a numeric value between 2 t0 10:')
            continue
        if 2<=count<=10:
            return count
        else:
            print('invalid input range')
turtles=n()
print(turtles)
s1 = Screen()
s1.setup(400,400)

x=width//(turtles+1)
turtle_list=[]
for i in range(1,turtles+1):
    t1=Turtle()
    t1.shape('turtle')
    t1.left(90)
    t1.color(colors[i-1])
    t1.penup()
    t1.goto(-width//2+(i*x),-height//2+10)
    turtle_list.append(t1)

def race():
    flag=True
    while flag:
        for turtle in turtle_list:
            distance=random.randrange(1,20)
            turtle.forward(distance)
            a,b=turtle.pos()
            if b>=(height//2)-40:
                print(f'the winner is {turtle.pencolor()} turtle')
                flag=False

race()
s1.exitonclick()
