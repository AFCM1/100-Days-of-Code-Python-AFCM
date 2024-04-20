def jump():
    move()
    turn_left_move()
    turn_right_move()
    turn_right_move()
    turn_left_move()
    turn_left_move()
    turn_right_move()
    turn_right_move()
    turn_left_move()
    turn_left_move()
    turn_right_move()
    turn_right_move()
    turn_left_move()
    turn_left_move()
    turn_right_move()
    turn_right_move()
    turn_left_move()
    turn_left_move()
    turn_right_move()
    turn_right_move()
    turn_left_move()
    turn_left_move()
    turn_right_move()
    turn_right_move()
    
def turn_left_move():
    turn_left()
    move()

def turn_right_move():
    turn_left()
    turn_left()
    turn_left()
    move()  

jump()


#Shorter version

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for step in range(6):
    jump()
    
    
jump()

#With While loop

nb_of_hurdles = 6
while nb_of_hurdles > 0:
    jump()
    nb_of_hurdles -= 1
    print(nb_of_hurdles)

##Hurdles loop challenge 2 

nb_of_hurdles = 6
while nb_of_hurdles > 0:
    jump()
    if at_goal():
        done()
    nb_of_hurdles -= 1

#Angela version
while at_goal() != True:
    jump()

or

while not at_goal():
    jump()


