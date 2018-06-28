# coding=utf-8
# 程序实例：展示一个人一件一件穿衣服的过程。
class Person:
    '''
    被装饰对象
    '''

    def __init__(self, tname):
        self.name = tname

    def show(self):
        print 'dressed %s' % (self.name)


class Finery(Person):
    '''
    装饰物
    '''
    component = None

    def __init__(self):
        pass

    def decorate(self, ct):
        self.component = ct

    def show(self):
        self.component.show()


class TShirts(Finery):
    '''
    装饰物具体实现（T恤）
    '''

    def __init__(self):
        pass

    def show(self):
        print 'Big TShirt'
        self.component.show()


class BigTrouser(Finery):
    '''
    装饰物具体实现（牛仔裤）
    '''

    def __init__(self):
        pass

    def show(self):
        print 'Big Trouser'
        self.component.show()


if __name__ == '__main__':
    p = Person('lyf')
    bt = BigTrouser()
    ts = TShirts()
    ts.decorate(p)
    bt.decorate(ts)
    bt.show()
