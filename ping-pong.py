from pygame import *

window = display.set_mode((700, 500))
display.set_caption('space')
background = transform.scale(image.load('galaxy.jpg'), (700, 500))

clock = time.Clock()
finish = False
FPS = 60

numbah1 = 0
numbah2 = 0


class GameSprite(sprite.Sprite):
    def __init__(self, height, width, player_x, player_y, color_1, color_2, color_3, player_speed):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = width
        self.height = height
        self.x = player_x
        self.y = player_y
        self.speed = player_speed
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))

    def reset(self):
        window.blit(self.image, (self.x, self.y))


class Player(GameSprite):
    def update(self, number):
        keys_pressed = key.get_pressed()
        if number == 'one':
            if keys_pressed[K_w] and self.y >= 0:
                self.y -= self.speed
            if keys_pressed[K_s] and self.y <= 350:
                self.y += self.speed
        if number == 'two':
            if keys_pressed[K_UP] and self.y >= 0:
                self.y -= self.speed
            if keys_pressed[K_DOWN] and self.y <= 350:
                self.y += self.speed


game = True

racket_1 = Player(150, 20, 5, 250, 200, 100, 100, 3)
racket_2 = Player(150, 20, 675, 250, 200, 100, 100, 3)

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
    window.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        racket_1.update('one')
        racket_1.reset()

        racket_2.update('two')
        racket_2.reset()
        '''
        window.blit(shot, (1, 30))
        window.blit(missed, (1, 60))
        '''

        shot = font1.render('shot:' + str(numbah1), True, (255, 105, 0))
        missed = font1.render('missed: ' + str(numbah2), True, (255, 0, 140))
    display.update()
    clock.tick(FPS)
