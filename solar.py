# Author: Georgia Mandell
# Date: 02/16/2020
# Purpose: simulates the motion of the Sun and first four planets of the solar system

from cs1lib import *
from system import System
from body import Body

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

TIME_SCALE = 2000000        # real seconds per simulation second
PIXELS_PER_METER = 8 / 1e10  # distance scale for the simulation

FRAMERATE = 30              # frames per second
TIMESTEP = 1.0 / FRAMERATE  # time between drawing each frame

AU = 1.49598e11
EM = 5.9736e24

def main():

    set_clear_color(0, 0, 0)    # black background

    clear()

    # Draw the system in its current state.
    solar.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

    # Update the system for its next state.
    solar.update(TIMESTEP * TIME_SCALE)

sun = Body(1.98892e30, 0, 0, 0, 0, 15, 1, 1, 0)
mercury = Body(.06 * EM, -.3871 * AU, 0, 0, 47890, 3, 1, .4, 0)
venus = Body(.82 * EM, -.7233 * AU, 0, 0, 35040, 6, 0, .6, .2)
earth = Body(1.0 * EM, -1.0 * AU, 0, 0, 29790, 7, 0, .4, 1)
mars = Body(.11 * EM, -1.524 * AU, 0, 0, 24140, 4, .8, .2, 0)
solar = System([sun, mercury, venus, earth, mars])

start_graphics(main, 2400, framerate=FRAMERATE)