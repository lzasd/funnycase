# iter()函数的另一种用法， 第一个参数接收一个函数的引用，第二个参数接收标记值， 但函数返回这个值时，结束程序
import random

def f():
    return random.randint(1,6)


fs = iter(f,3)
print(fs)
for i in fs:
    print(i)
