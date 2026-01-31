import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
rect1 = pygame.Rect(100, 100, 50, 50)
rect2 = pygame.Rect(120, 120, 50, 50)

if rect1.colliderect(rect2):
    print("Collision detected!")
else:
    print("No collision.")
pygame.quit()
