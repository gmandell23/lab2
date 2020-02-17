# Author: Georgia Mandell
# Date: 02/13/2020
# Purpose: to create a Body class, which represents an individual body, such as the Earth, the moon, the Sun,
# or any other planet


from cs1lib import *

class Body:

    def __init__(self, mass, x, y, vx, vy, pixel_radius, r, g, b):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.pixel_radius = pixel_radius
        self.r = r
        self.g = g
        self.b = b
        self.ax = 0
        self.ay = 0

    def draw(self, cx, cy, pixels_per_meter):
        set_fill_color(self.r, self.g, self.b)

        # The parameters cx and cy represent the location, in pixels, of the center of the simulation
        # The parameter pixels_per_meter gives the scale of the simulation, and it’s used to convert
        # the position of the body (stored in meters) into pixel coordinates in the window
        draw_circle(cx + pixels_per_meter * self.x, cy + pixels_per_meter * self.y, self.pixel_radius)

    def update_velocity(self, ax, ay, timestep):
        # the x and y velocities are updated by some accelerations that will be passed into the method,
        # as well as the timestep (also passed in)
        self.vx = self.vx + ax * timestep
        self.vy = self.vy + ay * timestep

    def update_position(self, timestep):
        # the x and y locations are updated by the appropriate velocities times the time step (passed in)
        self.x = self.x + self.vx * timestep
        self.y = self.y - self.vy * timestep


