class A:
    __name="mani"
    def test(self):
        print(__name)

obja=A()
#print(obja.__name)#error
print(obja._A__name)