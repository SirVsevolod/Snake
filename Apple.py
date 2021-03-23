import pygame
import random


class Apple:
    
    x = 300
    y = 200
    
    apple_width = 30
    apple_height = 30

    def __init__(self, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

    def MakeApple(self, Win, body,):
        self.x = random.choice(range(self.WIDTH - self.apple_width))
        self.y = random.choice(range(self.HEIGHT - self.apple_height))
        pygame.draw.rect(Win, (0, 0, 255), (self.x, self.y, self.apple_width, self.apple_height))
        apple = [self.x, self.y]
        if self.SApple in body:
            self.MakeApple(Win, body)
            
    def SApple(self):
        s = []
        x = self.x
        y = self.y
        for i in range(30):
            y = self.y
            for j in range(30):
                s.append([x, y])
                y = y + 1
            x = x + 1
        return s

    def ChekEat(self, snake_head, Win, body):
        for s in snake_head:
            if s in self.SApple():
                self.MakeApple(Win, body)
                return True
