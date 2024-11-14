import pygame
import random

def draw_grid(screen):
    color = "black"
    for x in range(0, 640, 32):
        pygame.draw.line(screen, color, (x, 0), (x, 512))
    for y in range(0, 512, 32):
        pygame.draw.line(screen, color, (0, y), (640, y))







def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        #screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))

        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        mole_image = pygame.image.load("mole.png")

        x_mole, y_mole = 0, 0

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x_mouse, y_mouse = event.pos
                    if (x_mole <= x_mouse < x_mole + 32 and y_mole <= y_mouse < y_mole + 32):
                        x_mole = random.randrange(0, 640, 32)
                        y_mole = random.randrange(0, 512, 32)

            screen.fill("light green")
            draw_grid(screen)
            screen.blit(mole_image, mole_image.get_rect(topleft=(x_mole,y_mole)))

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
