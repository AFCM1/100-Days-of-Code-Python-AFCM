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
