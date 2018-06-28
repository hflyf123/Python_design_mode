# coding=utf-8
'''
程序实例：商场收银软件，需要根据不同的销售策略方式进行收费
'''


class CashSuper:
    '''
    策略类接口
    '''

    def accept_cash(self, money):
        return 0


class CashNormal(CashSuper):
    '''
    一般收费策略
    '''

    def accept_cash(self, money):
        return money


class CashRebate(CashSuper):
    '''
    打折收费策略
    '''
    discount = 0

    def __init__(self, ds):
        self.discount = ds

    def accept_cash(self, money):
        return money * self.discount


class CashReturn(CashSuper):
    '''
    满减收费策略
    '''
    total = 0
    ret = 0

    def __init__(self, t, r):
        self.total = t
        self.ret = r

    def accept_cash(self, money):
        if money >= self.total:
            re = money // self.total
            return money - self.ret * re
        else:
            return money


class CashContext:
    '''
    上下文类，配置策略类接口，维护一个对策略对象的引用
    '''

    def __init__(self, csuper):
        self.cs = csuper

    def get_result(self, money):
        return self.cs.accept_cash(money)


if __name__ == '__main__':
    money = input('money:')
    strategy = {}
    strategy[1] = CashContext(CashNormal())
    strategy[2] = CashContext(CashRebate(0.8))
    strategy[3] = CashContext(CashReturn(300, 100))
    ctype = input('type:1 for normal, 2 for 80% discount, 3 for 300 - 100:')
    if ctype in strategy:
        cc = strategy[ctype]
    else:
        print 'Undefine type,use normal mode'
        cc = strategy[1]
    print 'you will pay : %d' % (cc.get_result(money))
