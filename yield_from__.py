def gen():
    while True:

        yield 1
        return 999

def gf():

    yield from gen()

print(gen())
print(next(gen()))
print(next(gen()))

print(list(gen()))


print(list(gf()))

