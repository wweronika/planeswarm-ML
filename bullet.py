import constants
import pymunk
from pymunk.vec2d import Vec2d


class Bullet:
    def __init__(self, space, position, angle, bullets):
        self.bullet_body = pymunk.Body(constants.BULLET_MASS, constants.BULLET_INERTIA, body_type=pymunk.Body.DYNAMIC)
        self.bullet_body.position = position + Vec2d(40,5).rotated(angle)
        self.bullet_shape = pymunk.Circle(self.bullet_body, 5)
        self.bullet_shape.collision_type = constants.BULLET_COLLISION_TYPE
        self.movement_vector = Vec2d(constants.BULLET_SPEED, 0).rotated(angle)
        self.space = space
        self.bullets = bullets

    def update(self):
        self.bullet_body.position += self.movement_vector
        if abs(self.bullet_body.position.x) > 2000 or abs(self.bullet_body.position.y) > 1000:
            self.space.remove(self.bullet_body, self.bullet_shape)
            self.bullets.remove(self)


def spawn_bullet(space, position, angle, bullets):
    bullet = Bullet(space, position, angle, bullets)
    space.add(bullet.bullet_body, bullet.bullet_shape)
    bullets.append(bullet)
