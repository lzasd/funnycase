## 时间复杂度O（logn）


import bisect
alist = ['asd','swwa','dsa']
# 使用二分查找必须先排序
alist.sort()
# print(alist)
# bisect() 方法 返回被查找元素的位置，是第几个不是下标
b = bisect.bisect(alist,'swwa')
# print(b)
#  bisect_left() 返回索引
c = bisect.bisect_left(alist,'dsa')
# print(alist)
# print(c)
alist2 = [1,5,8,9]
# bisect.insort() 方法插入一个值不破坏原有顺序
bisect.insort(alist2,5)
print(alist2)