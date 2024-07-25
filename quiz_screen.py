import pygame
import random, csv, os
from question import Question

class QuizScreen:
    def __init__(self, screen):
        self.screen = screen
        font_path = os.path.join(os.path.dirname(__file__), 'fonts', 'Oswald-VariableFont_wght.ttf')
        self.font = pygame.font.Font(font_path, 45)
        self.questions = self.load_questions()
        self.current_question = None
        self.timer = 8 * 1000  
        self.start_time = None
        self.option_font = pygame.font.Font(None, 40)
        self.option_button_width = 350
        self.option_button_height = 40
        self.option_button_rects = [
            pygame.Rect(90, 250 + idx * 80, self.option_button_width, self.option_button_height) for idx in range(4)
        ]
        self.answered = -1
        self.result_start_time = None
        self.score = [0, False]
        self.completed = False

    def load_questions(self):
        question_list = []
        with open("questions.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                text = row[0]
                options = row[1:5]
                ans_index = int(row[5])
                question_list.append(Question(text, options, ans_index))

        random.shuffle(question_list)
        return question_list[:10]
    
    def multi_line_text(self, text):
        max_width = self.screen.get_width() - 100
        words = text.split(" ")
        lines = []
        current_line = ""
        current_line_width = 0
        for word in words:
            word_render = self.font.render(word + " ", True, (255, 255, 255))
            if word_render.get_width() + current_line_width  < max_width:
                current_line += word + " "
                current_line_width += word_render.get_width()
            else:
                lines.append(current_line)
                current_line = word + " "
                current_line_width = word_render.get_width()
        
        lines.append(current_line)
        for idx, line in enumerate(lines):
            question_text = self.font.render(line, True, (255, 255, 255))
            self.screen.blit(question_text, (50, 50 + idx * question_text.get_height()))


    def display(self):
        gray = (70,70,70)
        orange = (229, 157, 36)
        white = (255, 255, 255)
        light_green = (0,140,0)
        red = (255,0,0)
        self.screen.fill(gray)
        
        if not self.current_question:
            if self.questions:
                self.current_question = self.questions.pop()
            else:
                self.completed = True
                return

        if self.start_time is None:
            self.start_time = pygame.time.get_ticks()

        question_text = self.font.render(self.current_question.text, True, (255, 255, 255))
        if question_text.get_width() > self.screen.get_width() - 150:
            self.multi_line_text(self.current_question.text)
        else:
            self.screen.blit(question_text, (50, 50))

        for idx, option in enumerate(self.current_question.options):
            if self.option_button_rects[idx].collidepoint(pygame.mouse.get_pos()):
                option_color = orange
            else:
                option_color = gray
            
            pygame.draw.rect(self.screen, option_color, self.option_button_rects[idx])
            
            option_text = self.option_font.render(option, True, white)
            current_option_button = self.option_button_rects[idx]
            self.screen.blit(option_text, (100, current_option_button.y + self.option_button_height // 2 - option_text.get_height() // 2))

        if self.answered != -1:
            if self.result_start_time is None:
                self.result_start_time = pygame.time.get_ticks()
                self.showing_result = True
            
            if self.showing_result:
                if pygame.time.get_ticks() - self.result_start_time < 1000: 
                    result_text = "Correct!" if self.current_question.correct_index == self.answered else "Incorrect!"
                    result_color = light_green if self.current_question.correct_index == self.answered else red
                    self.screen.fill(result_color)
                    result_text_surface = self.font.render(result_text, True, white)
                    self.screen.blit(result_text_surface, (self.screen.get_width() // 2 - result_text_surface.get_width() // 2, self.screen.get_height() // 2 - result_text_surface.get_height() // 2))
                    if result_text == "Correct!" and not self.score[1]:
                        self.score[0] += 1
                        self.score[1] = True
                else:
                    self.screen.fill(gray)
                    self.showing_result = False
                    self.answered = -1
                    self.current_question = None
                    self.start_time = pygame.time.get_ticks()
                    self.result_start_time = None
                    self.score[1] = False
            else:
                if self.completed:
                    self.showing_result = False
                    self.current_question = None
                    self.start_time = pygame.time.get_ticks()
        else:
            elapsed_time = pygame.time.get_ticks() - self.start_time
            if elapsed_time > self.timer:
                self.current_question = None
                self.start_time = pygame.time.get_ticks()
        
        if self.completed:
            self.screen.fill(gray)