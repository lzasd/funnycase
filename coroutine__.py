# 使用协程 动态的计算平均值

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
next(ave)
print(ave.send(10))
print(ave.send(20))