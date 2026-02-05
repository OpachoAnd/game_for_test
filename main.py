import gif_pygame
import numpy as np
import pygame

from loader_images import bg_image, aspi_sit_image, aspi_jump_image, null_square_image, core_character_image

WIDTH, HEIGHT = 900, 900  # Размеры окна
pygame.init()
clock = pygame.time.Clock()

# Окно
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Лягушонок Аспи и Тагаширская Ведьма')

# Фоновый экран
bg_image = bg_image.convert_alpha()  # Конвертация в альфа канал
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))  # Изменение размера изображения

# Квадратик нулевого поля
null_sqr_image = null_square_image.convert_alpha()
# Квадратик главного героя
core_character_image = core_character_image.convert_alpha()

"""
    0 - пустая клетка
    1 - персонаж Аспи
    2 - NPC
    3 - река - перенесет в следующую клетку
    4 - воспоминание - заставит вспомнить эпизод из жизни
    5 - сундук - какие то предметы
    6 - дремучие заросли - +1 ХП
    7 - котёл Тагаширской ведьмы - переносит Аспи к Тагаширской ведьме
    8 - Тагаширская ведьма 
"""
game_board = np.array([
    [0, 0, 0,  0, 0, 0,  0, 0, 0],
    [0, 0, 0,  0, 0, 0,  0, 0, 0],
    [0, 2, 0,  0, 0, 0,  0, 0, 0],

    [0, 6, 6,  4, 5, 0,  0, 0, 0],
    [1, 0, 0,  0, 3, 0,  0, 0, 0],
    [0, 0, 0,  0, 3, 0,  0, 0, 0],

    [0, 0, 0,  0, 3, 0,  0, 0, 0],
    [0, 7, 0,  0, 2, 0,  0, 0, 0],
    [0, 0, 0,  0, 0, 0,  0, 8, 0]])

game_board_mask = np.array([
    [0, 0, 0,  0, 0, 0,  0, 0, 0],
    [0, 0, 0,  0, 0, 0,  0, 0, 0],
    [0, 0, 0,  0, 0, 0,  0, 0, 0],

    [0, 0, 0,  0, 0, 0,  0, 0, 0],
    [1, 0, 0,  0, 0, 0,  0, 0, 0],
    [0, 0, 0,  0, 0, 0,  0, 0, 0],

    [0, 0, 0,  0, 0, 0,  0, 0, 0],
    [0, 0, 0,  0, 0, 0,  0, 0, 0],
    [0, 0, 0,  0, 0, 0,  0, 0, 0]])

def draw_game_board():
    rows, cols = game_board_mask.shape
    size_square = min(WIDTH, HEIGHT) // max(rows, cols)
    count_y = 0
    count_x = 0
    for i in range(0, rows):
        for j in range(0, cols):
            x, y = i * size_square, j * size_square
            
            if game_board_mask[j, i] == 0:
                screen.blit(null_sqr_image, (x + count_x, y + count_y))
            if game_board_mask[j, i] == 1:
                screen.blit(core_character_image, (x + count_x, y + count_y))

            count_y += 1
        count_y = 0
        count_x += 1


if __name__ == "__main__":
    draw_game_board()

    run = True
    while run:
        clock.tick(60)  # Ограничение FPS до 60 кадров

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Отрисовка игрового поля:

        # Обновление сцены
        pygame.display.update()
