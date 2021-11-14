from pygame import *
from random import randint

window = display.set_mode((700, 500))
display.set_caption('space')

clock = time.Clock()
finish = False
FPS = 60

numbah1 = 0
numbah2 = 0

keys_pressed = key.get_pressed()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (75, 75))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x >= 10:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x <= 640:
            self.rect.x += self.speed

game = True

font.init()
font1 = font.Font(None, 30)
font2 = font.Font(None, 70)
shot = font1.render('shot:' + str(numbah1), True, (255, 105, 0))
missed = font1.render('missed: ' + str(numbah2), True, (255, 0, 140))
rules = font1.render('rules: you need to kill 25 aliens, you have 10 lives, good luck!', True, (105, 220, 140))
again = font1.render('press e to play again', True, (255, 150, 40))

win = font2.render('you win', True, (255, 175, 0))
lose = font2.render('you lose', True, (255, 105, 40))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:

        window.blit(shot, (1, 30))
        window.blit(missed, (1, 60))

        shot = font1.render('shot:' + str(numbah1), True, (255, 105, 0))
        missed = font1.render('missed: ' + str(numbah2), True, (255, 0, 140))
    display.update()
    clock.tick(FPS)
