
# 纯数字序列用数组比用列表实现更高效
# 因为是由数组封装而来的

from array import array

arr = array('b',(1,2,9,3,4,127))
print(arr)
arr = array(arr.typecode,sorted(arr))
print(arr)