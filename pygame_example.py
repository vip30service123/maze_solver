import pygame
from sys import exit

def choose_suitable_position(coor):
    return (int(coor[0] / 50) * 50, int(coor[1] / 50) * 50)


pygame.init()
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

white_surface = pygame.Surface((50, 50))
white_surface.fill('White')

white_status = True

red_surface = pygame.Surface((50, 50))
red_surface.fill('Red')
blue_surface = pygame.Surface((50, 50))
blue_surface.fill('Blue')

text_font = pygame.font.Font(None, 50)
wall_text = text_font.render("Create wall", False, "White")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos)

            if white_status:
                white_status = False
                new_pos = choose_suitable_position(pos)
                screen.blit(white_surface, new_pos)
            else:
                white_status = True
                new_pos = choose_suitable_position(pos)
                screen.blit(red_surface, new_pos)

    screen.blit(wall_text, (0, 0))

    pygame.display.update()
    clock.tick(60) # Frame = 60