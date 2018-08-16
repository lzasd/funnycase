def gen():
    while True:

        yield 1
        return 999

def gf():
    print(1)

    yield from gen() # 后面跟一个生成器 可以直接使用next（） 调用则个生成器

print(gen())
# print(next(gen()))
print(next(gen()))

print(list(gen()))


print(gf())
print(next(gf()))
print(next(gf()))

