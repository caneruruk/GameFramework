import pygame

class App:
    def __init__(self):
        pygame.init()
        self.__surface = pygame.display.set_mode((500, 500))
        pygame.display.set_caption('Window')
        self.__bg_color = (0, 0, 0)
        
    def run(self):
        while True:
            self.__render()
            self.__handle_input()
            self.__update()
    
    def __render(self):
        self.__surface.fill(self.__bg_color)
        
        pygame.display.update()
        
    def __handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    
    def __update(self):
        pass