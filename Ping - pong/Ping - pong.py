from pygame import *
'''Необхадимые классы'''

#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
    #конструктор класса
        #конструктор класса
    def __init__(self, player_image, player_x, player_y, wight, height, player_speed):
        super().__init__()

        #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed

        #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    #метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed   
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed  

#
back = (200, 255, 255)#
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

#
game = True
finish = False
clock = time.Clock()
FPS = 60

#
goku = Player('goku.png', 30, 200, 100, 150, 7)
vegetta = Player('vegeta.png', 520, 200, 100, 150, 7)
ball = GameSprite('drag.png', 200, 200, 50, 50, 6)

font.init()
font = font.SysFont('Arial', 35)
lose1 = font.render('Goku lose!', True, (180, 0, 0))
lose2 = font.render('Vegeta lose!', True, (180, 0, 0))

speed_x = 6
speed_y = 6

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        goku.update_r()
        vegetta.update_1()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(goku, ball) or sprite.collide_rect(vegetta, ball):
            speed_x *= -1
            speed_y *= 1
            
            #
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
                speed_y *= -1

            #
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

            
        #
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))


        goku.reset()
        vegetta.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)