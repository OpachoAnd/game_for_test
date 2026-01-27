import pygame
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, 'images', 'hero.jpg')


if __name__ == '__main__':
    pygame.init()
    # Окно
    screen = pygame.display.set_mode((800, 600))
    WIDTH, HEIGHT = 800, 600
    pygame.display.set_caption('первая игра c персонажем')
    # Для анимации start
    animation_frames = []
    for i in range(1, 3):
        frame_path = os.path.join(current_dir, 'images', f'sprite_{i}.png')
        frame = pygame.image.load(frame_path).convert_alpha()
        animation_frames.append(frame)


    current_frame = 0
    animation_speed = 0.2  # Скорость смены кадров в секундах
    animation_timer = 0
    # Для анимации end

    clock = pygame.time.Clock()



    # Спрайт персонажа
    character_image = pygame.image.load(image_path).convert_alpha()
    character_image = pygame.transform.scale(character_image, (100, 100))

    # Настройки персонажа:
    player_size = 50
    player_x = WIDTH // 2 - player_size // 2
    player_y = HEIGHT // 2 - player_size // 2
    player_speed = 5

    # Цвета
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    run = True
    while run:
        clock.tick(60)  # Ограничение FPS до 60 кадров
        mouse_x, mouse_y = None, None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print('клик по', mouse_x, mouse_y)

        keys = pygame.key.get_pressed()
        if mouse_x and mouse_y:
            player_x = mouse_x
            player_y = mouse_y

            # Обновление анимации start
            dt = clock.tick(60) / 1000
            animation_timer += dt
            if animation_timer >= animation_speed:
                animation_timer = 0
                current_frame = (current_frame + 1) % len(animation_frames)
            # Обновление анимации end

        else:
            if keys[pygame.K_a] and player_x > 0:
                player_x -= player_speed
                # Обновление анимации start
                dt = clock.tick(60) / 1000
                print('dt', dt)
                print('animation_speed', animation_speed)
                exit(1)
                animation_timer += dt
                if animation_timer >= animation_speed:
                    animation_timer = 0
                    current_frame = (current_frame + 1) % len(animation_frames)
                # Обновление анимации end

            if keys[pygame.K_d] and player_x < WIDTH - player_size:
                player_x += player_speed
                # Обновление анимации start
                dt = clock.tick(60) / 1000
                animation_timer += dt
                if animation_timer >= animation_speed:
                    animation_timer = 0
                    current_frame = (current_frame + 1) % len(animation_frames)
                # Обновление анимации end
            if keys[pygame.K_w] and player_y > 0:
                player_y -= player_speed
                # Обновление анимации start
                dt = clock.tick(60) / 1000
                animation_timer += dt
                if animation_timer >= animation_speed:
                    animation_timer = 0
                    current_frame = (current_frame + 1) % len(animation_frames)
                # Обновление анимации end
            if keys[pygame.K_s] and player_y < HEIGHT - player_size:
                player_y += player_speed
                # Обновление анимации start
                dt = clock.tick(60) / 1000
                animation_timer += dt
                if animation_timer >= animation_speed:
                    animation_timer = 0
                    current_frame = (current_frame + 1) % len(animation_frames)
                # Обновление анимации end


        # Отрисовка
        screen.fill(WHITE)  # Заливка фона
        screen.blit(animation_frames[current_frame], (player_x, player_y))
        # screen.blit(character_image, (player_x, player_y))
        # pygame.draw.rect(screen, RED, (player_x, player_y, player_size, player_size))  # Персонаж
        pygame.display.flip()

    pygame.quit()




