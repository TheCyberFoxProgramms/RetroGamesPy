import pygame


def game_raiting_main():
    pygame.init()
    pygame.display.set_caption('Retro Games')
    size = Width, Height = 894, 732
    screen = pygame.display.set_mode(size)
    FPS = 60
    clock = pygame.time.Clock()
    running = True

    def run_menu_musik():
        pygame.mixer.music.load('data/sounds/general_music/raiting_sound.wav')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(1)

    run_menu_musik()

    click1 = pygame.mixer.Sound('data/sounds/main_menu/click1.ogg')
    click2 = pygame.mixer.Sound('data/sounds/main_menu/click2.ogg')
    click1.set_volume(0.4)
    click2.set_volume(0.6)
    click1_play = True
    click1_2_play = True

    def read_db():
        with open('data/database/RaitingDb.txt', encoding='utf-8') as file:
            return tuple(map(int, file.read().rstrip().split(',')))

    rait1, rait2, rait3 = read_db()

    img_game_raiting = pygame.image.load(r'data/image/raiting/fon_raiting.png')

    size_font = 35
    game_font = pygame.font.Font(r'data/Minecraft Seven_2.ttf', size_font)
    game_text1 = game_font.render('Сбросить', 1, 'green')
    game_text2 = game_font.render('Вернуться в меню', 1, 'green')

    def rait_text_update():
        rait_text1 = game_font.render(f'Puckman: {rait1} op', 1, 'green')
        rait_text2 = game_font.render(f'Space Invaders: {rait2} op', 1, 'green')
        rait_text3 = game_font.render(f'Space Drive: {rait3} op', 1, 'green')
        return rait_text1, rait_text2, rait_text3

    rait_text1, rait_text2, rait_text3 = rait_text_update()

    def render_text(screen):
        screen.blit(game_text1, (50, 500))
        screen.blit(game_text2, (50, 600))
        screen.blit(rait_text1, (50, 100))
        screen.blit(rait_text2, (50, 200))
        screen.blit(rait_text3, (50, 300))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and (50 < event.pos[0] < 279) and (508 < event.pos[1] < 551):
                    click2.play()
                    with open('data/database/RaitingDb.txt', 'w', encoding='utf-8') as file:
                        file.write('0,0,0')
                    rait1, rait2, rait3 = read_db()
                    rait_text1, rait_text2, rait_text3 = rait_text_update()

                if event.button == 1 and (50 < event.pos[0] < 483) and (609 < event.pos[1] < 654):
                    click2.play()
                    return 1

            if event.type == pygame.MOUSEMOTION:
                if (50 < event.pos[0] < 279) and (508 < event.pos[1] < 551):
                    game_font = pygame.font.Font(r'data/Minecraft Seven_2.ttf', 45)
                    game_text1 = game_font.render('Сбросить', 1, 'green')
                    if click1_play:
                        click1.play()
                        click1_play = False
                else:
                    game_font = pygame.font.Font(r'data/Minecraft Seven_2.ttf', 35)
                    game_text1 = game_font.render('Сбросить', 1, 'green')
                    click1_play = True

                if (50 < event.pos[0] < 483) and (609 < event.pos[1] < 654):
                    game_font = pygame.font.Font(r'data/Minecraft Seven_2.ttf', 45)
                    game_text2 = game_font.render('Вернуться в меню', 1, 'green')
                    if click1_2_play:
                        click1.play()
                        click1_2_play = False
                else:
                    game_font = pygame.font.Font(r'data/Minecraft Seven_2.ttf', 35)
                    game_text2 = game_font.render('Вернуться в меню', 1, 'green')
                    click1_2_play = True

        screen.fill((0, 0, 0))
        screen.blit(img_game_raiting, (0, 0))
        render_text(screen)
        pygame.display.flip()
        clock.tick(FPS)
    return 0


if __name__ == '__main__':
    game_raiting_main()
