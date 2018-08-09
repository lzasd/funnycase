# 使用__getattr__ 实现adapter 模式(适配器模式)
#适配器模式主要应用于希望复用一些现存的类，但是接口又与复用环境要求不一致的情况，
# 比如在需要对早期代码复用一些功能等应用上很有实际价值。


class adaptee(object):
    def foo(self):
        print ('foo in adaptee')
    def bar(self):
        print ('bar in adaptee')

class adapter(object):
    def __init__(self):
        self.adaptee = adaptee()

    # def foo(self):
    #     print ('foo in adapter')
    #     self.adaptee.foo()

    def __getattr__(self, name):
        return getattr(self.adaptee, name)

if __name__ == '__main__':
    a = adapter()
    # a.foo()
    # adapter（） 这个类没有bar（） 这个方法 所以会调用__getattr__() bar() 作为第二个参数
    a.bar()