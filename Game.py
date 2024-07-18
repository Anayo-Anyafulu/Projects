import pygame

# Initialize pygame
pygame.init()

# Set the window size and caption
win = pygame.display.set_mode((555, 555))
pygame.display.set_caption("Ping Pong")

# Fill the window with a background color
win.fill((23, 34, 44))


class Plank:
    def __init__(self, x, y, width, height, color):
        # Initialize plank attributes
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 7
        self.left = False
        self.right = False
        self.color = color


class Ball:
    def __init__(self, x, y, radius, color):
        # Initialize ball attributes
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.ball_vel = 5




# Create instances of Ball and Plank
ball = Ball(250, 250, 5, (255, 30, 30))
Player = Plank(230, 350, 30, 10, (255, 80, 20))
Player2 = Plank(230, 100,30 , 10, (255, 80, 20))
run = True
while run:
    pygame.time.delay(20)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    ball.x += ball.ball_vel
    ball.y += ball.ball_vel


    # Fill the window with the background color before drawing the ball and plank
    win.fill((23, 34, 44))

    # Draw the ball and plank on the window
    pygame.draw.circle(win, ball.color, (ball.x, ball.y), ball.radius)
    pygame.draw.rect(win, Player.color, (Player.x, Player.y, Player.width, Player.height))
    pygame.draw.rect(win, Player2.color, (Player2.x, Player2.y, Player2.width, Player2.height))


    # Update the display
    pygame.display.update()

    # Handle key presses to move the player 1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and Player.x >= 80 or keys[pygame.K_LEFT] and Player.x <= 20:
        Player.x -= Player.vel
    if keys[pygame.K_RIGHT] and Player.x < 400 or keys[pygame.K_RIGHT] and Player.x < 400:
        Player.x += Player.vel
    if ball.x == Player.x or ball.y == Player.y:
        ball.ball_vel *= -1

    # Handle key presses to move the player 1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and Player2.x >= 80 or keys[pygame.K_a] and Player2.x <= 20:
        Player2.x -= Player2.vel
    if keys[pygame.K_d] and Player2.x < 400 or keys[pygame.K_d] and Player2.x < 400:
        Player2.x += Player2.vel


    # Check for collision between the ball and the plank
    if ball.y + ball.radius >= Player.y and ball.x >= Player.x and ball.x <= Player.x + Player.width:
       # Change the direction of the ball's velocity to bounce off
       ball.ball_vel *= -1

# Update the ball's position based on its velocity
ball.x += ball.ball_vel
ball.y += ball.ball_vel
    
# Quit pygame
pygame.quit()