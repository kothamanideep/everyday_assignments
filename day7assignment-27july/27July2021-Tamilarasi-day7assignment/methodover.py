class Car:
    def color(self):
        print("Red")

class BMW(Car):
    def color(self):
        print("Black")

objbmw=BMW()
objbmw.color()

obcar=Car()
obcar.color()