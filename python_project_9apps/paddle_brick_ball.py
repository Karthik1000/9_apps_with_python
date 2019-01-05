from Tkinter import Tk, Canvas, BOTH
from math import sin, cos, radians
from random import choice, randint
WIDTH=1000
HEIGHT=600
def call():
	class Breakout(Tk):
		def __init__(self):
		    Tk.__init__(self)
		    self.geometry('790x600')
		    self.resizable(0,0)		#set both parameters to false and to check whether window is resizable in x and y directions

		    # game screen
		    self.canvas = Canvas(self, bg='skyblue', width=990, height=600)
		    self.canvas.pack(expand=1, fill=BOTH) #when it is true and widget expands to fill any space 

		    # ball
		    self._initiate_new_ball()

		    # paddle
		    self.canvas.create_rectangle(375,975,525,585, fill='blue',
		                                 outline='white', tags='paddle')
		    self.bind('<Key>', self._move_paddle)

		    # bricks
		    self.bricks = {}
		    brick_coords = [15,15,60,35]
		    for i in range(105):
		        self.canvas.create_rectangle(*brick_coords, outline='white',
		                                     fill=('yellow'),
		                                     tags='brick' + str(i))
		        self.bricks['brick' + str(i)] = None
		        brick_coords[0] += 35; brick_coords[2] += 35
		        if brick_coords[2] > 790:
		            brick_coords[0] = 15; brick_coords[2] = 60
		            brick_coords[1] += 55; brick_coords[3] += 55
		
		def _initiate_new_ball(self):
		    if self.canvas.find_withtag('ball'):
		        self.canvas.delete('ball')
		    self.x = 160; self.y = 500
		    self.angle = 120; self.speed = 5; self.score=0; self.level=0
		    
		    self.canvas.create_oval(self.x,self.y,self.x+10,self.y+10,
		                            fill='lawn green', outline='white', tags='ball')
		    self.after(1000, self._move_ball)
		    
		def _move_paddle(self, event):
		    if event.keysym == 'Left':
		        if self.canvas.coords('paddle')[0] > 0:
		            self.canvas.move('paddle', -20, 0)
		    elif event.keysym == 'Right':
		        if self.canvas.coords('paddle')[2] < 990:
		            self.canvas.move('paddle', +20, 0)
	
		def _move_ball(self):
		
		    # variables to determine where ball is in relation to other objects
		    ball = self.canvas.find_withtag('ball')[0]
		    bounds = self.canvas.find_overlapping(0,0,790,600)
		    paddle = self.canvas.find_overlapping(*self.canvas.coords('paddle'))
		    for brick in self.bricks.iterkeys():
		        self.bricks[brick] = self.canvas.find_overlapping(*self.canvas.bbox(brick))

		    # calculate change in x,y values of ball
		    angle = self.angle - 90 # correct for quadrant IV
		    increment_x = cos(radians(angle)) * self.speed
		    increment_y = sin(radians(angle)) * self.speed
			#score=self.score
			#score=0
		    # finite state machine to set ball state
		    if ball in bounds:
		        self.ball_state = 'moving'
		        for brick, hit in self.bricks.iteritems():
		            if ball in hit:
		                self.ball_state = 'hit_brick'
		                delete_brick = brick
		            elif ball in paddle:
		                self.ball_state = 'hit_wall'
		            elif (self.score)//3 == 101:
		            	self.canvas.create_text(WIDTH/4,HEIGHT/2.3,text="GAME completed! u won one ")
						
		            	self.canvas.create_text(WIDTH/4,HEIGHT/2,text=self.score//3)
		            	self.canvas.create_text(WIDTH/4,HEIGHT/1.7,text="score is above")	
		        
		            	
		       			
					

		    elif ball not in bounds:
		        if self.canvas.coords('ball')[1] < 600:
		            self.ball_state = 'hit_wall'
		        else:
		            self.ball_state = 'out_of_bounds'
		            
		            self.canvas.create_text(WIDTH/4,HEIGHT/2.3,text="GAME OVER there is chance to play!")
		            self.canvas.create_text(WIDTH/4,HEIGHT/2,text="score is below")           		
		            self.canvas.create_text(WIDTH/4,HEIGHT/1.7,text=self.score//3)
		            #self.canvas.create_text(WIDTH/4,HEIGHT/3,text="LEVEL IS BELOW")
		            #self.canvas.create_text(WIDTH/4,HEIGHT/2,text=self.level//89//6)
		            call()
		            self._initiate_new_ball()
				
				
		    # handler for ball state
		    if self.ball_state is 'moving':
		        self.canvas.move('ball', increment_x, increment_y)
		        self.after(35, self._move_ball)
		        self.level +=choice([1])
		        
		    elif self.ball_state is 'hit_brick' or self.ball_state is 'hit_wall':
		        if self.ball_state == 'hit_brick':
		            self.canvas.delete(delete_brick)
		            del self.bricks[delete_brick]
		        self.canvas.move('ball', -increment_x, -increment_y)
		        self.score += choice([1])
		        self.angle += choice([135])
		        #canvas.create_text(WIDTH/4,HEIGHT/5,text="GAME OVER!")
		        self._move_ball()

	game = Breakout()
	game.mainloop()

call()

