import constants
from pygame.locals import *  # Keys
import pymunk  # For constructing the plane body
from pymunk.vec2d import Vec2d  # Vector calculations - needed for the plane to fly like a goddamn plane does
import math  # Żeby Pan Merdas był wesoły <3
from enum import Enum
import bullet

class DIRECTION(Enum):
    LEFT = 1.
    RIGHT = -1

class Plane:

    def __init__(self, start_x, start_y, space, bullets):
        self.plane_body = pymunk.Body(constants.PLANE_MASS,
                                      constants.PLANE_INERTIA, body_type=pymunk.Body.DYNAMIC)
        self.plane_body.center_of_gravity = constants.PLANE_GRAVITY_CENTER
        self.plane_body.position = start_x, start_y
        self.plane_shape = pymunk.Poly(self.plane_body, constants.PLANE_VERTICES)
        self.plane_body.angle = 0  # works, no idea why
        self.speed = constants.PLANE_STARTING_SPEED
        self.space = space
        self.bullets = bullets

    def turn(self, direction):
        self.plane_body.angle += direction.value * constants.PLANE_ROTATION_SPEED * self.speed
    def shoot(self):
        bullet.spawn_bullet(self.space, self.plane_body.position, self.plane_body.angle, self.bullets)


class PlaneAI(Plane):
    def update(self):
        pass  # TODO


class PlaneHuman(Plane):
    def update(self, keys):  # Called every frame

        # Plane rotation
        if keys[K_LEFT]:
            self.turn(DIRECTION.LEFT)

        elif keys[K_RIGHT]:
            self.turn(DIRECTION.RIGHT)

        if keys[K_SPACE]:
            self.shoot()
        # Engine
        self.speed -= math.sin(self.plane_body.angle) * constants.PLANE_SPEED_CHANGE_RATE
        if self.speed < constants.PLANE_MIN_SPEED:
            self.speed = constants.PLANE_MIN_SPEED
        elif self.speed > constants.PLANE_MAX_SPEED:
            self.speed = constants.PLANE_MAX_SPEED
        self.plane_body.position += Vec2d(self.speed, 0).rotated(self.plane_body.angle)
        # self.plane_body.position += Vec2d(0,-0.2)