
    # # returns True for id > 0 else False
    # def __bool__(self):
    #     print('bool function called')
    #     if self.id>0:
    #         return self.id
    #     else:
    #         return 0


    # returns 0 for id <= 0, else id
# def __bool__(self):
#     print('len function called')
#     if self.id > 0:
#         return self.id
#     else:
#         return 0
# #print('len function called')

class custom():
    val = 0
    def __init__(self, num):
        self.val = num 
    def __bool__(self):
        return bool(self.val)
 
# custom objects
x = custom(0)
y = custom(52)
 
print(bool(x))
print(bool(y))