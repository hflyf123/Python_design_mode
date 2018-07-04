# coding=utf-8
'''
方法1,实现__new__方法
并在将一个类的实例绑定到类变量_instance上,
如果cls._instance为None说明该类还没有实例化过,实例化该类,并返回
如果cls._instance不为None,直接返回cls._instance
'''
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls)
        return cls._instance

class MyClass(Singleton):
    a = 1

if __name__ == '__main__':
    one = MyClass()
    two = MyClass()

    two.a = 3
    print(one.a)

    print(id(one))
    print(id(two))

    print(one == two)
    print(one is two)
