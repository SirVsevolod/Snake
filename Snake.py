import pygame


class Snake:

    body_lenh = 3
    body_width = 10
    body_height = 10
    x = 60
    y = 30
    speed = 20
    body = [[60, 30], [45, 30], [30, 30], ]
    snake_head = body[0]

    def __init__(self, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

    def SnakeGo(self, direction, Win):
        if direction == "RIGHT":
            self.x += self.speed
        elif direction == "LEFT":
            self.x -= self.speed
        elif direction == "UP":
            self.y -= self.speed
        elif direction == "DOWN":
            self.y += self.speed

        if self.x < 0:
            self.x = self.WIDTH
        elif self.x > self.WIDTH - self.body_width:
            self.x = 0

        if self.y < 0:
            self.y = self.HEIGHT
        elif self.y > self.HEIGHT - self.body_height:
            self.y = 0

        self.BodyUpdate()
        self.PrintBody(Win)

    def PrintBody(self, Win):
        for i in range(len(self.body)):
            if len(self.body) % 2 != 0:
                pygame.draw.rect(Win, (255, 0, 0), (self.body[i - 1][0], self.body[i - 1][1], self.body_width, self.body_height))
            else:
                pygame.draw.rect(Win, (255, 255, 255), (self.body[i - 1][0], self.body[i - 1][1], self.body_width, self.body_height))


    def BodyUpdate(self,):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i][0] = self.body[i - 1][0]
            self.body[i][1] = self.body[i - 1][1]
        self.body[0][0] = self.x
        self.body[0][1] = self.y

    def DieSnake(self,):
        if self.body[0] in self.body[1:]:
            return False
        else:
            return True

    def SnakeGrowth(self, points):
        if points + 3 > len(self.body):
            tail = []
            tail.append(self.body[-1][0])
            tail.append(self.body[-1][1])
            self.body.append(tail)

    def SHead(self):
        s = []
        s.append([self.snake_head[0], self.snake_head[1]])
        s.append([self.snake_head[0], self.snake_head[1] + 10])
        s.append([self.snake_head[0] + 10, self.snake_head[1]])
        s.append([self.snake_head[0] + 10, self.snake_head[1] + 10])
        return s



