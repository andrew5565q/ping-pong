from pygame import *

# from random import choice

window = display.set_mode((700, 500))
display.set_caption('ping_pong')
background = transform.scale(image.load('galaxy.jpg'), (700, 500))

clock = time.Clock()
finish = False
FPS = 60

number1 = 0
number2 = 0


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (20, 150))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

        '''
             if self.rect.x <= 230:
                 self.direction = 'right'
             if self.rect.x >= 500:
                 self.direction = 'left'
             if self.direction == 'left':
                 self.rect.x -= self.speed
             else:
                 self.rect.x += self.speed
            de vertical(self):
             if self.rect.y <= 170:
                 self.direction = 'top'
             if self.rect.y >= 450:
                 self.direction = 'down'
             if self.direction == 'down':
                 self.rect.y -= self.speed
             else:
                 self.rect.y += self.speed
             '''


class Player(GameSprite):
    def update(self, number):
        keys_pressed = key.get_pressed()
        if number == 'one':
            if keys_pressed[K_w] and self.rect.y >= 0:
                self.rect.y -= self.speed
            if keys_pressed[K_s] and self.rect.y <= 350:
                self.rect.y += self.speed
        if number == 'two':
            if keys_pressed[K_UP] and self.rect.y >= 0:
                self.rect.y -= self.speed
            if keys_pressed[K_DOWN] and self.rect.y <= 350:
                self.rect.y += self.speed


class Wall(sprite.Sprite):
    def __init__(self, height, width, x_cor, y_cor, color_1, color_2, color_3):
        super().__init__()
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

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class GameSpritee(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (75, 75))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed

    def resett(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Ball(GameSpritee):
    direction_x = 'left'
    direction_y = 'up'


    def movement(self):
        if self.direction_x == 'left':
            self.rect.x -= self.speed
        if self.direction_x == 'right':
            self.rect.x += self.speed
        if self.direction_y == 'up':
            self.rect.y -= self.speed
        if self.direction_y == 'down':
            self.rect.y += self.speed


game = True

racket_1 = Player('bone.png', 5, 250, 3)
racket_2 = Player('bone.png', 675, 250, 3)

ball = Ball('ball_1.png', 300, 250, 4)

wall_top = Wall(2, 700, 0, 0, 0, 0, 110)
wall_bottom = Wall(2, 700, 0, 498, 0, 0, 110)
wall_left = Wall(500, 2, 0, 0, 0, 0, 110)
wall_right = Wall(500, 2, 698, 0, 0, 0, 110)

font.init()
font1 = font.Font(None, 30)
font2 = font.Font(None, 70)
shot = font1.render('shot:' + str(number1), True, (255, 105, 0))
missed = font1.render('missed: ' + str(number2), True, (255, 0, 140))
rules = font1.render('rules: you need to kill 25 aliens, you have 10 lives, good luck!', True, (105, 220, 140))
again = font1.render('press e to play again', True, (255, 150, 40))

win = font2.render('you win', True, (255, 175, 0))
lose = font2.render('you lose', True, (255, 105, 40))

while game:
    window.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish is not True:
        wall_top.draw_wall()
        wall_left.draw_wall()
        wall_bottom.draw_wall()
        wall_right.draw_wall()

        racket_1.update('one')
        racket_1.reset()

        racket_2.update('two')
        racket_2.reset()

        ball.resett()
        ball.movement()
        '''
        window.blit(shot, (1, 30))
        window.blit(missed, (1, 60))
        '''
        if sprite.collide_rect(ball, wall_top):
            if ball.direction_y == 'up':
                ball.direction_y = 'down'
            else:
                ball.direction_y = 'up'
            '''
            if ball.direction_x == 'left':
                ball.direction_x = 'right'
            else:
                ball.direction_x = 'left'
'''
        if sprite.collide_rect(ball, wall_bottom):
            if ball.direction_y == 'up':
                ball.direction_y = 'down'
            else:
                ball.direction_y = 'up'
            '''
            if ball.direction_x == 'left':
                ball.direction_x = 'right'
            else:
                ball.direction_x = 'left'
'''
        if sprite.collide_rect(ball, wall_left):
            '''
            if ball.direction_y == 'up':
                ball.direction_y = 'down'
            else:
                ball.direction_y = 'up'''
            ball.direction_x = 'right'

        if sprite.collide_rect(ball, wall_right):
            '''
            if ball.direction_y == 'up':
                ball.direction_y = 'down'
            else:
                ball.direction_y = 'up'
                '''
            ball.direction_x = 'left'
        if sprite.collide_rect(ball, racket_2):
            ball.direction_x = 'left'
        if sprite.collide_rect(ball, racket_1):
            ball.direction_x = 'right'


        shot = font1.render('shot:' + str(number1), True, (255, 105, 0))
        missed = font1.render('missed: ' + str(number2), True, (255, 0, 140))
    display.update()
    clock.tick(FPS)
