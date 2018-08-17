import collections

# 具名元祖 可以为元祖设置名字和属性，并具有元祖的性质，
# 具名元祖的内部已经将
t1 = collections.namedtuple('basketer',['x','y','z'])

t = t1(1,2,3)
print(t)
print(t.x)