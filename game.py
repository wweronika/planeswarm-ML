"""
Tutaj będzie mądry opis
"""
import sys

import pygame
from pygame.locals import *
from pygame.color import *
import pymunk

import pymunk.pygame_util

import constants
import planes

def main():
    global PLANE_MOVING_SPEED
    ### PyGame init

    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True  # to jest całkiem ważne xD
    font = pygame.font.SysFont("Arial", 16)

    ### Physics stuff
    space = pymunk.Space()
    space.gravity = 0, constants.GRAVITY_FORCE
    draw_options = pymunk.pygame_util.DrawOptions(screen) # connecting the physics engine to graphic engine

    ### End of game engine skeleton
    # Here the game starts

    my_plane = planes.PlaneHuman(100,500)
    plane_body, plane_shape = my_plane.plane_body, my_plane.plane_shape
    space.add(plane_body, plane_shape)
    while running:

        for event in pygame.event.get():  # pętla eventowa
            if event.type == QUIT:
                running = False
        keys = pygame.key.get_pressed()

        my_plane.update(keys)


        ### Clear screen
        screen.fill(pygame.color.THECOLORS["black"])

        ### Draw stuff
        space.debug_draw(draw_options)
        # draw(screen, space)

        pygame.display.flip()

        ### Update physics
        fps = 60
        dt = 1. / fps
        space.step(dt)

        clock.tick(fps)
        pygame.display.set_caption("fps: " + str(clock.get_fps()))


if __name__ == '__main__':
    sys.exit(main())
