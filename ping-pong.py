from typing import Any
from pygame import *
init()
font.init()

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))

display.set_caption('ping-pong')

window.fill((6, 155, 181))

font1 = font.SysFont('Calibri', 36)
txt_loose_1 = font1.render(
    'PLAYER 1 LOOSE!', 1, (255, 255, 255)
)

font1 = font.SysFont('Calibri', 36)
txt_loose_2 = font1.render(
    'PLAYER 2 LOOSE!', 1, (255, 255, 255)
)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed, player_speed_y):
        super().__init__(player_image, player_x, player_y, size_x, size_y, player_speed)
        self.speed_y = player_speed_y
    def update_b(self):
        self.rect.x += self.speed
        self.rect.y += self.speed_y

player_1 = Player('pl_1.png', 80, 200, 10, 100, 2)
player_2 = Player('pl_2.png', 620, 200, 10, 100, 2)

ball = Ball('Ball.png', 250, 350, 50, 50, 2, 2)

game = True
clock = time.Clock()
FPS = 60

speed_x = 3
speed_y = 3
finish = False

while game:
    window.fill((6, 155, 181))
    
    if finish != True:
        player_1.reset()
        player_1.update_l()
        player_2.reset()
        player_2.update_r()
        ball.reset()
        ball.update_b()

        if sprite.collide_rect(player_1, ball) or sprite.collide_rect(player_2, ball):
            ball.speed *= -1
            ball.speed_y *= 1
        if ball.rect.y > 450 or ball.rect.y < 1:
            ball.speed_y *= -1
    if ball.rect.x >= 650:
        window.blit(txt_loose_2, (300, 200))
        finish = True
    if ball.rect.x <= 0:
        window.blit(txt_loose_1, (300, 200))
        finish = True

    for e in event.get():
        if e.type == QUIT:
            game = False


    display.update()
    clock.tick(FPS)