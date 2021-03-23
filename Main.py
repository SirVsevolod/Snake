import pygame
import random
from Snake import Snake
from Apple import Apple
from Menu import Button



point = 0
WIDTH = 600
HEIGHT = 400

s = Snake(WIDTH, HEIGHT)
a = Apple(WIDTH, HEIGHT)


speed = 5
direction = "RIGHT"


pygame.init()
Win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Snake")


StartButton = Button(Win, 190, 75)
ExitButton = Button(Win, 190, 75)

#Main menu
Menu = True
while Menu:
    pygame.time.delay(50)
    if StartButton.Draw(200, 50, "Start Game",):
        s = Snake(WIDTH, HEIGHT)
        point = 0
        running = True
        while running:
            pygame.time.delay(50)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                direction = "LEFT"
            elif keys[pygame.K_RIGHT]:
                direction = "RIGHT"
            elif keys[pygame.K_UP]:
                direction = "UP"
            elif keys[pygame.K_DOWN]:
                direction = "DOWN"

            Win.fill((0, 200, 0))

            pygame.draw.rect(Win, (0, 0, 255), (a.x, a.y, a.apple_width, a.apple_height))
            running = s.DieSnake()
            Menu = s.DieSnake()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    Menu = False

            if a.ChekEat(s.SHead(), Win, s.body):
                point = point + 1

            s.SnakeGrowth(point)
            s.SnakeGo(direction, Win)

            pygame.display.update()
    elif ExitButton.Draw(200, 150, "Exit Game",):
        Menu = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Menu = False
    pygame.display.update()

print("Your Score: " + str(point))
pygame.quit()

