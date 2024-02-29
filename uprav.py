import pygame

def uprav_main():
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

    image_uprav = pygame.image.load('data/image/raiting/fon_raiting.png')

    click1 = pygame.mixer.Sound('data/sounds/main_menu/click1.ogg')
    click2 = pygame.mixer.Sound('data/sounds/main_menu/click2.ogg')
    click1.set_volume(0.4)
    click2.set_volume(0.6)
    click1_play = True
    click1_2_play = True


    size_font = 35
    game_font = pygame.font.Font(r'data/Minecraft Seven_2.ttf', size_font)
    game_text1 = game_font.render('Сбросить', 1, 'green')
    game_text2 = game_font.render('Вернуться в меню', 1, 'green')

    rait_text1 = game_font.render(f'Puckman: Движение: Стрелочки (Вверх, Вниз, Влево, Вправо)', 1, 'green')
    rait_text1_1 = game_font.render(f'Вниз, Влево, Вправо)', 1, 'green')
    rait_text2 = game_font.render(f'Space Invaders: Движение: Стрелочки', 1, 'green')
    rait_text2_2 = game_font.render(f'(Влево, Вправо) Стрельба: Пробел', 1, 'green')
    rait_text3 = game_font.render(f'Space Drive: Движение: Стрелочки ', 1, 'green')
    rait_text3_3 = game_font.render(f'(Влево, Вправо) Ускорение: Вверх', 1, 'green')
    rait_text4 = game_font.render(f'Выйти из игры в главное меню:', 1, 'green')
    rait_text4_4 = game_font.render(f'(Средняя кнопка мыши)', 1, 'green')

    def render_text(screen):
        screen.blit(game_text2, (50, 600))

        screen.blit(rait_text1, (50, 20))
        screen.blit(rait_text1_1, (50, 70))
        screen.blit(rait_text2, (50, 170))
        screen.blit(rait_text2_2, (50, 220))
        screen.blit(rait_text3, (50, 320))
        screen.blit(rait_text3_3, (50, 370))
        screen.blit(rait_text4, (50, 450))
        screen.blit(rait_text4_4, (50, 500))


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and (50 < event.pos[0] < 483) and (609 < event.pos[1] < 654):
                    click2.play()
                    return 1

            if event.type == pygame.MOUSEMOTION:
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
        screen.blit(image_uprav, (0, 0))
        render_text(screen)
        pygame.display.flip()
        clock.tick(FPS)
    return 0


if __name__ == '__main__':
    uprav_main()