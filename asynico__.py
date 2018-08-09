import threading
import asyncio
import time

# 使用asyncio 实现单线程并发
@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    # time.sleep(1)

    yield from asyncio.sleep(1)# 模拟网络延迟， 这里不能使用time.sleep()


    print('Hello again! (%s)' % threading.currentThread())
# 创建一个 loop 对象
loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
# 将协程放在 loop中执行 即可实现单线程并发， 原理是循环执行 调用next()
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

#-------------------------------------------

# 简化写法
# async def hello():
#     print('Hello world! (%s)' % threading.currentThread())
#     # time.sleep(1)
#
#     await asyncio.sleep(1)# 模拟网络延迟， 这里不能使用time.sleep()
#
#
#     print('Hello again! (%s)' % threading.currentThread())
#
#
# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# # 将协程放在 loop中执行 即可实现单线程并发， 原理是循环执行 调用next()
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()
