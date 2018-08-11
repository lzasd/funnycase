# 用python 实现多种排序
# 冒泡排序， 队列表执行n -1 次遍历 , 每次遍历后执行要要排序数值-1 次比较
def	bubbleSort(alist):

    for	passnum	in	range(len(alist)-1,0,-1):
        point = True
        for	i	in	range(passnum):
            if	alist[i]>alist[i+1]:
                temp=alist[i]
                alist[i]=alist[i+1]
                alist[i+1]=temp
                point = False
        if point:
            return

alist=[1,2,3,99,4]
bubbleSort(alist)
print(alist)


# select_sort， 选择排序，遍历一次找出序列中最小的一个放在第一位，确定第一个位置，再遍历剩下的找出最小的放在第二个位子
def selectSort(s):
    for i in range(0, len(s) - 1):
        index = i
        for j in range(i + 1, len(s)):
            if s[index] > s[j]:
                index = j
        s[i], s[index] = s[index], s[i]

# print sort result.

# s = [3, 4, 1, 6, 2, 9, 7, 0, 8, 5]
# selectSort(s)
# print(s)


# 插入排序，第一个元素一定是排列好的， 然后拿到第二个，插入到排列好的序列， 所以插入之后得到的序列也是排列好的，
# 然后拿到第三个元素插入到前面的序列。。。
def	insertionSort(alist):
    for	index	in	range(1,len(alist)):

        currentvalue=alist[index]
        position=index

        while	position>0	and	alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position	=	position-1
        alist[position]=currentvalue
alist=[54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)


# 合并排序
# def	mergeSort(alist):
#     print("Splitting	",alist)
#     if	len(alist)>1:
#         mid	=	len(alist)//2
#         lefthalf	=	alist[:mid]
#         righthalf	=	alist[mid:]
#         mergeSort(lefthalf)
#         mergeSort(righthalf)
#
#         i=0
#         j=0
#         k=0
#         while	i	<	len(lefthalf)	and	j	<	len(righthalf):
#             if	lefthalf[i]	<	righthalf[j]:
#                 alist[k]=lefthalf[i]
#                 i=i+1
#             else:
#                 alist[k]=righthalf[j]
#                 j=j+1
#                 k=k+1
#
#             while	i	<	len(lefthalf):
#                 alist[k]=lefthalf[i]
#                 i=i+1
#                 k=k+1
#
#             while j	<	len(righthalf):
#                 alist[k]=righthalf[j]
#                 j=j+1
#                 k=k+1
#                 print("Merging	",alist)
# alist=[54,26,93,17,77,31,44,55,20]
# mergeSort(alist)
# print(alist)




