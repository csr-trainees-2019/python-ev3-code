import time
import math
from ev3dev.ev3 import *

def cut_abs(value, max):
    return max * math.copysign(1, value) if abs(value) > max else value

class PI:
    def __init__(self, setup, motor, wdup):
        self.motor = motor
        (self.kp, self.ki) = setup
        self.state = {'last': 0, 'now': 0, 'wanted': 0}
        (self.error_i, self.last_time, self.wdup) = (0, time.time(), 0)
        self.motor.reset()
        self.wdup = new

    def set_wanted_rad(self, wanted):
        self.state['wanted'] = wanted

    def proc(self):
        dt = (time.time() - self.last_time) / 1000
        self.last_time = time.time()
        error = self.state['wanted'] - self.state['now']
        error_d = (error - (self.state['wanted'] - self.state['last'])) / dt
        if self.wdup != 0:
            error_i = error_i if abs(error_i) < self.wdup else math.copysign(1, error_i) * self.wdup
        self.error_i += error * dt
        new_state = self.motor.position / 180 * math.pi
        (self.state['last'], self.state['now']) = (self.state['now'], new_state)
        derivative = (self.state['now'] - self.state['last']) / dt
        Ut = self.kp * error + self.ki * self.error_i
        value = cut_abs(Ut, 100)
        self.motor.run_direct(duty_cycle_sp = value)

    def get_state(self):
        return self.state['now']

    def unreset(self):
        self.last_time = time.time()

    def reset(self):
        (self.last_time, self.error_i) = (time.time(), 0)
        self.motor.stop(stop_action = 'brake')