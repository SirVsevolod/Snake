import pygame


class Button:


    black = (0, 0, 0)

    def __init__(self, Win, WIDTH, HEIGHT,):
        self.width = WIDTH
        self.heigh = HEIGHT
        self.inactive_color = (0, 255, 0)
        self.active_color = (255, 0, 0)
        self.Win = Win
        self.font = pygame.font.SysFont("microsofttaile", 32)

    def Draw(self,  x, y, message,):
        follow = self.font.render(message, 1, self.black)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < int(mouse[0]) < x + self.width and y < int(mouse[1]) < y + self.heigh:
            pygame.draw.rect(self.Win, self.active_color, (x, y, self.width, self.heigh))
            if click[0] == 1:
                return True
        else:
            pygame.draw.rect(self.Win, self.inactive_color, (x, y, self.width, self.heigh))
        self.Win.blit(follow, (x + 15, y + 15))




