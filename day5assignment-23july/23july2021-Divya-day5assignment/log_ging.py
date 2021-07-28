import logging 

logging.basicConfig(filename='test.log',level=logging.DEBUG)
def addnum(a,b):
    return a+b

def subnum(a,b):
    return a-b

def mul(a,b):
    return a*b

def divi(a,b):
    return a/b

a = int(input("enter a number: "))
b = int(input("enter a number: "))

addnum_result = addnum(a , b)
#print('add: {} + {} = {}',format(a,b,addnum))
logging.debug(addnum(a,b))
subnum_result = subnum(a , b)
logging.debug(subnum(a,b))
#print('sub: {} + {} = {}',format(a  ,b ,subnum_result))
mul_result = mul(a , b)
logging.debug(mul(a,b))
#print('mul: {} + {} = {}',format(a  ,b ,mul_result))
divi_result = divi(a , b)
logging.debug(divi(a,b))
#print('div: {} + {} = {}',format(a  ,b ,divi_result))