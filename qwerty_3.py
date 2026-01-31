import pygame, sys, gif_pygame

if __name__ == "__main__":
    win = pygame.display.set_mode((512, 512))
    gif = gif_pygame.load("images/анимация_котла.gif")

    while True:
        win.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gif.render(win, (128 - gif.get_width() * 0.5, 256 - gif.get_height() * 0.5))

        pygame.display.update()
