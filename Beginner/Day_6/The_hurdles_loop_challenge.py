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

def jump():
    move()
    jump_func()
    jump_func()
    jump_func()
    jump_func()
    jump_func()
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
    
def jump_func():
    turn_left_move()
    turn_right_move()
    turn_right_move()
    turn_left_move()

jump()
