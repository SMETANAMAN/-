from pygame import *
#создай окно игры
from random import*
window = display.set_mode((700, 500))
schet = 0
font.init()
font = font.SysFont('Montserrat', 36)
win = font.render(
    'YOU WON!', True, (255,215,0)
)
lose = font.render(
    'YOU ARE BIBA-BOBA!', True, (0,0,0)
)
display.set_caption("Your life")
class GameSprite (sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size1, size2):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size1, size2))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player (GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a]:
            self.rect.x -= self.speed

        if keys_pressed[K_d]:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet("хук мой.png",self.rect.centerx, self.rect.top,30,40,20)
        bullets.add(bullet)

class Enemy (GameSprite):
    def update(self):
        self.rect.y += self.speed
        global globsus
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randint(30, 400)
            globsus += 1

class Bullet (GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()


sprite1 = Player("pudge.png", 20, 380, 15, 400, 150)

globsus = 0
monsters = sprite.Group()
for i in range (1, 6):
    monster = Enemy ("Без названия3.png", randint(0, 700), randint(10, 30), randint (5,10), 50, 50)
    monsters.add(monster)



bullets = sprite.Group()






mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_music = mixer.Sound('fire.ogg')

background = transform.scale(image.load("Без названия.jpg"), (700, 500))
game = True
FPS = 30
finish = False
clock = time.Clock()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                sprite1.fire()
                fire_music.play()



    if not finish:
        window.blit(background, (0, 0))
        text = font.render("Missed Enemy's:" + str(globsus),1,(255,255,255))
        window.blit(text, (10, 10))
        text1 = font.render("Your social rating points:" + str(schet ),1,(255,255,255))
        window.blit(text1, (10, 50))
        sprite1.update()
        monsters.update()
       
        monsters.draw(window)
        sprite1.reset()
        bullets.update()
        bullets.draw(window)

        if sprite.spritecollide(sprite1, monsters, False) or globsus >= 10:
            finish = True
            window.blit(lose, (200, 250))
            

        
        BABAX_AHAHAHAHAAHAH = sprite.groupcollide(monsters, bullets, True, True)
        for i in BABAX_AHAHAHAHAAHAH:
            schet = schet + 1
            monster = Enemy ("Без названия3.png", randint(0, 700), randint(10, 30), randint (1,2), 50, 50)
            monsters.add(monster)
     
        if schet >= 5:
            finish = True
            window.blit(win, (200, 250))

        

        
    display.update()
    clock.tick(FPS)











