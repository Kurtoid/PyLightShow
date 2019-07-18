class Keyframe():
    def __init__(self, start, stop, segment, action, update_type):
        self.start = start
        self.stop = stop
        self.segment = segment
        self.action = action
        self.update_type = update_type
    def doAction(self, time):
        result = self.action.func(time, keyframe=self)
        if self.update_type == "bounds":
            if(abs(time - self.start) < 0.2 or abs(time-self.stop) < 0.2):
                return True

        return result
        
