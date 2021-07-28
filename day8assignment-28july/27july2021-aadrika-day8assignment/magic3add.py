class distance:
    def __init__(self, x=None,y=None):
        self.feet=x
        self.inch=y
    def __add__(self,x):
        temp=distance()
        temp.feet=self.feet+x.feet
        temp.inch=self.inch+x.inch
        if temp.inch>=12:
            temp.feet+=1
            temp.inch-=12
            return temp
    def __str__(self):
        return 'feet:'+str(self.feet)+' inches: '+str(self.inch)

d1=distance(3,10)
print(d1)