class Segment():
    def getLights(self):
        pass
    

class RangeSegment(Segment):
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    def getLights(self):
        yield from range(self.start, self.stop)

class CrossSegment(Segment):
    def __init__(self, start, width, rows, skip):
        self.start = start
        self.width = width
        self.skip = skip
        self.rows = rows
    def getLights(self):
        numLights = self.width * self.rows
        for i in range(self.rows):
            yield from range(self.start+(self.width+self.skip)*i,(self.start+self.width)+(self.width+self.skip)*i)
            print()

def main():
    print("running main")
    rTest = RangeSegment(0,10)
    for i in rTest.getLights():
        print(i)

    print()
    cTest = CrossSegment(2,2,5,3)
    for i in cTest.getLights():
        print(i)


if __name__ == "__main__":
    main()
