# Author: Georgia Mandell
# Date: 02/13/2020
# Purpose: to create the System class, which represents the collection of bodies that we want to simulate
from cs1lib import *
import math


class System:

    def __init__(self, body_list):
        self.body_list = body_list

    def draw(self, cx, cy, pixels_per_meter):

        # calls the draw method on each body in the body list
        for body in self.body_list:
            body.draw(cx, cy, pixels_per_meter)

    def compute_acceleration(self, n):
        new_body = self.body_list[n]
        ax = 0
        ay = 0
        # loops through each body to compute the ax and ay contributions of each of them to acceleration of the body at index n
        for i in range(len(self.body_list)):
            if i != n:
                g = 6.67384 / 1e11
                dx = (self.body_list[i].x - new_body.x)
                dy = (self.body_list[i].y - new_body.y)
                r = math.sqrt(dx*dx + dy*dy)
                acc = (g * self.body_list[i].mass) / (r * r)
                ax = ax + acc * (dx / r)
                ay = ay - acc * (dy / r)

        # returns ax and ay
        return (ax, ay)

    def update(self, timestep):
        # computes the acceleration adn updates the position and velocity of each body in the body list
        for n in range(len(self.body_list)):
            (ax, ay) = self.compute_acceleration(n)
            self.body_list[n].update_velocity(ax, ay, timestep)
            self.body_list[n].update_position(timestep)

