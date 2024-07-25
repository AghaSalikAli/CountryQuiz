import pygame
from start_screen import StartScreen
from quiz_screen import QuizScreen
from end_screen import EndScreen

class CountryQuizGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Country Quiz Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = "start"  
        self.start_screen = StartScreen(self.screen)
        self.quiz_screen = QuizScreen(self.screen)
        self.end_screen = EndScreen(self.screen)

    def run(self): 
        while self.running:
            if self.state == "start":
                self.start_screen.display()
                self.handle_start_events()
            elif self.state == "quiz":
                self.quiz_screen.display()
                self.handle_quiz_events()
            elif self.state == "end":
                self.end_screen.display(self.quiz_screen.score[0])
                self.handle_end_events()
            pygame.display.flip()
            self.clock.tick(60)

    def handle_start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_screen.start_button_rect.collidepoint(event.pos):
                    self.state = "quiz"

    def handle_quiz_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.quiz_screen.option_button_rects[0].collidepoint(event.pos):
                    self.quiz_screen.answered = 0
                elif self.quiz_screen.option_button_rects[1].collidepoint(event.pos):
                    self.quiz_screen.answered = 1
                elif self.quiz_screen.option_button_rects[2].collidepoint(event.pos):
                    self.quiz_screen.answered = 2
                elif self.quiz_screen.option_button_rects[3].collidepoint(event.pos):
                    self.quiz_screen.answered = 3
        if self.quiz_screen.completed:
            self.state = "end"
            self.quiz_screen.completed = False

    def handle_end_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False


if __name__ == "__main__":
    game = CountryQuizGame()
    game.run()