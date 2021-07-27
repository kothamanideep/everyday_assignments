class RBI:
    def intrest(self):
        print(10)

class SBI(RBI):
    def intrest(self):
        print(11)

class HDFC(RBI):
    def intrest(self):
        print(12)

objrbi=RBI()
objrbi.intrest()

objsbi=SBI()
objsbi.intrest()

objhdfc=HDFC()
objhdfc.intrest()