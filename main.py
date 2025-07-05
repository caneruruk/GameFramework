import pygame

if __name__ == "__main__":
    pygame.init()
    surface = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Window")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        surface.fill((0, 0, 0))
        
        pygame.display.update()