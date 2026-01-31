import pygame
import os
import sys

WIDTH, HEIGHT = 450, 450
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Цвета
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

# Настройка экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Крестики-нолики')
screen.fill(BG_COLOR)

pygame.init()


def draw_lines():
    # Горизонтальные линии
    pygame.draw.line(surface=screen,
                     color=LINE_COLOR,
                     start_pos=(0, SQUARE_SIZE),
                     end_pos=(WIDTH, SQUARE_SIZE),
                     width=LINE_WIDTH)
    pygame.draw.line(surface=screen,
                     color=LINE_COLOR,
                     start_pos=(0, 2 * SQUARE_SIZE),
                     end_pos=(WIDTH, 2 * SQUARE_SIZE),
                     width=LINE_WIDTH)
    # Вертикальные линии
    pygame.draw.line(surface=screen,
                     color=LINE_COLOR,
                     start_pos=(SQUARE_SIZE, 0),
                     end_pos=(SQUARE_SIZE, HEIGHT),
                     width=LINE_WIDTH)
    pygame.draw.line(surface=screen,
                     color=LINE_COLOR,
                     start_pos=(2 * SQUARE_SIZE, 0),
                     end_pos=(2 * SQUARE_SIZE, HEIGHT),
                     width=LINE_WIDTH)


def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                # Крестик
                pygame.draw.line(surface=screen,
                                 color=CROSS_COLOR,
                                 start_pos=(col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 end_pos=((col + 1) * SQUARE_SIZE - SPACE, (row + 1) * SQUARE_SIZE - SPACE),
                                 width=CROSS_WIDTH)
                pygame.draw.line(surface=screen,
                                 color=CROSS_COLOR,
                                 start_pos=((col + 1) * SQUARE_SIZE - SPACE, (row + 1) * SQUARE_SIZE - SPACE),
                                 end_pos=(col * SQUARE_SIZE + SPACE, (row + 1) * SQUARE_SIZE - SPACE),
                                 width=CROSS_WIDTH)
            elif board[row][col] == 2:
                # Нолик
                pygame.draw.circle(screen, CIRCLE_COLOR,
                                   (int(col * SQUARE_SIZE + SQUARE_SIZE // 2),
                                    int(row * SQUARE_SIZE + SQUARE_SIZE // 2)),
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)


# Проверка на победителя
def check_winner():
    # Проверка по горизонтали
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] != 0:
            return board[row][0]

    # Проверка по вертикали
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] != 0:
            return board[0][col]

    # Проверка по диагонали (сверху слева вниз вправо)
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]

    # Проверка по диагонали (сверху справа вниз влево)
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]

    # Проверка на ничью
    is_board_full = True
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                is_board_full = False
                break

    if is_board_full:
        return 'tie'  # Ничья
    return None  # Игра продолжается


if __name__ == '__main__':
    # Игровая доска: 0 - пусто, 1 - крестик, 2 - нолик
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    # Начинает игрок с крестиком
    player = 1

    # Основной игровой цикл
    draw_lines()

    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = pygame.mouse.get_pos()[0]  # x координата
                mouseY = pygame.mouse.get_pos()[1]  # y координата

                # Определяем, в какую клетку кликнули
                clicked_row = mouseY // SQUARE_SIZE
                clicked_col = mouseX // SQUARE_SIZE

                # Если клетка пуста – ставим фигуру
                if board[clicked_row][clicked_col] == 0:
                    board[clicked_row][clicked_col] = player

            # Проверка на победителя после хода
            winner = check_winner()
            if winner:
                game_over = True

            # Смена игрока
            player = 1 if player == 2 else 2

            # Перерисовка игровых объектов
            draw_figures()

            # Возможность перезапустить игру после завершения
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    screen.fill(BG_COLOR)
        draw_lines()
        player = 1
        board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        game_over = False

        pygame.display.update()
