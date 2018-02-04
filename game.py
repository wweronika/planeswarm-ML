"""
Tutaj będzie mądry opis
"""
import sys

import pygame
from pygame.locals import *
import pymunk
import pymunk.pygame_util

import constants
import planes


def plane_collision_handler(arbiter, space, data):
    print("plane collision!")

    return False

def bullet_collision_handler(arbiter, space, data):
    print("bullet hit!")

    return False

### Global parameters



def main():
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

    # Collision handling
    collision_plane_to_plane_handler = space.add_collision_handler(  # Collision between plane and plane
        constants.PLANE_COLLISION_TYPE, constants.PLANE_COLLISION_TYPE
    )
    collision_plane_to_plane_handler.pre_solve = plane_collision_handler

    collision_bullet_to_plane_handler = space.add_collision_handler(  # Collision between plane and bullet
        constants.PLANE_COLLISION_TYPE, constants.BULLET_COLLISION_TYPE
    )
    collision_bullet_to_plane_handler.pre_solve = bullet_collision_handler

    bullets = []
    my_plane = planes.PlaneHuman(100,500, space, bullets)
    plane_body, plane_shape = my_plane.plane_body, my_plane.plane_shape
    space.add(plane_body, plane_shape)

    dummy_plane = planes.DummyPlane(400,500, space, bullets)
    dummy_body, dummy_shape = dummy_plane.plane_body, dummy_plane.plane_shape
    space.add(dummy_body, dummy_shape)

    while running:

        for event in pygame.event.get():  # event loop
            if event.type == QUIT:
                running = False
        keys = pygame.key.get_pressed()

        my_plane.update(keys)
        for bullet in bullets:
            bullet.update()
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
