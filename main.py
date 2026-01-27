import gif_pygame
import pygame

from loader_images import bg_image, aspi_sit_image, aspi_jump_image

WIDTH, HEIGHT = 800, 600
pygame.init()
clock = pygame.time.Clock()

# Окно
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Лягушонок Аспи и Тагаширская Ведьма')

if __name__ == '__main__':
    temp_cauldron = 50  # Температура котла Тагаширской Ведьмы

    # Шрифт для Температуры
    temp_font = pygame.font.Font(None, 30)

    # Шрифт для Кнопки
    button_font = pygame.font.Font(None, 18)
    # Поверхность кнопки
    button_surface = pygame.Surface((150, 50))
    # Отображение текста на кнопке
    text_button = button_font.render("Увеличить температуру", True, (255, 255, 255))
    text_button_rect = text_button.get_rect(center=(button_surface.get_width() / 2,
                                                    button_surface.get_height() / 2))
    button_rect = pygame.Rect(10, 50, 50, 50)

    # Фоновый экран
    bg_image = bg_image.convert_alpha()  # Конвертация в альфа канал
    bg_image = pygame.transform.scale(bg_image, (800, 600))  # Изменение размера изображения

    # Спрайты и Ректы персонажей
    aspi_sit_sprite = aspi_sit_image.convert_alpha()
    aspi_sit_sprite = pygame.transform.scale(aspi_sit_sprite, (70, 70))
    aspi_sit_rect_1 = aspi_sit_sprite.get_rect(center=(400, 285))
    aspi_sit_rect_1 = pygame.Rect(aspi_sit_rect_1)

    aspi_jump_sprite = aspi_jump_image.convert_alpha()
    aspi_jump_sprite = pygame.transform.scale(aspi_jump_sprite, (70, 70))
    aspi_jump_rect_1 = aspi_jump_sprite.get_rect(center=(500, 250))
    aspi_jump_rect_1 = pygame.Rect(aspi_jump_rect_1)

    # Анимация котла
    gif = gif_pygame.load("images/анимация_котла.gif")

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # Проверяем событие нажатия кнопки мыши
            if event.type == pygame.MOUSEBUTTONDOWN: #and event.button == 1:
                # Вызовите функцию on_mouse_button_down()
                if button_rect.collidepoint(event.pos):
                    print("Button clicked!")
                    temp_cauldron += 5


        clock.tick(60)  # Ограничение FPS до 60 кадров
        screen.fill((255, 255, 255))  # Заливка фона, цвет - белый

        # Текст с температурой
        temp_text = temp_font.render(f"Температура в котле {temp_cauldron} C°", True, (0, 0, 0))
        # Текст на кнопке
        button_surface.blit(text_button, text_button_rect)

        # Рендер
        if temp_cauldron >= 70:
            screen.blit(aspi_jump_sprite, aspi_jump_rect_1)  # Размещение лягушонка Аспи высокая температура
        else:
            screen.blit(aspi_sit_sprite, aspi_sit_rect_1)  # Размещение лягушонка Аспи норм температура

        gif.render(screen, (270, 200))
        screen.blit(temp_text, (10, 10))
        screen.blit(button_surface, button_rect)

        pygame.display.update()  # Обновление сцены
