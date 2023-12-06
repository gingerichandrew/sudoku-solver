import pygame
from random import *

class Button():
    def __init__(self,
                 screen,
                 objects,
                 x,
                 y,
                 width,
                 height,
                 button_id=None,
                 button_text='Button',
                 onclick_function=None,
                 function_param=None,
                 one_press=False):
        self.x = x
        self.y = y
        self.text = button_text
        self.button_id = button_id
        self.width = width
        self.button_text = button_text
        self.height = height
        self.onclickFunction = onclick_function
        self.function_param = function_param
        self.onePress = one_press
        self.font = pygame.font.SysFont('Arial', 40)
        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }
        self.screen = screen
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.button_surf = self.font.render(button_text, True, (20, 20, 20))

        self.alreadyPressed = False

        objects.append(self)

    def get_button_text(self):

        return self.button_text

    def button_set_text(self, text):
        self.button_text = text
        self.button_surf = self.font.render(text, True, (20, 20, 20))

    def process(self):

        mousePos = pygame.mouse.get_pos()

        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])

                if self.onePress:
                    if self.function_param:
                        self.onclickFunction(self.function_param)
                    else:
                        self.onclickFunction()

                elif not self.alreadyPressed:
                    if self.function_param:
                        self.onclickFunction(self.function_param)
                    else:
                        self.onclickFunction()
                        self.alreadyPressed = True

            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.button_surf, [
            self.buttonRect.width / 2 - self.button_surf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.button_surf.get_rect().height / 2
        ])
        self.screen.blit(self.buttonSurface, self.buttonRect)


# def create_game_grid():
#     x, y = 400, 30
#     current_left = x
#     current_y = y
#     b_width, b_height = 50, 50
#     margin = 2
#     for i in range(9):
#         if i % 3 == 0 and i != 0:
#             current_y += ((b_height + margin) * 3) + margin * 2
#             x = 400
#         y = current_y
#         current_left = x
#         block = []
#         for i in range(9):
#             if i % 3 == 0 and i != 0:
#                 y += b_height + margin
#                 x = current_left
#             button_id = randint(0, 100000)
#             block.append(button_id)
#             grid_button = Button(screen, objects, x, y, b_width, b_height, button_id, " ", return_button_clicked,
#                                  button_id, False)
#             x += b_width + margin
#             grid.append(block)
#         x += margin * 2