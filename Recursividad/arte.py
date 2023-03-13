# Name: Ilan Nestor Angeles Rodriguez
# Date: 13/03/23

#Imports
import turtle;
import random;

myTurtle=turtle.Turtle(); #Analogia con tortuga, tiene direccion y sentido, deja rastro
myWin=turtle.Screen();

def draw(myTurtle, length):
    if length>0 :
        myTurtle.forward(length);
        myTurtle.right(90);
        draw(myTurtle, length-10);

colors = (
    '#006699',
    '#006666',
    '#660066',
    '#990000',
    '#ad3270',
    '#e65100',
    '#1a237e',
    '#827717',
    '#006064',
    '#f57f17',
    '#d50000',
    '#4a148c',
)

for color in colors:
    myTurtle.pencolor(color)
    draw(myTurtle, 180)
#draw(myTurtle, 100);
myWin.exitonclick();
