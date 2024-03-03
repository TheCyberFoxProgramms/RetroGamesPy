import pygame
from puckman import puckman_main
from space_invaiders import space_invaiders_main
from Raiting import game_raiting_main
from uprav import uprav_main
from space_drive import space_drive_main

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Retro Games')
    size = Width, Height = 894, 732
    screen = pygame.display.set_mode(size)
    FPS = 60
    clock = pygame.time.Clock()
    running = True

    def run_menu_musik():
        pygame.mixer.music.load('data/sounds/main_menu/main_menu.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)

    run_menu_musik()

    click1 = pygame.mixer.Sound('data/sounds/main_menu/click1.ogg')
    click2 = pygame.mixer.Sound('data/sounds/main_menu/click2.ogg')
    click1.set_volume(0.4)
    click2.set_volume(0.6)
    click1_play = True
    click1_2_play = True
    click1_3_play = True
    click1_4_play = True
    click1_5_play = True

    img_main_menu = pygame.image.load(r'data/image/main_menu/main_menu.jpg')

    oblaco1 = pygame.image.load(r'data/image/main_menu/oblaco1.png')
    oblaco1_pos_x, oblaco1_pos_y = 10, 100

    oblaco2 = pygame.image.load(r'data/image/main_menu/oblaco2.png')
    oblaco2_pos_x, oblaco2_pos_y = 800, 250

    oblaco3 = pygame.image.load(r'data/image/main_menu/oblaco2.png')
    oblaco3_pos_x, oblaco3_pos_y = -300, 350

    size_font = 24
    game_font = pygame.font.Font(r'data/Minecraft Seven_2.ttf', size_font)
    game_text1 = game_font.render('Puckman', 1, 'green')
    game_text2 = game_font.render('Space Invaders', 1, 'green')
    game_text3 = game_font.render('Space Drive', 1, 'green')
    game_text4 = game_font.render('Ваш Рейтинг', 1, 'green')
    game_text5 = game_font.render('Как играть?', 1, 'green')


    def render_text(screen):
        screen.blit(game_text1, (100, 450))
        screen.blit(game_text2, (100, 500))
        screen.blit(game_text3, (100, 550))
        screen.blit(game_text4, (100, 650))
        screen.blit(game_text5, (370, 650))


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and (100 < event.pos[0] < 225) and (455 < event.pos[1] < 495):
                    click2.play()
                    status = puckman_main()
                    if not status:
                        running = False
                    run_menu_musik()

                if event.button == 1 and (100 < event.pos[0] < 335) and (505 < event.pos[1] < 545):
                    click2.play()
                    status = space_invaiders_main()
                    if not status:
                        running = False
                    run_menu_musik()

                if event.button == 1 and (100 < event.pos[0] < 275) and (557 < event.pos[1] < 595):
                    click2.play()
                    status = space_drive_main()
                    while True:
                        if status == 1:
                            break
                        if not status:
                            running = False
                            break
                        if status == 666:
                            status = space_drive_main()
                    run_menu_musik()

                if event.button == 1 and (100 < event.pos[0] < 280) and (650 < event.pos[1] < 700):
                    click2.play()
                    status = game_raiting_main()
                    if not status:
                        running = False
                    run_menu_musik()

                if event.button == 1 and (370 < event.pos[0] < 500) and (650 < event.pos[1] < 700):
                    click2.play()
                    status = uprav_main()
                    if not status:
                        running = False
                    run_menu_musik()

            if event.type == pygame.MOUSEMOTION:
                if (100 < event.pos[0] < 225) and (455 < event.pos[1] < 495):
                    game_font = pygame.font.Font(r'data/Minecraft Seven_2.ttf', 35)
                    game_text1 = game_font.render('Puckman', 1, 'green')
                    if click1_play:
                        click1.play()
                        click1_play = False
                else:
                    game_font = pygame.font.Font(r'data/Minecraft Seven_2.ttf', 24)
                    game_text1 = game_font.render('Puckman', 1, 'green')
                    click1_play = True

                if (100 < event.pos[0] < 335) and (505 < event.pos[1] < 545):
                    game_font = pygame.font.Font(r'data/Minecraft Seven_2.ttf', 35)
                    game_text2 = game_font.render('Space Invaders', 1, 'green')
                    if click1_2_play:
                        click1.play()
                        click1_2_play = False
                else:
                    game_font = pygame.font.Font(r'data/Minecraft Seven_2.ttf', 24)
                    game_text2 = game_font.render('Space Invaders', 1, 'green')
                    click1_2_play = True

                if (100 < event.pos[0] < 275) and (557 < event.pos[1] < 595):
                    game_font = pygame.font.Font(r'data/Minecraft Seven_2.ttf', 35)
                    game_text3 = game_font.render('Space Drive', 1, 'green')
                    if click1_3_play:
                        click1.play()
                        click1_3_play = False
                else:
                    game_font = pygame.font.Font(r'data/Minecraft Seven_2.ttf', 24)
                    game_text3 = game_font.render('Space Drive', 1, 'green')
                    click1_3_play = True

                if (100 < event.pos[0] < 280) and (650 < event.pos[1] < 700):
                    game_font = pygame.font.Font(r'data/Minecraft Seven_2.ttf', 35)
                    game_text4 = game_font.render('Ваш Рейтинг', 1, 'green')
                    if click1_4_play:
                        click1.play()
                        click1_4_play = False
                else:
                    game_font = pygame.font.Font(r'data/Minecraft Seven_2.ttf', 24)
                    game_text4 = game_font.render('Ваш Рейтинг', 1, 'green')
                    click1_4_play = True

                if (370 < event.pos[0] < 500) and (650 < event.pos[1] < 700):
                    game_font = pygame.font.Font(r'data/Minecraft Seven_2.ttf', 35)
                    game_text5 = game_font.render('Как играть?', 1, 'green')
                    if click1_5_play:
                        click1.play()
                        click1_5_play = False
                else:
                    game_font = pygame.font.Font(r'data/Minecraft Seven_2.ttf', 24)
                    game_text5 = game_font.render('Как играть?', 1, 'green')
                    click1_5_play = True

        screen.fill((0, 0, 0))
        screen.blit(img_main_menu, (0, 0))
        render_text(screen)

        screen.blit(oblaco1, (oblaco1_pos_x, oblaco1_pos_y))
        oblaco1_pos_x += 1
        if oblaco1_pos_x > 900:
            oblaco1_pos_x = -400

        screen.blit(oblaco2, (oblaco2_pos_x, oblaco2_pos_y))
        oblaco2_pos_x -= 0.6
        if oblaco2_pos_x < -300:
            oblaco2_pos_x = 900

        screen.blit(oblaco3, (oblaco3_pos_x, oblaco3_pos_y))
        oblaco3_pos_x += 0.3
        if oblaco3_pos_x > 900:
            oblaco3_pos_x = -400

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
