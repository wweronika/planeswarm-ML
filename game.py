"""
Tutaj będzie mądry opis
"""
import sys
from enum import Enum

import pygame
from pygame.locals import *
import pymunk
import pymunk.pygame_util

import constants
import planes


class GameState(Enum):
    running = 0
    a_won = 1
    b_won = 2
    collision = 3
    a_crashed = 4
    b_crashed = 5
    quit = 6


class Game():
    def __init__(self):
        """
        Constructor only loads the pygame module,
        then sets the rest of class attributes to None.
        Other tasks such as creating the game window
        are moved to create_basic_game_components method,
        since they will be reused when launching the game
        in different modes (train/vs/whatever else may come)
        """
        # Game engine related
        pygame.init()
        self.screen = None
        self.clock = None
        self.space = None
        self.draw_options = None
        self.font = None  # But do we really need a font..?

        # Simulation related
        self.bullets = None
        self.game_state = None

    def create_basic_game_components(self):
        """
        This method makes a basic pygame window
        and connects it with the pymunnk physic engine
        """
        self.screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.space = pymunk.Space()
        self.space.gravity = 0, constants.GRAVITY_FORCE
        self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)  # connecting the physics lib to graphic engine
        self.font = pygame.font.SysFont("Arial", 16)

    def plane_a_hit_b(self, arbiter, space, data):
        print("a hit b!")
        self.game_state = GameState.a_won
        return False

    def planes_collision(self, arbiter, space, data):
        print("planes collision!")
        self.game_state = GameState.collision
        return False

    def plane_b_hit_a(self, arbiter, space, data):
        print("b hit a!")
        self.game_state = GameState.b_won
        return False

    def initialise_collisions(self):

        plane_a_hit_b_collision = self.space.add_collision_handler(  # Plane a scores
            constants.PLANE_B_COLLISION_TYPE, constants.BULLET_COLLISION_TYPE
        )
        plane_a_hit_b_collision.pre_solve = self.plane_a_hit_b

        plane_b_hit_a_collision = self.space.add_collision_handler(  # Plane b scores
            constants.PLANE_A_COLLISION_TYPE, constants.BULLET_COLLISION_TYPE
        )
        plane_b_hit_a_collision.pre_solve = self.plane_b_hit_a

        planes_collision = self.space.add_collision_handler(  # Smoleńsk
            constants.PLANE_A_COLLISION_TYPE, constants.PLANE_B_COLLISION_TYPE
        )
        planes_collision.pre_solve = self.planes_collision

    def test_vs_dummy(self):
        """
        Fly freely, one dummy plane is spawned to test collisions
        Method used just for testing
        """
        self.create_basic_game_components()
        self.initialise_collisions()  # Collision handling

        # Object spawning
        bullets = []

        my_plane = planes.PlaneHuman(100, 500, self.space, bullets, constants.PLANE_B_COLLISION_TYPE)
        self.space.add(my_plane.plane_body, my_plane.plane_shape)

        dummy_plane = planes.DummyPlane(400, 500, self.space, bullets, constants.PLANE_A_COLLISION_TYPE)
        self.space.add(dummy_plane.plane_body, dummy_plane.plane_shape)

        self.game_state = GameState.running

        while self.game_state == GameState.running:

            for event in pygame.event.get():  # event loop
                if event.type == QUIT:
                    self.game_state = GameState.quit
            keys = pygame.key.get_pressed()

            # Plane rotation
            if keys[K_LEFT]:
                my_plane.turn(planes.DIRECTION.LEFT)

            elif keys[K_RIGHT]:
                my_plane.turn(planes.DIRECTION.RIGHT)

            if keys[K_SPACE]:
                my_plane.shoot()

            my_plane.update()
            for bullet in bullets:
                bullet.update()
            ### Clear screen
            self.screen.fill(pygame.color.THECOLORS["black"])

            ### Draw stuff
            self.space.debug_draw(self.draw_options)
            # draw(screen, space)

            pygame.display.flip()

            ### Update physics
            fps = 60
            dt = 1. / fps
            self.space.step(dt)

            self.clock.tick(fps)
            pygame.display.set_caption("fps: " + str(self.clock.get_fps()))

    def train_visible(self):
        """
        Trains the network and lets the user see
        the progress made by the network.
        Simulation runs in real-time
        """
        self.create_basic_game_components()
        self.initialise_collisions()  # Collision handling

        # Object spawning
        bullets = []

        B_plane = planes.PlaneHuman(100, 500, self.space, bullets, constants.PLANE_B_COLLISION_TYPE)
        self.space.add(B_plane.plane_body, B_plane.plane_shape)

        A_plane = planes.DummyPlane(400, 500, self.space, bullets, constants.PLANE_A_COLLISION_TYPE)
        self.space.add(A_plane.plane_body, A_plane.plane_shape)

        self.game_state = GameState.running

        while self.game_state == GameState.running:

            for event in pygame.event.get():  # event loop
                if event.type == QUIT:
                    self.game_state = GameState.quit
            keys = pygame.key.get_pressed()

            # Plane rotation
            if keys[K_LEFT]:
                B_plane.turn(planes.DIRECTION.LEFT)

            elif keys[K_RIGHT]:
                B_plane.turn(planes.DIRECTION.RIGHT)

            if keys[K_SPACE]:
                B_plane.shoot()

            B_plane.update()
            A_plane.shoot()
            for bullet in bullets:
                bullet.update()
            ### Clear screen
            self.screen.fill(pygame.color.THECOLORS["black"])

            ### Draw stuff
            self.space.debug_draw(self.draw_options)
            # draw(screen, space)

            pygame.display.flip()

            ### Update physics
            fps = 60
            dt = 1. / fps
            self.space.step(dt)

            self.clock.tick(fps)
            pygame.display.set_caption("fps: " + str(self.clock.get_fps()))


def main():
    myGame = Game()
    myGame.train_visible()


if __name__ == '__main__':
    sys.exit(main())
