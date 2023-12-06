# Imports
import sys
import pygame
from pygame_button import *
from solve_sudoku import *
from pygame import mixer
import time
# Configuration
pygame.init()
pygame.display.set_caption('Sudoku Solver')
fps = 60
fpsClock = pygame.time.Clock()
width, height = 900, 530
screen = pygame.display.set_mode((width, height))

font = pygame.font.SysFont('Arial', 40)

objects = []
grid = []
last_grid_clicked = []


def set_grid_number(number):
    try:
        last_grid_clicked[len(last_grid_clicked) - 1].button_set_text(str(number))
    except:
        print("error")


def return_button_clicked(button_id):
    for button in objects:
        if button_id == button.button_id:
            try:
                last_grid_clicked[len(last_grid_clicked) - 1].fillColors = {
                    'normal': '#ffffff',
                    'hover': '#666666',
                    'pressed': '#333333',
                }
            except:
                print("error")

            button.fillColors = {
                'normal': '#ADD8E6',
                'hover': '#666666',
                'pressed': '#333333',
            }
            last_grid_clicked.append(button)


def reset_grid():
    for button in objects:
        if button.button_id:
            button.button_set_text(" ")

def update_grid_visual(solution):
    visual_grid = solution
    for v, s in zip(grid, visual_grid):
        for slot, solution in zip(v, s):
            for button in objects:
                if button.button_id == slot:
                    button.button_set_text(str(solution))


def create_value_grid():
    value_grid = []
    for column in grid:
        slots = []
        for slot in column:
            for button in objects:
                if button.button_id == slot:
                    text = button.get_button_text()
                    if text == ' ':
                        text = 0
                    slots.append(int(text))
        value_grid.append(slots)
    solution = run_solution(value_grid)
    update_grid_visual(solution)



def create_solve_button():
    solve_button = Button(screen, objects, 30, 385, 330, 50, 0, "Solve", create_value_grid,
                         None, False)
def reset_grid_button():
    reset_button = Button(screen, objects, 30, 450, 330, 50, 0, "Reset", reset_grid,
                         None, False)
def create_button_grid():
    x, y = 30, 30
    b_width, b_height = 100, 100
    margin = 15
    for i in range(9):
        if i % 3 == 0 and i != 0:
            y += b_height + margin
            x = 30
        grid_button = Button(screen, objects, x, y, b_width, b_height,0, str(i+1), set_grid_number, i+1,False)
        x += b_width + margin


def create_game_grid():
    x, y = 400, 30
    b_width, b_height = 50, 50
    margin = 2
    block_margin = 6
    for i in range(9):
        if i % 3 == 0 and i != 0:
            y += block_margin
        block = []
        for j in range(9):
            if j % 3 == 0 and j != 0:
                x += block_margin
            button_id = randint(0, 100000)
            grid_button = Button(screen, objects, x, y, b_width, b_height, button_id, " ", return_button_clicked,
                                 button_id, False)
            x += b_width + margin
            block.append(button_id)
        y += b_height + margin
        x = 400
        grid.append(block)


create_button_grid()
create_game_grid()
create_solve_button()
reset_grid_button()

# Game loop.
while True:
    screen.fill((20, 20, 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for object in objects:
        object.process()

    pygame.display.flip()
    fpsClock.tick(fps)