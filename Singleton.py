class Singleton:
    point = None
    def __new__(cls, *args, **kwargs):
        if cls.point == None:
            # new方法是一个静态方法，因此需要传入cls
            cls.point = super().__new__(cls)
        return cls.point




class tracer:
    def __init__(self,cls):
        self._cls = cls
        self._instances = None
    def __call__(self, *args, **kwargs):
        if not self._instances:
            self._instances = self._cls(*args,**kwargs)
        return self._instances




@tracer # f = tracer(f)
class f:
    def __init__(self,age):
        pass


f1 = f(1)
f2 = f(2)
print(id(f1))
print(id(f2))




def single(func):
    point = None
    def inner(*args,**kwargs):
        nonlocal point
        if point == None:
            point = func(*args,**kwargs)
        return point

    return inner
@single
class x:
    def __init__(self,age):
        pass


x1 = x(1)
x2 = x(2)
print(id(x1))
print(id(x2))



