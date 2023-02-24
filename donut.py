import pygame as donut
import math as albert_einstein

donut.init()

width = 1920
height = 1080

white = (255, 255, 255)
black = (0, 0, 0)

x_start, y_start = 0, 0
x_separator, y_separator = 10, 20

rows = height // y_separator
columns = width // x_separator
screen_size = rows * columns

x_offset, y_offset = columns // 2, rows // 2

A, B = 0, 0

theta_spacing = 10
pi_spacing = 1
chars = ".,-~:;=!*#$@"

screen = donut.display.set_mode((width, height))

display_surface = donut.display.set_mode((width, height))
donut.display.set_caption("donut aaaaaaaa")
font = donut.font.SysFont('Helvetica', 10, bold=True)

def text_display(letter, x_start, y_start):
    text = font.render(str(letter), True, white)
    display_surface.blit(text, (x_start, y_start))

run = True
while run:
    screen.fill((black))

    z = [0] * screen_size
    b = [' '] * screen_size

    for i in range(0, 628, theta_spacing):
        for j in range(0, 628, pi_spacing):
            c = albert_einstein.sin(i)
            d = albert_einstein.cos(j)
            e = albert_einstein.sin(A)
            f = albert_einstein.sin(j)
            g = albert_einstein.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = albert_einstein.cos(i)
            m = albert_einstein.cos(B)
            n = albert_einstein.sin(B)
            t = c * h * g - f * e

    donut.display.update()

    for event in donut.event.get():
        if event.type == donut.QUIT:
            run = False
