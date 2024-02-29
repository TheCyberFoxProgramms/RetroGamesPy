import pygame

def game_over_main():
    pygame.init()
    pygame.display.set_caption('Retro Games')
    size = Width, Height = 894, 732
    screen = pygame.display.set_mode(size)
    FPS = 60
    clock = pygame.time.Clock()
    running = True

    pygame.mixer.music.load('data/sounds/general_music/over.wav')
    pygame.mixer.music.play(1)
    pygame.mixer.music.set_volume(0.2)

    click1 = pygame.mixer.Sound('data/sounds/main_menu/click1.ogg')
    click2 = pygame.mixer.Sound('data/sounds/main_menu/click2.ogg')
    click1.set_volume(0.4)
    click2.set_volume(0.6)
    click1_play = True
    click1_2_play = True

    img_game_over = pygame.image.load(r'data/image/general_image/game_over.png')

    size_font = 35
    game_font = pygame.font.Font(r'data/Minecraft Seven_2.ttf', size_font)
    game_text1 = game_font.render('Повторить', 1, 'green')
    game_text2 = game_font.render('Вернутьсяь в меню', 1, 'green')

    def render_text(screen):
        screen.blit(game_text1, (330, 500))
        screen.blit(game_text2, (240, 600))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and (329 < event.pos[0] < 565) and (508 < event.pos[1] < 551):
                    click2.play()

                if event.button == 1 and (237 < event.pos[0] < 664) and (609 < event.pos[1] < 654):
                    click2.play()

            if event.type == pygame.MOUSEMOTION:
                if (329 < event.pos[0] < 565) and (508 < event.pos[1] < 551):
                    game_font = pygame.font.Font(r'data/Minecraft Seven_2.ttf', 45)
                    game_text1 = game_font.render('Повторить', 1, 'green')
                    if click1_play:
                        click1.play()
                        click1_play = False
                else:
                    game_font = pygame.font.Font(r'data/Minecraft Seven_2.ttf', 35)
                    game_text1 = game_font.render('Повторить', 1, 'green')
                    click1_play = True

                if (237 < event.pos[0] < 664) and (609 < event.pos[1] < 654):
                    game_font = pygame.font.Font(r'data/Minecraft Seven_2.ttf', 45)
                    game_text2 = game_font.render('Вернутьсяь в меню', 1, 'green')
                    if click1_2_play:
                        click1.play()
                        click1_2_play = False
                else:
                    game_font = pygame.font.Font(r'data/Minecraft Seven_2.ttf', 35)
                    game_text2 = game_font.render('Вернутьсяь в меню', 1, 'green')
                    click1_2_play = True


        screen.fill((0, 0, 0))
        screen.blit(img_game_over, (100, 50))
        render_text(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()

if __name__ == '__main__':
    game_over_main()
