from pid import *

class Mani:
    def __init__(self, knots):
        self.pidlist = []
        for pid in range(knots):
            self.pidlist.append(PID((0, 0, 0),LargeMotor('outA')))

    def set_gear_ratios(self, ratiolist):
        self.gear_ratio_list = ratiolist

    def set_motors(self, motorlist):
        if len(motorlist) != len(self.pidlist):
            return 'error';
        for i in range(1, len(self.pidlist)):
            self.pidlist[i].set_motor(motorlist[i])
        return 'ok'

    def set_setup(delf, setuplist):
        if len(setuplist) != len(self.pidlist):
            return 'error';
        for i in range(1, len(self.pidlist)):
            self.pidlist[i].set_setup(setuplist[i])
        return 'ok'

    def set_state(self, wantedlist):
        if len(wantedlist) != len(self.pidlist):
            return 'error';
        for i in range(1, len(self.pidlist)):
            self.pidlist[i].set_wanted_rad(wantedlist[i] * self.gear_ratio_list[i])
        return 'ok'

    def get_state(self):
        to_ret = []
        for i in range(1, len(self.pidlist)):
            to_ret.append(self.pidlist[i].get_state() / self.gear_ratio_list[i])
        return to_ret

    def set_wdups(self, wduplist):
        if len(wduplist) != len(self.pidlist):
            return 'error';
        for i in range(1, len(self.pidlist)):
            self.pidlist[i].set_wdup(wduplist[i])
        return 'ok'

    def reset(self):
        for i in self.pidlist:
            i.reset()

    def unreset(self):
        for i in self.pidlist:
            i.last_time = time.time()

    def proc(self):
        for i in self.pidlist:
            i.proc()
