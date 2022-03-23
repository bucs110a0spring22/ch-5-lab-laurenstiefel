'''
Estimates pi using Monte Carlo simulation

Virtual Dartboard has area 2 X 2 to accommodate unit circle
Total area is 4
Therefore, since area of unit circle = pi * radius^2 (and radius of 1 squared
  is 1), ratio of area of unit circle to area of board should be pi/4
  Theoretically, if you fill the entire board with darts, counting
  the number of darts that fall within the circle divided by the
  total number of darts thrown should give us that ratio (i.e., 1/4 * pi)
  Therefore, multiplying that result by 4 should give us an approx. of pi

Output to monitor:
  approximation of pi (float)
Output to window:
  colored dots that simulate unit circle on 2x2 square
Functions you must implement:
  drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0) - to outline dartboard
  drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0) - to draw axes
  drawCircle(myturtle=None, radius=0) - to draw the circle
  setUpDartboard(myscreen=None, myturtle=None) - to set up the board using the above functions
  isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0) - determine if dot is in circle
  throwDart(myturtle=None)
  playDarts(myturtle=None) - a simulated game of darts between two players
  montePi(myturtle=None, num_darts=0) - simulation algorithm returns the approximation of pi
'''
import turtle
import random
import time

#########################################################
#                   Your Code Goes Below                #
#########################################################

  
  
def drawSquare(myturtle=None, width=0,top_left_x=0, top_left_y=0):
  myturtle.up()
  myturtle.goto(top_left_x,top_left_y)
  myturtle.down()
  for i in range (4):
    myturtle.forward(2)
    myturtle.right(90)
 ''This function draws the line based on the measurements given, and loops it 4 times to create a square
	args: turtle.myturtle,width, top_left_x, top_left_y
	return: None'''


 

def drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0):
  myturtle.up()
  myturtle.goto(x_start,y_start)
  myturtle.down()
  myturtle.goto (x_end,y_end)
''This function draws the axis based on the measurements given
	args: turtle.myturtle,width, x_start, y_start,x_end,y_end
	return: None'''  
def drawCircle(myturtle=None, radius=0):
  myturtle.speed(0)
  myturtle.up()
  myturtle.goto(0,-radius)
  myturtle.down()
  myturtle.circle(radius,steps=360)
''This function draws the circle based on the measurements given
	args: turtle.myturtle,radius
	return: None'''  
  
def setUpDartboard(mywindow,darty):
  mywindow.setworldcoordinates (-1,-1,1,1) 
  drawSquare (darty,2,-1,1)
  drawLine (darty,-1,0,1,0)
  drawLine(darty,0,-1,0,1)
  drawCircle(darty,1)
  darty.up()
''This function calls the drawcircle, square and axis functions to create the total dartboard
	args: mywindow, darty
	return: None'''

def throwDart(myturtle=None):
  x= random.uniform(-1,1)
  y=random.uniform(-1,1)
  myturtle.goto (x,y)
  myturtle.dot(5,"blue")
''This function throws the dart to a random location on the dartboard
	args: turtle.myturtle, x,y
	return: None'''
def isInCircle(myturtle=None,circle_center_x=0,circle_center_y=0, radius= 0):
  if myturtle.distance (circle_center_x,circle_center_y) > 1:
      return False
      
  if myturtle.distance(circle_center_x,circle_center_y) <= 1:
      return True
''This function determines if the dart thrown is in the circle of the dartboard and uses boolean values
	args: turtle.myturtle,circle_center_x,Circle_center_y,radius
	return: true or false'''
def playDarts (myturtle=None):
  player1= 0
  player2=0
  for i in range (10):
    throwDart (myturtle)
    if  isInCircle (myturtle,0,0,1) == True:
      myturtle.dot(5,"blue")
      player1 = player1+1
      
  
    else :
      myturtle.dot (5,"red")
    throwDart (myturtle)
    if  isInCircle (myturtle,0,0,1) == True:
      myturtle.dot(5,"blue")
      player2 = player2+1
      
  
    else :
      myturtle.dot (5,"red")  
  if player1 > player2 :
    winner = "player1"
    print (winner)
  elif player2 >player1:
    winner="player2"
    print (winner)
  else :
    print ("tie")
''This function creates the dart game between two players, alternating turns between them and declaring a winner besed on the number of darts in the circle. Also changes the color of the dart if they are outside the circle of the dartboard
	args: turtle.myturtle,player1,player2
	return: None'''


def montePi (myturtle=None, num_darts=0):
  inside_count= 0 
  for i in range (num_darts):
    throwDart (myturtle)
    if isInCircle (myturtle,0,0,1) :
      inside_count = inside_count+1
      myturtle.dot(5,"blue")
    else :
      myturtle.dot(5,"red")
  pi =(inside_count/num_darts) *4 
  return pi
''This function calculates the value of pi based on the number of darts thrown and the ratio darts inside the circle to the total number of darts thrown
	args: turtle.myturtle,num_darts,inside_count
	return: pi'''
#########################################################
#         Do not alter any code below here              #
#       Your code must work with the main proivided     #
#########################################################
def main():
    # Get number of darts for simulation from user
    # Note continuation character <\> so we don't go over 78 columns:
    print("This is a program that simulates throwing darts at a dartboard\n" \
        "in order to approximate pi: The ratio of darts in a unit circle\n"\
        "to the total number of darts in a 2X2 square should be\n"\
        "approximately  equal to pi/4")
    print("=========== Part A ===========")

    #Create window, turtle, set up window as dartboard
    window = turtle.Screen()
    darty = turtle.Turtle()
    darty.speed(0) # as fast as it will go!
    setUpDartboard(window, darty)

    # Loop for 10 darts to test your code
    for i in range(10):
        throwDart(darty)
    print("\tPart A Complete...")
    print("=========== Part B ===========")
    darty.clear()
    setUpDartboard(window, darty)
    playDarts(darty)
    print("\tPart B Complete...")
    # Keep the window up until dismissed
    print("=========== Part C ===========")
    darty.clear()
    setUpDartboard(window, darty)
    # Include the following code in order to update animation periodically
    #instead of for each throw (saves LOTS of time):
    BATCH_OF_DARTS = 5000
    window.tracer(BATCH_OF_DARTS)

    # Conduct simulation and print result
    number_darts = int(input("\nPlease input the number of darts to be thrown in the simulation:  "))
    approx_pi = montePi(darty, number_darts)
    print("\nThe estimation of pi using "+str(number_darts)+" virtual darts is " + str(approx_pi))
    print("\tPart C Complete...")
    # Don't hide or mess with window while it's 'working'
    window.exitonclick()
main()