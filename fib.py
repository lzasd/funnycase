#使用yield
def fib1():
    a = 0
    b = 1
    while True:
        yield a
        a = a+b
        a,b = b,a
import functools
import time
# 递归 使用lru_cache缓存机制 优化递归
# lru_cache 将函数的值缓存，在此遇到相同的函数时 直接使用这个值，不执行函数
@functools.lru_cache()
def fib2(n):
    if n < 2:
        return 1 if n==2 else n
    return fib2(n-2)+ fib2(n-1)

t1 = time.time()
print(fib2(500))
t2 = time.time()

print(t2-t1)








