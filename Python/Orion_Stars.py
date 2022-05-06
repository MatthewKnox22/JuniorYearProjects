# Matthew Knox 9-28-2020
# Orion Stars

import turtle
# setup turtle
turtle.penup()
turtle.hideturtle()

#Create variables for each star name
left_shoulder_x = -70
left_shoulder_y = 200

right_shoulder_x = 80
right_shoulder_y = 180

left_beltstar_x = -40
left_beltstar_y = -20

middle_beltstar_x = 0
middle_beltstar_y = 0

right_beltstar_x = 40
right_beltstar_y = 20


left_knee_x = -90
left_knee_y = -180

right_knee_x = 120
right_knee_y = -140

#set window size
turtle.setup(500, 600)

#draw the stars
turtle.goto(left_shoulder_x, left_shoulder_y) #this is the left shoulder
turtle.dot()

turtle.goto(right_shoulder_x, right_shoulder_y) #this is the right shoulder
turtle.dot()

turtle.goto(left_beltstar_x, left_beltstar_y) #this is the left belt star
turtle.dot()

turtle.goto(middle_beltstar_x, middle_beltstar_y) #this is the middle belt star
turtle.dot()

turtle.goto(right_beltstar_x, right_beltstar_y) #this is the right belt star
turtle.dot()

turtle.goto(left_knee_x, left_knee_y) #this is the left knee
turtle.dot()

turtle.goto(right_knee_x, right_knee_y) #this is the right knee
turtle.dot()

# names of stars
turtle.goto(left_shoulder_x, left_shoulder_y)
turtle.write('Betegeuse')

turtle.goto(right_shoulder_x, right_shoulder_y)
turtle.write('Meissa')

turtle.goto(left_beltstar_x, left_beltstar_y)
turtle.write('Alnitak')

turtle.goto(middle_beltstar_x, middle_beltstar_y)
turtle.write('Alnilam')

turtle.goto(right_beltstar_x, right_beltstar_y)
turtle.write('Mintaka')

turtle.goto(left_knee_x, left_knee_y)
turtle.write('Saiph')

turtle.goto(right_knee_x, right_knee_y)
turtle.write('Rigel')

#drawing lines to each dot

#left shoulder to lef belt star
turtle.goto(left_shoulder_x, left_shoulder_y)
turtle.pendown()
turtle.goto(left_beltstar_x, left_beltstar_y)
turtle.penup()

#right shoulder to right beltstar
turtle.goto(right_shoulder_x, right_shoulder_y)
turtle.pendown()
turtle.goto(right_beltstar_x, right_beltstar_y)
turtle.penup()

#left belt star to middle bet star
turtle.goto(left_beltstar_x, left_beltstar_y)
turtle.pendown()
turtle.goto(middle_beltstar_x, middle_beltstar_y)
turtle.penup()

#middle belt star to right belt star 
turtle.goto(middle_beltstar_x, middle_beltstar_y)
turtle.pendown()
turtle.goto(right_beltstar_x, right_beltstar_y)
turtle.penup()

#left belt star to left knee
turtle.goto(left_beltstar_x, left_beltstar_y)
turtle.pendown()
turtle.goto(left_knee_x, left_knee_y)
turtle.penup()

# right belt star to right knee 
turtle.goto(right_beltstar_x, right_beltstar_y)
turtle.pendown()
turtle.goto(right_knee_x, right_knee_y)
turtle.penup()





