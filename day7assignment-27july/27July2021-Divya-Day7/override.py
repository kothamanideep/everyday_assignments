class RBI:
    def ROI(self):
        print("The interest of RBI 8%")
class SBI(RBI):
    def ROI(self):
        print("The interest of SBI 7.9%")
class Canara(RBI):
    def ROI(self):
        print("The interest of Canara 7.5")
class HDFC(RBI):
    def ROI(self):
        print("The interest of HDFC 7%")
#roi = HDFC()
#roi.ROI()
hdfc = HDFC()
canara = Canara()
sbi = SBI()
rbi = RBI()
hdfc.ROI()
canara.ROI()

