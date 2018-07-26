#使用yield
def fib1():
    a = 0
    b = 1
    while True:
        yield a
        a = a+b
        a,b = b,a

# 递归
def fib2(n):
    if n < 2:
        return 1 if n==2 else n
    return fib2(n-2)+ fib2(n-1)

fib_list = list(map(fib2,range(10)))
print(fib_list)








