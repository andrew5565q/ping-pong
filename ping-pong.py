from pygame import *
from time import sleep
# from random import choice

window = display.set_mode((700, 500))
display.set_caption('ping_pong')
background = transform.scale(image.load('galaxy.jpg'), (700, 500))

clock = time.Clock()
finish = False
menu = True
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


class GameSprites(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (75, 75))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed

    def resets(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Ball(GameSprites):
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

racket_1 = Player('racket_1.png', 5, 250, 3)
racket_2 = Player('racket_1.png', 675, 250, 3)

rackets = [racket_1, racket_2]

ball = Ball('ball_1.png', 300, 250, 4)

wall_top = Wall(2, 700, 0, 0, 0, 0, 110)
wall_bottom = Wall(2, 700, 0, 498, 0, 0, 110)
wall_left = Wall(500, 2, 0, 0, 0, 0, 110)
wall_right = Wall(500, 2, 698, 0, 0, 0, 110)

font.init()
font1 = font.Font(None, 60)
font2 = font.Font(None, 30)
winner = font.Font(None, 90)

shot = font1.render('shot:' + str(number1), True, (255, 105, 0))
missed = font1.render('missed: ' + str(number2), True, (255, 0, 140))


switch = False

startBtn = Rect(290, 200, 120, 35)
skinsBtn = Rect(290, 250, 120, 35)
backBtn = Rect(570, 50, 120, 35)

racket_skin_1 = Rect(190, 200, 120, 35)
racket_skin_2 = Rect(190, 250, 120, 35)
racket_skin_3 = Rect(190, 300, 120, 35)

ball_skin_1 = Rect(390, 200, 120, 35)
ball_skin_2 = Rect(390, 250, 120, 35)
ball_skin_3 = Rect(390, 300, 120, 35)

first = 0
second = 0
score = font1.render('score ' + str(first) + ':' + str(second), True, (255, 0, 140))

c_1 = (0, 0, 0)
c_2 = (0, 0, 0)
c_3 = (0, 0, 0)

cc_1 = (0, 0, 0)
cc_2 = (0, 0, 0)
cc_3 = (0, 0, 0)

while game:
    window.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    mousePos = mouse.get_pos()
    if finish is not True:
        if menu is True:
            if switch is False:
                draw.rect(window, (110, 200, 255), startBtn)
                draw.rect(window, (110, 200, 255), skinsBtn)
                window.blit(font1.render('start', True, (0, 0, 0)), (300, 200))
                window.blit(font1.render('skins', True, (0, 0, 0)), (295, 250))
            if Rect.collidepoint(skinsBtn, mousePos) and e.type == MOUSEBUTTONDOWN or switch is True:
                draw.rect(window, (110, 200, 255), backBtn)
                window.blit(font1.render('back', True, (0, 0, 0)), (580, 50))
                switch = True

                window.blit(font2.render('racket skins', True, (100, 200, 205)), (190, 150))

                draw.rect(window, (210, 200, 55), racket_skin_1)
                window.blit(font1.render('bone', True, c_1), (200, 200))
                draw.rect(window, (210, 200, 55), racket_skin_2)
                window.blit(font1.render('plank', True, c_2), (200, 250))
                draw.rect(window, (210, 200, 55), racket_skin_3)
                window.blit(font2.render('cardboard', True, c_3), (200, 310))

                window.blit(font2.render('racket skins', True, (100, 200, 205)), (390, 150))
                draw.rect(window, (255, 165, 0), ball_skin_1)
                window.blit(font2.render('pokeball', True, cc_1), (400, 210))
                draw.rect(window, (255, 165, 0), ball_skin_2)
                window.blit(font2.render('beach ball', True, cc_2), (400, 260))
                draw.rect(window, (255, 165, 0), ball_skin_3)
                window.blit(font2.render('disco ball', True, cc_3), (400, 310))

                if Rect.collidepoint(racket_skin_1, mousePos) and e.type == MOUSEBUTTONDOWN:
                    racket_1 = Player('racket_1.png', 5, 250, 3)
                    racket_2 = Player('racket_1.png', 675, 250, 3)

                    c_1 = (255, 255, 255)
                    c_2 = (0, 0, 0)
                    c_3 = (0, 0, 0)

                if Rect.collidepoint(racket_skin_2, mousePos) and e.type == MOUSEBUTTONDOWN:
                    racket_1 = Player('racket_2.png', 5, 250, 3)
                    racket_2 = Player('racket_2.png', 675, 250, 3)

                    c_1 = (0, 0, 0)
                    c_2 = (255, 255, 255)
                    c_3 = (0, 0, 0)

                if Rect.collidepoint(racket_skin_3, mousePos) and e.type == MOUSEBUTTONDOWN:
                    racket_1 = Player('racket_3.png', 5, 250, 3)
                    racket_2 = Player('racket_3.png', 675, 250, 3)

                    c_1 = (0, 0, 0)
                    c_2 = (0, 0, 0)
                    c_3 = (255, 255, 255)

                if Rect.collidepoint(ball_skin_1, mousePos) and e.type == MOUSEBUTTONDOWN:
                    ball = Ball('ball_1.png', 300, 250, 4)

                    cc_1 = (255, 255, 255)
                    cc_2 = (0, 0, 0)
                    cc_3 = (0, 0, 0)

                if Rect.collidepoint(ball_skin_2, mousePos) and e.type == MOUSEBUTTONDOWN:
                    ball = Ball('ball_2.png', 300, 250, 4)

                    cc_1 = (0, 0, 0)
                    cc_2 = (255, 255, 255)
                    cc_3 = (0, 0, 0)

                if Rect.collidepoint(ball_skin_3, mousePos) and e.type == MOUSEBUTTONDOWN:
                    ball = Ball('ball_3.png', 300, 250, 4)

                    cc_1 = (0, 0, 0)
                    cc_2 = (0, 0, 0)
                    cc_3 = (255, 255, 255)

            if Rect.collidepoint(backBtn, mousePos) and e.type == MOUSEBUTTONDOWN or switch is False:
                switch = False

            if Rect.collidepoint(startBtn, mousePos) and e.type == MOUSEBUTTONDOWN:
                menu = False

        if menu is False:
            wall_top.draw_wall()
            wall_left.draw_wall()
            wall_bottom.draw_wall()
            wall_right.draw_wall()

            racket_1.update('one')
            racket_1.reset()

            racket_2.update('two')
            racket_2.reset()

            ball.resets()
            ball.movement()

            window.blit(score, (250, 10))

            if sprite.collide_rect(ball, wall_top):
                if ball.direction_y == 'up':
                    ball.direction_y = 'down'
                else:
                    ball.direction_y = 'up'

            if sprite.collide_rect(ball, wall_bottom):
                if ball.direction_y == 'up':
                    ball.direction_y = 'down'
                else:
                    ball.direction_y = 'up'

            if sprite.collide_rect(ball, wall_left):
                ball.speed = 0
                ball.direction_x = 'right'
                breathing_room = font1.render('3', True, (255, 105, 40))
                window.blit(breathing_room, (150, 250))
                sleep(0.25)
                breathing_room = font1.render('2', True, (255, 105, 40))
                window.blit(breathing_room, (150, 250))
                sleep(0.25)
                breathing_room = font1.render('1', True, (255, 105, 40))
                window.blit(breathing_room, (150, 250))
                sleep(0.25)
                second += 1
                ball.rect.x = 350
                ball.rect.y = 250
                ball.speed = 4

            if sprite.collide_rect(ball, wall_right):
                ball.speed = 0
                ball.direction_x = 'left'
                breathing_room = font1.render('3', True, (255, 105, 40))
                window.blit(breathing_room, (150, 250))
                sleep(0.25)
                breathing_room = font1.render('2', True, (255, 105, 40))
                window.blit(breathing_room, (150, 250))
                sleep(0.25)
                breathing_room = font1.render('1', True, (255, 105, 40))
                window.blit(breathing_room, (150, 250))
                sleep(0.25)
                first += 1
                ball.rect.x = 350
                ball.rect.y = 250
                ball.speed = 4

            if sprite.collide_rect(ball, racket_2):
                ball.speed += 1
                ball.direction_x = 'left'

            if sprite.collide_rect(ball, racket_1):
                ball.speed += 1
                ball.direction_x = 'right'

            if first == 3 or second == 3:
                finish = True

            score = font1.render('score ' + str(first) + ':' + str(second), True, (255, 0, 140))
    if first == 3:
        window.blit(winner.render('player1 wins', True, (0, 200, 205)), (170, 210))
    elif second == 3:
        window.blit(winner.render('player2 wins', True, (0, 200, 205)), (170, 210))
    display.update()
    clock.tick(FPS)
