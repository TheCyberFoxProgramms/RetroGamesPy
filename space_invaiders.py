import pygame
from GameOver import game_over_main
from GameWin import game_win_main
from random import choice

def space_invaiders_main():
    pygame.init()
    pygame.display.set_caption('Retro Games')
    size = Width, Height = 894, 732
    screen = pygame.display.set_mode(size)
    FPS = 60
    clock = pygame.time.Clock()
    MYEVENTTYPE = pygame.USEREVENT + 1
    pygame.time.set_timer(MYEVENTTYPE, 300)
    check_position = False
    all_enamy = 23
    count = 0
    count2 = None
    with open('data/database/RaitingDb.txt', encoding='utf-8') as f:
        count2 = f.read().rstrip().split(',')
    game_exit = None
    running = True
    space_invaiders_fon = pygame.image.load('data/image/space_invaiders/space_invaiders_fon.png')

    gg_sprite_group = pygame.sprite.Group()
    enamy_sprite_group = pygame.sprite.Group()
    wall_sprite_group = pygame.sprite.Group()
    floor_sprite_group = pygame.sprite.Group()
    bullet_sprite_group = pygame.sprite.Group()
    bullet_enamy_sprite_group = pygame.sprite.Group()

    def run_menu_musik():
        pygame.mixer.music.load('data/sounds/space_invaiders/space_invaiders.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)

    run_menu_musik()

    blust_sound = pygame.mixer.Sound('data/sounds/space_invaiders/blaster.ogg')
    blust_sound.set_volume(0.6)

    size_font = 24
    game_font = pygame.font.Font(r'data/Minecraft Seven_2.ttf', size_font)


    class Gg(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.left_move = False
            self.right_move = False
            self.image = pygame.image.load('data/image/space_invaiders/gg.png')
            self.rect = self.image.get_rect()
            self.rect.x = 422
            self.rect.y = 682

        def update(self, *args, **kwargs):
            if self.left_move:
                if self.rect.x > 0:
                    self.rect.x -= 5
            if self.right_move:
                if self.rect.x + 50 < Width:
                    self.rect.x += 5
            if args and args[0] == 'left1':
                self.left_move = True
            elif args and args[0] == 'right1':
                self.right_move = True
            elif args and args[0] == 'left0':
                self.left_move = False
            elif args and args[0] == 'right0':
                self.right_move = False

    class Wall(pygame.sprite.Sprite):
        def __init__(self, pos_x):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((10, Height))
            self.rect = self.image.get_rect()
            self.rect.x = pos_x
            self.rect.y = 0


    class Floor(pygame.sprite.Sprite):
        def __init__(self, pos_y):
            pygame.sprite.Sprite.__init__(self)
            self.surf = pygame.Surface((Width, 1))
            self.surf.fill('green')
            self.image = self.surf
            self.rect = self.image.get_rect()
            self.rect.x = 0
            self.rect.y = pos_y

    class Bullet(pygame.sprite.Sprite):
        def __init__(self, gg_pos):
            pygame.sprite.Sprite.__init__(self)
            self.surf = pygame.Surface((5, 15))
            self.surf.fill('green')
            self.image = self.surf
            self.rect = self.image.get_rect()
            self.rect.x = gg_pos - 3
            self.rect.y = 680

        def update(self, *args, **kwargs):
            self.rect.y -= 10

    class BulletEnamy(pygame.sprite.Sprite):
        def __init__(self, gg_pos_x, gg_pos_y):
            pygame.sprite.Sprite.__init__(self)
            self.surf = pygame.Surface((15, 5))
            self.surf.fill('green')
            self.image = self.surf
            self.rect = self.image.get_rect()
            self.rect.x = gg_pos_x - 3
            self.rect.y = gg_pos_y

        def update(self, *args, **kwargs):
            nonlocal game_exit
            self.rect.y += 10
            if pygame.sprite.spritecollideany(self, gg_sprite_group):
                count2[1] = str(int(count2[1]) + count)
                with open('data/database/RaitingDb.txt', 'w', encoding='utf-8') as f:
                    f.write(','.join(count2))
                status = game_over_main()
                if status == 1:
                    game_exit = 1
                elif status == 2:
                    game_exit = 2
                elif status == 0:
                    game_exit = 0

    class Enamy(pygame.sprite.Sprite):
        def __init__(self, pos_x, pos_y):
            pygame.sprite.Sprite.__init__(self)
            self.sprites_img = list()
            self.check_position = False
            self.sprites_img.append(pygame.image.load(r'data/image/space_invaiders/enamy/inv1.png'))
            self.sprites_img.append(pygame.image.load(r'data/image/space_invaiders/enamy/inv2.png'))
            self.sprites_img.append(pygame.image.load(r'data/image/space_invaiders/enamy/inv1.png'))
            self.count_sprites = 0
            self.image = self.sprites_img[self.count_sprites]
            self.rect = self.image.get_rect()
            self.rect.x = pos_x
            self.rect.y = pos_y

        def update(self, *args, **kwargs):
            nonlocal check_position
            nonlocal game_exit
            nonlocal count
            nonlocal count2
            if pygame.sprite.spritecollideany(self, wall_sprite_group):
                if check_position:
                    check_position = False
                else:
                    check_position = True
                move_y()
            if check_position:
                self.rect.x += 1
            else:
                self.rect.x -= 1
            self.count_sprites += 0.03
            if self.count_sprites > 2:
                self.count_sprites = 0
            self.image = self.sprites_img[int(self.count_sprites)]
            if pygame.sprite.spritecollideany(self, floor_sprite_group):
                count2[1] = str(int(count2[1]) + count)
                with open('data/database/RaitingDb.txt', 'w', encoding='utf-8') as f:
                    f.write(','.join(count2))
                status = game_over_main()
                if status == 1:
                    game_exit = 1
                elif status == 2:
                    game_exit = 2
                elif status == 0:
                    game_exit = 0
            for i in bullet_sprite_group:
                if self.rect.collidepoint(i.rect.center):
                    self.kill()
                    i.kill()
                    count += 1
            if count == all_enamy:
                count2[1] = str(int(count2[1]) + count)
                with open('data/database/RaitingDb.txt', 'w', encoding='utf-8') as f:
                    f.write(','.join(count2))
                status = game_win_main()
                if status == 1:
                    game_exit = 1
                elif status == 2:
                    game_exit = 2
                elif status == 0:
                    game_exit = 0



    gg_sprite_group.add(Gg())
    wall_sprite_group.add(Wall(-10))
    wall_sprite_group.add(Wall(Width))
    floor_sprite_group.add(Floor(640))


    size = 100
    for i in range(8):
        enamy_sprite_group.add(Enamy(size, 100))
        size += 100
    size = 150
    for i in range(7):
        enamy_sprite_group.add(Enamy(size, 200))
        size += 100
    size = 100
    for i in range(8):
        enamy_sprite_group.add(Enamy(size, 300))
        size += 100

    def move_y():
        for i in enamy_sprite_group:
            i.rect.y += 20
            if check_position:
                i.rect.x += 1
            else:
                i.rect.x -= 1



    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 2:
                    return 1

            if event.type == pygame.MOUSEMOTION:
                pass

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    gg_sprite_group.update('left1')
                if event.key == pygame.K_RIGHT:
                    gg_sprite_group.update('right1')
                if event.key == pygame.K_SPACE:
                    bullet_sprite_group.add(Bullet(gg_sprite_group.sprites()[0].rect.centerx))
                    blust_sound.play()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    gg_sprite_group.update('left0')
                if event.key == pygame.K_RIGHT:
                    gg_sprite_group.update('right0')

            if event.type == MYEVENTTYPE:
                bullet_enamy_sprite_group.add(BulletEnamy(choice(enamy_sprite_group.sprites()).rect.centerx,
                                                          choice(enamy_sprite_group.sprites()).rect.centery))

        screen.fill((0, 0, 0))
        screen.blit(space_invaiders_fon, (0, 0))

        gg_sprite_group.draw(screen)
        gg_sprite_group.update()

        wall_sprite_group.draw(screen)
        floor_sprite_group.draw(screen)

        enamy_sprite_group.update()
        enamy_sprite_group.draw(screen)

        bullet_sprite_group.draw(screen)
        bullet_sprite_group.update()

        bullet_enamy_sprite_group.draw(screen)
        bullet_enamy_sprite_group.update()

        screen.blit(game_font.render(f'Уничтожено {count}', 1, 'green'), (10, 0))
        screen.blit(game_font.render(f'уничтожено за все время {count2[1]}', 1, 'green'), (10, 40))


        if game_exit == 1:
            return 1
        elif game_exit == 0:
            running = False
        elif game_exit == 2:
            return 666
        pygame.display.flip()
        clock.tick(FPS)
    return 0


if __name__ == '__main__':
    space_invaiders_main()