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

    def __init__(self, start_x, start_y, space, bullets, collision_type):
        self.plane_body = pymunk.Body(constants.PLANE_MASS,
                                      constants.PLANE_INERTIA, body_type=pymunk.Body.DYNAMIC)
        self.plane_body.center_of_gravity = constants.PLANE_GRAVITY_CENTER
        self.plane_body.position = start_x, start_y
        self.plane_shape = pymunk.Poly(self.plane_body, constants.PLANE_VERTICES)
        self.plane_shape.collision_type = collision_type
        self.plane_body.angle = 0  # works, no idea why
        self.speed = constants.PLANE_STARTING_SPEED
        self.space = space
        self.bullets = bullets
        self.ammo = constants.PLANE_STARTING_AMMO
        self.can_shoot = True

    def update(self):  # Called every frame
        # Engine
        self.speed -= math.sin(self.plane_body.angle) * constants.PLANE_SPEED_CHANGE_RATE
        if self.speed < constants.PLANE_MIN_SPEED:
            self.speed = constants.PLANE_MIN_SPEED
        elif self.speed > constants.PLANE_MAX_SPEED:
            self.speed = constants.PLANE_MAX_SPEED
        self.plane_body.position += Vec2d(self.speed, 0).rotated(self.plane_body.angle)
        # self.plane_body.position += Vec2d(0,-0.2)
        if self.ammo < 10:
            self.ammo += 0.1
        else:
            self.can_shoot = True
        # print(self.ammo)

    def turn(self, direction):
        self.plane_body.angle += direction.value * constants.PLANE_ROTATION_SPEED * self.speed

    def shoot(self):
        if self.ammo > 0 and self.can_shoot:
            bullet.spawn_bullet(self.space, self.plane_body.position, self.plane_body.angle, self.bullets)
            self.ammo -= 1
        else:
            self.can_shoot = False


class PlaneAI(Plane):
    def update(self):
        pass  # TODO


class DummyPlane(Plane):
    def update(self):
        pass  # just stand where u are, i'm gonna use you for collision detection


class PlaneHuman(Plane):
    pass