import turtle
import time
import random
import math
from ball import Ball



turtle.tracer(0)
turtle.hideturtle()
turtle.colormode(1)
running = True
turtle.bgpic("background.gif")



screen_width = turtle.getcanvas().winfo_width()/2
screen_height = turtle.getcanvas().winfo_height()/2
turtle.setup(screen_width *2, screen_height*2)

number_of_balls = 5
minimum_ball_radius = 10
maximum_ball_radius = 100
minimum_ball_dx = -5
maximum_ball_dx = 5
minimum_ball_dy = -5
maximum_ball_dy = 5
game_over = turtle.Turtle()
turtle.register_shape('gameover1.gif')

my_ball = Ball (0,0,5,-5,50,"blue")
other_player_ball = Ball (0,0,5,-5,50,"deep pink")
other_player_ball.hideturtle()

BALLS = []
	
for i in range (number_of_balls):
	x = random.randint(-screen_width + maximum_ball_radius,screen_width - maximum_ball_radius)
	y = random.randint(-screen_height + maximum_ball_radius,screen_height - maximum_ball_radius)
	dx = random.randint(minimum_ball_dx,maximum_ball_dx)
	dy = random.randint(minimum_ball_dy,maximum_ball_dy)
	r = random.randint(minimum_ball_radius,maximum_ball_radius)
	color = (random.random(),random.random(),random.random())
	ball1 = Ball(x,y,dx,dy,r,color)
	BALLS.append(ball1)
	ball1.hideturtle()




def move_all_balls():
	other_player_ball.move(screen_width,screen_height)
	for i in BALLS:
		i.move(screen_width,screen_height)
def collied(balla,ballb):
	if balla == ballb:
		return False
	d = math.sqrt(math.pow(ballb.pos()[0] - balla.pos()[0],2) + math.pow(ballb.pos()[1] - balla.pos()[1],2))
	radii = balla.r + ballb.r
	if d <= radii:
		return True
	else:
		return False
		

def check_all_balls_collisions():
	global running
	all_balls = []
	all_balls.append(my_ball)
	all_balls.append(other_player_ball)
	for ball in BALLS:
		all_balls.append(ball)

#turtle.update()
#turtle.mainloop()
	for balla in all_balls:
		for ballb in all_balls:
			if collied(balla,ballb):
				r1 = balla.r
				r2 = ballb.r
				x = random.randint(-screen_width + maximum_ball_radius,screen_width - maximum_ball_radius)
				y = random.randint(-screen_height + maximum_ball_radius,screen_height - maximum_ball_radius)
				dx = random.randint(minimum_ball_dx,maximum_ball_dx)
				dy = random.randint(minimum_ball_dy,maximum_ball_dy)
				r = random.randint(minimum_ball_radius,maximum_ball_radius)
				color = (random.random(),random.random(),random.random())
				while (dx==0):
					dx = random.randint(minimum_ball_dx,maximum_ball_dx)
				while (dy==0):
					dy = random.randint(minimum_ball_dy,maximum_ball_dy)

				if (r1<r2):
					if my_ball==balla:
						running=False
						print(str(balla.color)+str(ballb.color))
						print("game over")
						game_over.goto(0,0)
						game_over.shape('gameover1.gif')

					else:
						balla.new_Ball(x,y,dx,dy,r,color)
						ballb.r=ballb.r + 8
						ballb.shapesize(ballb.r/10)
				else:
					if my_ball==ballb:
						running=False
						print("game over")
						game_over.goto(0,0)
						game_over.shape('gameover1.gif')
					else:
						ballb.new_Ball(x,y,dx,dy,r,color)
						balla.r=balla.r +8
						balla.shapesize(balla.r/10)
def up():
	print("UP!!!")
	other_player_ball.dy=5

turtle.onkey(up, "Up")
def down():
	print("DOWN!!!")
	other_player_ball.dy=-5
turtle.onkey(down,"Down")
def right():
	other_player_ball.dx=5
turtle.onkey(right,"Right")
def left():
	other_player_ball.dx=-5
turtle.onkey(left,"Left")
	
turtle.listen()




def movearound(screen_width, screen_height):
	curso_x=turtle.getcanvas().winfo_pointerx() - screen_width
	curso_y=screen_height - turtle.getcanvas().winfo_pointery()
	my_ball.goto(curso_x,curso_y)

#function for party mode
	#shows the other ball
	#call thw play button function
def party(x,y):
	other_player_ball.showturtle()
	play_button(23,35)


def play_button(x,y):
	global running,screen_height,screen_width
	party_mode.ht()
	for i in BALLS:
		i.showturtle()
	
	while running == True:
		if screen_width!=(turtle.getcanvas().winfo_width()/2) or screen_height!=(turtle.getcanvas().winfo_height()/2):
			screen_width = turtle.getcanvas().winfo_width()/2
			screen_height = turtle.getcanvas().winfo_height()/2
		movearound(screen_width, screen_height) 
		move_all_balls()
		check_all_balls_collisions()
		time.sleep(.1)
		turtle.Screen().update()
		if my_ball.r > 2000:
			running = False
			turtle.clear()
			turtle.bgcolor("white")
			turtle.color("deep pink")
			turtle.write("you became infinite",align="center",font=("Suruma",72,"normal"))

play = turtle.clone()
party_mode = turtle.clone()	
play.showturtle()

party_mode.goto(0,-screen_height/2)
party_mode.showturtle()
turtle.register_shape('playy.gif')
turtle.register_shape('2player.gif')
play.shape("playy.gif")
party_mode.shape("2player.gif")
#party_mode.shape("button.gif")
#party_mode.shapesize(10)
#party_mode.color("blue")
turtle.update()
play.onclick(play_button)
party_mode.onclick(party)

turtle.mainloop()







