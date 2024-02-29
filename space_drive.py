import pygame
from random import randint

def space_drive_main():
    pygame.init()
    pygame.display.set_caption('Retro Games')
    size = Width, Height = 894, 732
    screen = pygame.display.set_mode(size)
    FPS = 60
    clock = pygame.time.Clock()
    image_fon_pos1 = [0, 0]
    GG_CAR_X, GG_CAR_Y = 390, 550
    score = 0
    running = True

    gg_group = pygame.sprite.Group()
    enamy_group = pygame.sprite.Group()
    effects_group = pygame.sprite.Group()

    class Gg(pygame.sprite.Sprite):
        def __init__(self, pos_x, pos_y):
            pygame.sprite.Sprite.__init__(self)
            self.sprites_img = list()
            self.animation = False
            self.move = None
            self.sprites_img.append(pygame.image.load(r'data/image/space_driver/deiver1.png'))
            self.sprites_img.append(pygame.image.load(r'data/image/space_driver/deiver2.png'))
            self.sprites_img.append(pygame.image.load(r'data/image/space_driver/deiver3.png'))
            self.sprites_img.append(pygame.image.load(r'data/image/space_driver/deiver1.png'))
            self.count_sprites = 0
            self.image = self.sprites_img[self.count_sprites]
            self.rect = self.image.get_rect()
            self.rect.x = pos_x
            self.rect.y = pos_y

        def update(self, *args, **kwargs):
            if args:
                self.animation = True
                self.move = args[0]
            if self.count_sprites >= 4:
                self.count_sprites = 0
                self.animation = False
                self.move = None

            if self.animation:
                self.image = self.sprites_img[int(self.count_sprites)]
                self.count_sprites += 0.1
                if self.move == 'right' and self.rect.x < 510:
                    self.rect.x += 3
                elif self.move == 'left' and self.rect.x > 270:
                    self.rect.x -= 3

    gg_group.add(Gg(GG_CAR_X, GG_CAR_Y))

    class Effects(pygame.sprite.Sprite):
        def __init__(self, pos_x, pos_y, dlina):
            pygame.sprite.Sprite.__init__(self)
            self.move = False
            self.surf = pygame.Surface((10, dlina))
            self.surf.fill('green')
            self.image = self.surf
            self.rect = self.image.get_rect()
            self.pos_x = pos_x
            self.rect.x = -30
            self.rect.y = pos_y

        def update(self, *args, **kwargs):
            if args and args[0]:
                self.move = True
            elif args and not args[0]:
                self.move = False
            if self.move:
                self.rect.x = self.pos_x
            else:
                self.rect.x = -30
            self.rect.y += 60
            if self.rect.y > Height:
                self.rect.y = randint(-1000, -310)



    for _ in range(30):
        effects_group.add(Effects(randint(0, 250), randint(-1000, -310), randint(100, 300)))
    for _ in range(30):
        effects_group.add(Effects(randint(610, Width), randint(-1000, -310), randint(100, 300)))

    def run_menu_musik():
        pygame.mixer.music.load('data/sounds/space_driver/space_driver.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)

    run_menu_musik()
    image_space_drive1 = pygame.image.load('data/image/space_driver/space_drive_fon.png')

    def render_image_fons(screen):
        screen.blit(image_space_drive1, image_fon_pos1)
        screen.blit(image_space_drive1, (image_fon_pos1[0], image_fon_pos1[1] - Height))
        image_fon_pos1[1] += 1
        if image_fon_pos1[1] > Height:
            image_fon_pos1[1] = 0

    # click1 = pygame.mixer.Sound('data/sounds/main_menu/click1.ogg')
    # click1.set_volume(0.4)

    size_font = 25
    game_font = pygame.font.Font(r'data/Minecraft Seven_2.ttf', size_font)


    def render_text(screen):
        pass

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 2:
                    return 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    gg_group.update('right')
                if event.key == pygame.K_LEFT:
                    gg_group.update('left')
                if event.key == pygame.K_UP:
                    effects_group.update(True)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    effects_group.update(False)

        screen.fill((0, 0, 0))
        render_image_fons(screen)
        screen.blit(game_font.render(f'Пролетел: {score} св/л', 1, 'green'), (10, 0))
        screen.blit(game_font.render(f'Предыдущий рекорд: 0 св/л', 1, 'green'), (10, 40))
        score += 1
        gg_group.draw(screen)
        gg_group.update()
        effects_group.draw(screen)
        effects_group.update()
        pygame.display.flip()
        clock.tick(FPS)
    return 0

if __name__ == '__main__':
    space_drive_main()