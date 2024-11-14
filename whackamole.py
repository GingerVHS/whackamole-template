import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        times = 0
        while running:
            times += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = event.pos
                    if click[0] // 32 == mole_x // 32 and click[1] // 32 == mole_y // 32: #checks if the click is where the mole is and if so a new mole_x and mole_y are set
                        mole_x = random.randrange(0, 19) * 32
                        mole_y = random.randrange(0, 15) * 32
            screen.fill("light green")
            for i in range(32, 609): #for drawing vertical lines
                if i % 32 == 0:
                    pygame.draw.line(screen, 'black', (i, 0), (i, 512))
            for i in range(32, 481): #for drawing horizontal lines
                if i % 32 == 0:
                    pygame.draw.line(screen, 'black', (0, i), (640, i))
            if times == 1: #sets the mole's initial position
                mole_x = 0
                mole_y = 0
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
