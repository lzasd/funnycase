
# 内置堆结构就是一个完全二叉树， 父节点小于所有子节点
'''heap = []#建立一个常见的堆

heappush(heap,item)#往堆中插入一条新的值

item = heappop(heap)#弹出最小的值

item = heap[0]#查看堆中最小的值，不弹出

heapify(x)#以线性时间将一个列表转为堆 O(n)

item = heapreplace(heap,item)#弹出一个最小的值，然后将item插入到堆当中。堆的整体的结构不会发生改变。
heappoppush()#弹出最小的值，并且将新的值插入其中

merge()#将多个堆进行合并
nlargest(n , iterbale, key=None)从堆中找出做大的N个数，key的作用和sorted( )方法里面的key类似，用列表元素的某个属性和函数作为关键字'''

import heapq
import random
heap = []
for i in range(10):
    l = random.randint(0,999)
    print(l)


    heapq.heappush(heap,l)


print(heap)