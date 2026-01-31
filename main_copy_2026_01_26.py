import gif_pygame
import pygame
import os
import sys

from loader_images import bg_image, character_1_image, character_2_image, aspi_sit_image

WIDTH, HEIGHT = 800, 600
pygame.init()
clock = pygame.time.Clock()
# Окно
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Лягушонок Аспи и Тагаширская Ведьма')

if __name__ == '__main__':
    # Фоновый экран
    bg_image = bg_image.convert_alpha()  # Конвертация в альфа канал
    bg_image = pygame.transform.scale(bg_image, (800, 600))  # Изменение размера изображения

    # Картинки персонажей
    aspi_sprite = aspi_sit_image.convert_alpha()
    aspi_sprite = pygame.transform.scale(aspi_sprite, (70, 70))
    aspi_rect_1 = aspi_sprite.get_rect(center=(400, 285))
    aspi_rect_1 = pygame.Rect(aspi_rect_1)

    # Анимация котла
    # animation_cauldron = []
    # for i in range(1, 6):
    #     frame_path = f'animation/withs_cauldron_{i}.png'
    #     frame = pygame.image.load(frame_path).convert_alpha()
    #     animation_cauldron.append(frame)
    # current_frame = 0
    # animation_speed = 0.2  # Скорость смены кадров в секундах
    # animation_timer = 0
    gif = gif_pygame.load("images/анимация_котла.gif")

    run = True
    while run:
        # screen.blit(bg_image, (0, 0))  # Фоновый рисунок
        screen.fill((255, 255, 255))  # Заливка фона

        screen.blit(aspi_sprite, aspi_rect_1)  # Размещение лягушонка Аспи

        # screen.blit(character_sprite_1, character_rect_1)
        # screen.blit(character_sprite_2, character_rect_2)
        # screen.blit(character_sprite_1, (0, 0))
        # screen.blit(character_sprite_2, (200, 200))

        clock.tick(60)  # Ограничение FPS до 60 кадров
        mouse_x, mouse_y = None, None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Обновление анимации start

        # gif.render(screen, (128 - gif.get_width() * 0.5, 256 - gif.get_height() * 0.5))
        gif.render(screen, (270, 200))
        # dt = clock.tick(60) / 100
        # animation_timer += dt
        # if animation_timer >= animation_speed:
        #     animation_timer = 0
        #     current_frame = (current_frame + 1) % len(animation_cauldron)
        # screen.blit(animation_cauldron[current_frame], (200, 200))  # Отрисовка анимации
        # Обновление анимации end

        # if character_rect_1.colliderect(character_rect_2):
        #     print('пересечение')
        # else:
        #     print('нет пересечения')

        pygame.display.update()
