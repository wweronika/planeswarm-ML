import constants
from pygame.locals import *  # Keys
import pymunk  # For constructing the plane body
from pymunk.vec2d import Vec2d  # Vector calculations - needed for the plane to fly like a goddamn plane does
import math  # Żeby Pan Merdas był wesoły <3
from enum import Enum

class DIRECTION(Enum):
    LEFT = 1.
    RIGHT = -1

class Plane:

    def __init__(self, start_x, start_y):
        self.plane_body = pymunk.Body(constants.PLANE_MASS,
                                      constants.PLANE_INERTIA, body_type=pymunk.Body.DYNAMIC)
        self.plane_body.center_of_gravity = constants.PLANE_GRAVITY_CENTER
        self.plane_body.position = start_x, start_y
        self.plane_shape = pymunk.Poly(self.plane_body, constants.PLANE_VERTICES)
        self.plane_body.angle = 0  # works, no idea why
        self.speed = constants.PLANE_STARTING_SPEED

    def turn(self, direction):
        self.plane_body.angle += direction.value * constants.PLANE_ROTATION_SPEED * self.speed

class PlaneAI(Plane):
    def update(self):
        pass  # TODO


class PlaneHuman(Plane):
    def update(self, keys):  # Called every frame

        vel_len = self.plane_body.velocity.get_length()
        # Plane rotation
        if keys[K_LEFT]:
            self.turn(DIRECTION.LEFT)

        elif keys[K_RIGHT]:
            self.turn(DIRECTION.RIGHT)

        # Engine
        self.speed -= math.sin(self.plane_body.angle) * constants.PLANE_SPEED_CHANGE_RATE
        if self.speed < constants.PLANE_MIN_SPEED:
            self.speed = constants.PLANE_MIN_SPEED
        elif self.speed > constants.PLANE_MAX_SPEED:
            self.speed = constants.PLANE_MAX_SPEED
        self.plane_body.position += Vec2d(self.speed, 0).rotated(self.plane_body.angle)
