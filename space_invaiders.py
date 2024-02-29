import pygame


def space_invaiders_main():
    pygame.init()
    pygame.display.set_caption('Retro Games')
    size = Width, Height = 894, 732
    screen = pygame.display.set_mode(size)
    FPS = 60
    clock = pygame.time.Clock()
    running = True
    space_invaiders_fon = pygame.image.load('data/image/space_invaiders/space_invaiders_fon.png')

    gg_sprite_group = pygame.sprite.Group()
    enamy_sprite_group = pygame.sprite.Group()
    wall_sprite_group = pygame.sprite.Group()
    floor_sprite_group = pygame.sprite.Group()

    def run_menu_musik():
        pygame.mixer.music.load('data/sounds/space_invaiders/space_invaiders.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)

    run_menu_musik()

    blust_sound = pygame.mixer.Sound('data/sounds/space_invaiders/blaster.ogg')
    blust_sound.set_volume(0.6)

    def read_db():
        with open('data/database/RaitingDb.txt', encoding='utf-8') as file:
            return tuple(map(int, file.read().rstrip().split(',')))

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


    gg_sprite_group.add(Gg())
    wall_sprite_group.add(Wall(-10))
    wall_sprite_group.add(Wall(Width))
    floor_sprite_group.add(Floor(640 ))

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
                    print(666)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    gg_sprite_group.update('left0')
                if event.key == pygame.K_RIGHT:
                    gg_sprite_group.update('right0')

        screen.fill((0, 0, 0))
        screen.blit(space_invaiders_fon, (0, 0))

        gg_sprite_group.draw(screen)
        gg_sprite_group.update()

        wall_sprite_group.draw(screen)
        floor_sprite_group.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)
    return 0


if __name__ == '__main__':
    space_invaiders_main()