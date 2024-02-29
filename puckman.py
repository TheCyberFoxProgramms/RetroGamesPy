import pygame
from pprint import pprint

def puckman_main():
    pygame.init()
    pygame.display.set_caption('Retro Games')
    size = Width, Height = 894, 732
    screen = pygame.display.set_mode(size)
    FPS = 60
    clock = pygame.time.Clock()
    running = True

    game_map = None
    pygame.mixer.music.load('data/sounds/pucman/pucman_main.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    tails_sprites = pygame.sprite.Group()
    enamy_sprites = pygame.sprite.Group()
    item_sprites = pygame.sprite.Group()
    gg_sprites = pygame.sprite.Group()



    with open('data/maps/map3.txt') as f:
        game_map = f.read().split('\n')

    tile_images = {0: r'data/image/pucman/tail0.png',
                   1: 'data/image/pucman/tail1.png'}


    class Taile(pygame.sprite.Sprite):
        def __init__(self, tail_type, pos_x, pos_y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load(tile_images[tail_type])
            self.rect = self.image.get_rect()
            self.rect.x = pos_x
            self.rect.y = pos_y

    logic_mass = list()
    tails_pos_y = 0

    for index, value in enumerate(game_map):
        tails_pos_x = 0
        logic_mass_promt = list()
        for i, v in enumerate(value):
            if v == '.':
                tails_sprites.add(Taile(0, tails_pos_x, tails_pos_y))
                logic_mass_promt.append(0)
            elif v == '#':
                tails_sprites.add(Taile(1, tails_pos_x, tails_pos_y))
                logic_mass_promt.append(1)
            elif v == '@':
                tails_sprites.add(Taile(0, tails_pos_x, tails_pos_y))
                logic_mass_promt.append(2)
            elif v == '+':
                tails_sprites.add(Taile(0, tails_pos_x, tails_pos_y))
                logic_mass_promt.append(3)
            tails_pos_x += 50
        logic_mass.append(logic_mass_promt)
        tails_pos_y += 50

    pprint(logic_mass)

    def start_pos_gg(mod=False):
        for index, value in enumerate(logic_mass):
            for i, v in enumerate(value):
                if v == 2:
                    if mod:
                        return i, index
                    return i * 50, index * 50

    class Gg(pygame.sprite.Sprite):
        def __init__(self, pos_x, pos_y):
            pygame.sprite.Sprite.__init__(self)
            self.sprites_position = 1
            self.sprites_left = list()
            self.sprites_rigt = list()
            self.sprites_up = list()
            self.sprites_down = list()
            self.sprites_up.append(pygame.image.load(r'data/image/pucman/gg/1.png'))
            self.sprites_up.append(pygame.image.load(r'data/image/pucman/gg/1_1.png'))
            self.sprites_up.append(pygame.image.load(r'data/image/pucman/gg/1.png'))
            self.sprites_down.append(pygame.image.load(r'data/image/pucman/gg/2.png'))
            self.sprites_down.append(pygame.image.load(r'data/image/pucman/gg/2_2.png'))
            self.sprites_down.append(pygame.image.load(r'data/image/pucman/gg/2.png'))
            self.sprites_left.append(pygame.image.load(r'data/image/pucman/gg/3.png'))
            self.sprites_left.append(pygame.image.load(r'data/image/pucman/gg/3_3.png'))
            self.sprites_left.append(pygame.image.load(r'data/image/pucman/gg/3.png'))
            self.sprites_rigt.append(pygame.image.load(r'data/image/pucman/gg/4.png'))
            self.sprites_rigt.append(pygame.image.load(r'data/image/pucman/gg/4_4.png'))
            self.sprites_rigt.append(pygame.image.load(r'data/image/pucman/gg/4.png'))
            self.count_sprites = 0
            if self.sprites_position == 1:
                self.image = self.sprites_left[self.count_sprites]
                self.rect = self.image.get_rect()
                self.rect.x = pos_x
                self.rect.y = pos_y


        def update(self, *args, **kwargs):
            if self.count_sprites >= 2:
                self.count_sprites = 0
            self.count_sprites += 0.05
            if self.sprites_position == 1:
                self.image = self.sprites_left[int(self.count_sprites)]
            elif self.sprites_position == 2:
                self.image = self.sprites_rigt[int(self.count_sprites)]
            elif self.sprites_position == 3:
                self.image = self.sprites_up[int(self.count_sprites)]
            elif self.sprites_position == 4:
                self.image = self.sprites_down[int(self.count_sprites)]
            if args:
                self.sprites_position = args[0]
            if args and args[0] == 1:
                self.rect.x -= 50
            elif args and args[0] == 2:
                self.rect.x += 50
            elif args and args[0] == 3:
                self.rect.y -= 50
            elif args and args[0] == 4:
                self.rect.y += 50

    gg_sprites.add(Gg(*start_pos_gg()))

    class Enamy(pygame.sprite.Sprite):
        def __init__(self, pos_x, pos_y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load(r'data/image/pucman/puck_enamy.png')
            self.rect = self.image.get_rect()
            self.rect.x = pos_x
            self.rect.y = pos_y

    for index, value in enumerate(logic_mass):
        for i, v in enumerate(value):
            if v == 3:
                enamy_sprites.add(Enamy(i * 50, index * 50))

    def check_move(x):
        if x == 1:
            old_pos = start_pos_gg(mod=True)
            print(old_pos)
            if logic_mass[old_pos[1]][old_pos[0] - 1] == 0:
                logic_mass[old_pos[1]][old_pos[0]] = 0
                logic_mass[old_pos[1]][old_pos[0] - 1] = 2
                return True
            else:
                return False
        if x == 2:
            old_pos = start_pos_gg(mod=True)
            print(old_pos)
            if logic_mass[old_pos[1]][old_pos[0] + 1] == 0:
                logic_mass[old_pos[1]][old_pos[0]] = 0
                logic_mass[old_pos[1]][old_pos[0] + 1] = 2
                return True
            else:
                return False
        if x == 3:
            old_pos = start_pos_gg(mod=True)
            print(old_pos)
            if logic_mass[old_pos[1] - 1][old_pos[0]] == 0:
                logic_mass[old_pos[1]][old_pos[0]] = 0
                logic_mass[old_pos[1] - 1][old_pos[0]] = 2
                return True
            else:
                return False
        if x == 4:
            old_pos = start_pos_gg(mod=True)
            print(old_pos)
            if logic_mass[old_pos[1] + 1][old_pos[0]] == 0:
                logic_mass[old_pos[1]][old_pos[0]] = 0
                logic_mass[old_pos[1] + 1][old_pos[0]] = 2
                return True
            else:
                return False


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 2:
                    return 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if check_move(1):
                        gg_sprites.update(1)
                if event.key == pygame.K_RIGHT:
                    if check_move(2):
                        gg_sprites.update(2)
                if event.key == pygame.K_UP:
                    if check_move(3):
                        gg_sprites.update(3)
                if event.key == pygame.K_DOWN:
                    if check_move(4):
                        gg_sprites.update(4)



        screen.fill((0, 0, 0))
        tails_sprites.draw(screen)
        gg_sprites.draw(screen)
        gg_sprites.update()
        enamy_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
    return 0

if __name__ == '__main__':
    puckman_main()
