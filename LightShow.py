from Segment import RangeSegment
from Action import Action, FadeAction, AllLightsOff, AllLightsOn
from Keyframe import Keyframe
# import pyaudio
# import wave
import time

import board
import neopixel

class LightShow():
    # segments = {}
    keyframes = []
    total_time = 5
    delay_time = .05

pixels = neopixel.NeoPixel(board.D18, 10, auto_write=False)


def main():
    # message another machine a target time (2 seconds later?) to start playing sound
    # wait 2 seconds
    show = LightShow()
    first10 = RangeSegment(0,10)

    #act = Action(allLightsOn)
    act = FadeAction(first10, pixels, 0, 255)
    firstKeyframe = Keyframe(0, 1, first10, act, "every")
    show.keyframes.append(firstKeyframe)

    act = FadeAction(first10, pixels, 255, 0)
    firstKeyframe = Keyframe(1, 2, first10, act, "every")
    show.keyframes.append(firstKeyframe)
    #act2 = AllLightsOff(first10, pixels)
    #secondKeyframe = Keyframe(2, 4, first10, act2, "bounds")
    #show.keyframes.append(secondKeyframe)

    #print(show.keyframes)
    start = time.perf_counter()
    while time.perf_counter() - start < show.total_time:
        # do something
        loop_begin = time.perf_counter()
        elapsed = loop_begin - start
        #print("current time:",elapsed)
        needShow = False
        for keyframe in show.keyframes:
            if keyframe.start < elapsed and keyframe.stop > elapsed:
                needShow =  needShow | keyframe.doAction(elapsed)
        #print(needShow)
        if needShow:
            pixels.show()
        #print("time taken:",time.perf_counter()-loop_begin)
        time_taken = time.perf_counter() - loop_begin
        time.sleep(show.delay_time-max(0,time_taken))

if __name__ == "__main__":
    main()
