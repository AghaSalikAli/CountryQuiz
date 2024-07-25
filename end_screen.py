import pygame, os

class EndScreen:
    def __init__(self, screen):
        self.screen = screen
        self.screen_width = 800
        self.screen_height = 600
        self.score = 0
        text_font_path = os.path.join(os.path.dirname(__file__), 'fonts', 'BonaNovaSC-Bold.ttf')
        self.text_font = pygame.font.Font(text_font_path, 72)
        comment_font_path = os.path.join(os.path.dirname(__file__), 'fonts', 'BonaNovaSC-Regular.ttf')
        self.comment_font = pygame.font.Font(comment_font_path, 30)
        self.text = None
        self.comment = None
    
    def display(self, score):
        self.screen.fill((70,70,70))
        self.score = score
        self.text = self.text_font.render(f"Your Score: {self.score}/10", True, (255,255,255))
        self.screen.blit(self.text, (self.screen_width // 2 - self.text.get_width() // 2, self.screen_height // 2 - self.text.get_height() // 2))
        if self.score < 6:
            self.comment = self.comment_font.render("Maybe this game isnt for you..", True, (255,255,255))
        elif self.score < 9:
            self.comment = self.comment_font.render("Great job! Next time do better!", True, (255,255,255))
        else:
            self.comment = self.comment_font.render("Congrats! You're a know it all!", True, (255,255,255))
        self.screen.blit(self.comment, (self.screen_width // 2 - self.comment.get_width() // 2, self.screen_height // 2 + 100))