# 使用协程 动态的计算平均值


# 使用预激装饰器进行优化
import functools
def coroutine(func):
    @functools.wraps(func)
    def wraper(*args,**kwargs):
        g = func(*args,**kwargs)
        next(g)
        return g
    return wraper

@coroutine
def averager():

    totle = 0.0
    count = 0
    avereger = None
    while True:
        add = yield avereger
        totle += add
        count += 1
        avereger = totle/count


ave = averager()

print(ave.send(10))
print(ave.send(20))