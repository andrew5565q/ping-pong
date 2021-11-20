from pygame import *

window = display.set_mode((700, 500))
display.set_caption('space')

clock = time.Clock()
finish = False
FPS = 60

numbah1 = 0
numbah2 = 0


class GameSprite(sprite.Sprite):
    def init(self, player_image, player_x, player_y, player_speed):
        #super().init()
        self.image = transform.scale(image.load(player_image), (75, 75))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(sprite.Sprite):
    def init(self, height, width, x_cor, y_cor, color_1, color_2, color_3, speed):
        #super().init()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = x_cor
        self.rect.y = y_cor
        self.speed = speed
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y >= 10:
            self.rect.x -= self.speed
        if keys_pressed[K_s] and self.rect.x <= 440:
            self.rect.x += self.speed
    def draw_racket(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

game = True

racket_1 = Player(100, 20, 0, 250, 0, 0, 100, 3)

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

        racket_1.draw_racket()
        racket_1.update()

        '''
        window.blit(shot, (1, 30))
        window.blit(missed, (1, 60))
        '''

        shot = font1.render('shot:' + str(numbah1), True, (255, 105, 0))
        missed = font1.render('missed: ' + str(numbah2), True, (255, 0, 140))
    display.update()
    clock.tick(FPS)