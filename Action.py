class Action(): # lawsuit
    def __init__(self, func=None):
        self.func = func


class FadeAction(Action):
    def __init__(self, section,strip, b_start, b_stop):
        self.section = section
        self.b_start = b_start
        self.b_stop = b_stop
        self.strip = strip

    def func(self, time, keyframe):
        passed = time - keyframe.start
        total_len = keyframe.stop - keyframe.start
        out = self.b_start + (self.b_stop - self.b_start) * (passed) / (total_len)
        out = int(out)
        for index in self.section.getLights():
            self.strip[index] = (out, out, out)
        return True

class AllLightsOn(Action):
    def __init__(self, section, strip):
        self.section = section
        self.strip = strip
    def func(self, time, keyframe):
        for index in self.section.getLights():
            self.strip[index] = (255,255,255)
        return True



class AllLightsOff(Action):
    def __init__(self, section, strip):
        self.section = section
        self.strip = strip
    def func(self, time, keyframe):
        for index in self.section.getLights():
            self.strip[index] = (0,0,0)
        return True
