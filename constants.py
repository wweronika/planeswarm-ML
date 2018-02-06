import pymunk

## Game engine related
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 800

## Game physics related
GRAVITY_FORCE = -0

## Plane object related
PLANE_VERTICES = [(0, 0), (15, 0), (30,5), (15,10), (0,10)]
PLANE_GRAVITY_CENTER = (15,5)
PLANE_ROTATION_SPEED = 0.01
PLANE_MASS = 1
PLANE_STARTING_SPEED = 3
PLANE_MAX_SPEED = 10
PLANE_MIN_SPEED = 1
PLANE_SPEED_CHANGE_RATE = 0.02
PLANE_A_COLLISION_TYPE = 1
PLANE_B_COLLISION_TYPE = 2
PLANE_STARTING_AMMO = 5.
## Bullet object related
BULLET_SPEED = 7
BULLET_MASS = 0.1
BULLET_INERTIA = pymunk.inf
BULLET_COLLISION_TYPE = 3

PLANE_INERTIA = pymunk.inf