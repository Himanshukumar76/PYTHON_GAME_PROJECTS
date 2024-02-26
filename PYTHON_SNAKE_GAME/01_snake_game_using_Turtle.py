import turtle
import random
import time 

delay = 0.2
score = 0 
highestScore = 0

#snake body 

bodies = []

# Getting a screen  | canvas 

s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("purple")
s.setup(width = 600, height=600)

#  create snake head

head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("black")
head.fillcolor("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

# snake food

food = turtle.Turtle()
food.width(0.1)
food.speed(0)
food.shape("circle")
food.color("black")
food.fillcolor("black")
food.penup()
food.ht()
food.goto(0,200)
food.st()

# Score board 

sb = turtle.Turtle()
sb.shape("square")
sb.color("white")
sb.fillcolor("white")
sb.penup()
sb.ht()
sb.goto(-250,-250)
sb.write("Score : 0    |     Highest Score : 0 ")

#MOVEMENT OF THE SNAKE 

def moveup(): 
    if head.direction != "down": 
        head.direction = "up"

def movedown(): 
    if head.direction != "up": 
        head.direction = "down"

def moveleft(): 
    if head.direction != "right": 
        head.direction = "left"

def moveright(): 
    if head.direction != "left": 
        head.direction = "right"
        
def movestop(): 
    head.direction = "stop"

def move():
    if head.direction == "up": 
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down": 
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left": 
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right": 
        x = head.xcor()
        head.setx(x+20)
        
# Even handling  -  Key mappings

s.listen()
s.onkey(moveup, "Up")
s.onkey(movedown,"Down")
s.onkey(moveleft,"Left")
s.onkey(moveright,"Right")
s.onkey(movestop, "space")

# main loop 

while True: 
    # to update the screen 
    s.update()

    # check collision with border
    if head.xcor() > 290: 
        head.setx(-290)
    if head.xcor() < -290: 
        head.setx(290)
    if head.ycor() > 290: 
        head.sety(-290)
    if head.ycor() < -290: 
        head.sety(290)
        
    # check collision with food 
    
    if head.distance(food) < 20: 
        # move the food to the random place 
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x,y)

        # increase the lenght of the snake 
        
        body = turtle.Turtle()
        body.width(1)
        body.speed(0)
        body.penup()
        body.shape("circle")
        body.color("black")
        body.fillcolor("green")
        bodies.append(body)  # append new body

        # increase score 
        score += 10
        
        # change delay
        delay -= 0.001
        
        # update the highest score
        
        if score>highestScore: 
            highestScore = score
        sb.clear()
        sb.write("Score : {} Highest Score : {}".format(score, highestScore))
        
    # move the snake body 
    for index in range(len(bodies)-1, 0, -1): 
        x = bodies[index-1].xcor()
        y = bodies[index-1].ycor()
        bodies[index].goto(x,y)
        
    if len(bodies) > 0: 
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x,y)
    move()
    
    #check colision with snake body 
    
    for body in bodies: 
        if body.distance(head) < 20: 
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"

            #hide bodies 
            for body in bodies: 
                body.ht()
                
            bodies.clear()
            score = 0
            delay = 0.1
            
            # update score board 
            
            sb.clear()
            sb.write("Score : {} Highest Score : {}".format(score, highestScore))
            
    time.sleep(delay)
s.mainloop()

    
    
    
    
        



  