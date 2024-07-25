import pygame, os

class StartScreen:
    def __init__(self, screen):
        self.screen = screen
        self.screen_width = 800
        self.screen_height = 600
        self.background = pygame.image.load('Globe.jpg')
        self.background = pygame.transform.scale(self.background, (self.screen_width, self.screen_height))
        font_path = os.path.join(os.path.dirname(__file__), 'fonts', 'BonaNovaSC-Bold.ttf')
        self.title_font = pygame.font.Font(font_path, 72)
        self.start_button_font = pygame.font.Font(None, 28)
        self.start_button_width = 200
        self.start_button_height = 50
        self.start_button_rect = pygame.Rect(self.screen_width // 2 - self.start_button_width // 2, self.screen_height // 2 + 200, self.start_button_width, self.start_button_height)
    
    def display(self):
        self.screen.blit(self.background, (0, 0))
        white = (255, 255, 255)
        title_text = self.title_font.render("Country Quiz Game", True, white)
        self.screen.blit(title_text, (self.screen_width // 2 - title_text.get_width() // 2, 40))
        dark_green = (0,90,0)
        light_green = (0,140,0)
        
        mouse_pos = pygame.mouse.get_pos()
        if self.start_button_rect.collidepoint(mouse_pos):
            start_button_color = light_green
        else:
            start_button_color = dark_green

        pygame.draw.rect(self.screen, start_button_color, self.start_button_rect)
        start_button_text = self.start_button_font.render("Take the Quiz", True, white)
        self.screen.blit(start_button_text, (self.start_button_rect.x + self.start_button_width // 2 - start_button_text.get_width() // 2, self.start_button_rect.y + self.start_button_height // 2 - start_button_text.get_height() // 2))
    