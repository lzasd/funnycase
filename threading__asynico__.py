# import threading
# import itertools
# import time
# import sys
# class Signal:
#     go = True
# def spin(msg, signal):
#     write, flush = sys.stdout.write, sys.stdout.flush
#                 # itertools.cycle 会创建一个无线的迭代器 循环迭代 指定的内容
#     for char in itertools.cycle('|/-\\'):
#            status = char + ' ' + msg
#            write(status)
#            flush()
#            write('\x08' * len(status))
#            time.sleep(.1)
#            if not signal.go:
#                     break
#     write(' ' * len(status) + '\x08' * len(status))
#
# def slow_function():
# # 假装等待I/O一段时间
#     time.sleep(3)
#     return 42
#
# def supervisor():
#     signal = Signal()
#     spinner = threading.Thread(target=spin,args=('thinking!', signal))
#     print('spinner object:', spinner)
#
#     spinner.start()
#
#     result = slow_function()
#     # 当cpu 指向主线程时  signal.go 更新为false 从而关闭子线程
#     signal.go = False
#     spinner.join()
#     return result
#
# def main():
#     result = supervisor()
#     print('Answer:', result)
# if __name__ == '__main__':
#
#     main()


#--------------------------------------------------------------------------------

import asyncio
import itertools
import sys
import time
@asyncio.coroutine
def spin(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        try:
            yield from asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
    write(' ' * len(status) + '\x08' * len(status))
@asyncio.coroutine
def slow_function():
# 假装等待I/O一段时间
    yield from asyncio.sleep(3)
    return 42
@asyncio.coroutine
def supervisor():
    spinner = asyncio.async(spin('thinking!'))
    print('spinner object:', spinner)
    result = yield from slow_function()
    spinner.cancel()
    return result
def main():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(supervisor())
    loop.close()
    print('Answer:', result)
if __name__ == '__main__':

    main()


