
# 使用这个装饰器装饰的函数，写在with 语句里，遇到 yield 会暂停， 跳出with语句会自动执行后面的代码
# 可以用来自定义上下文管理器
import contextlib

@contextlib.contextmanager
def file():
    try:
        print('start')
        yield
    except Exception as e:
        raise e

    print('end')

if __name__ == '__main__':
    with file() as f:
        print('cont')

