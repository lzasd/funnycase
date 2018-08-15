# 用python 实现多种排序
# 冒泡排序， 队列表执行n -1 次遍历 , 每次遍历后执行要要排序数值-1 次比较,
# 稳定的排序
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

# alist=[1,2,3,99,4]
# bubbleSort(alist)
# print(alist)


# select_sort， 选择排序，遍历一次找出序列中最小的一个放在第一位，确定第一个位置，再遍历剩下的找出最小的放在第二个位子
# 不稳定
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
# 稳定
list1 = [1,2,3]
list1.sort()
def	insertionSort(alist):
    for	index	in	range(1,len(alist)):

        currentvalue=alist[index]
        position=index

        while	position>0	and	alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position	=	position-1
        alist[position]=currentvalue
# alist=[54,26,93,17,77,31,44,55,20]
# insertionSort(alist)
# print(alist)


# 希尔排序











# 快速排序:首先任意选取一个数据（通常选用数组的第一个数）作为关键数据，
# 然后将所有比它小的数都放到它前面，
# 所有比它大的数都放到它后面，这个过程称为一趟快速排序。
#O(nlgn) 不稳定
def QuickSort(myList,start,end):
    #判断low是否小于high,如果为false,直接返回
    if start < end:
        i,j = start,end
        #设置基准数
        base = myList[i]

        while i < j:
            #如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
            while (i < j) and (myList[j] >= base):
                j = j - 1

            #如找到,则把第j个元素赋值给第个元素i,此时表中i,j个元素相等
            myList[i] = myList[j]

            #同样的方式比较前半区
            while (i < j) and (myList[i] <= base):
                i = i + 1
            myList[j] = myList[i]
        #做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
        myList[i] = base

        #递归前后半区
        QuickSort(myList, start, i - 1)
        QuickSort(myList, j + 1, end)
    return myList


# myList = [49,38,65,97,76,13,27,49]
# QuickSort(myList,0,len(myList)-1)
# print(myList)

# 匿名函数实现快拍

#  选出第一个元素  把比他小的放在左边比他大的放在右边，
# 得到的结果后把比他小的那一边和比他大的那一边分别进行这个操作

quick_sort = lambda array: array if len(array) <= 1 else quick_sort(
    [item for item in array[1:] if item < array[0]]) + [array[0]] + quick_sort(
    [item for item in array[1:] if item >= array[0]])

print(quick_sort([1,223,2,312312,332,332,45]))





