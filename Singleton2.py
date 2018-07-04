# coding=utf-8
#方法2:也是方法1的升级（高级）版本,
#使用装饰器(decorator),
#这是一种更pythonic,更elegant的方法,
#单例类本身根本不知道自己是单例的,因为他本身(自己的代码)并不是单例的

def singleton(cls, *args, **kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton


@singleton
class Myclass(object):
    a = 1
    def __init__(self, x=0):
        self.x = x


if __name__ == '__main__':
    one = Myclass()
    two = Myclass()

    two.a = 3
    print(one.a)
    print(id(one))
    print(id(two))
    one.x = 1
    print(one.x)
    print(two.x)