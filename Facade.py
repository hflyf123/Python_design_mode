# coding=utf-8
class SubSystemOne:
    '''
    子系统类1
    '''

    def method_one(self):
        print 'subsysone'


class SubSystemTwo:
    '''
    子系统类2
    '''

    def method_two(self):
        print 'subsystwo'


class SubSystemThree:
    '''
    子系统类3
    '''

    def method_three(self):
        print 'subsysthree'


class SubSystemFour:
    '''
    子系统类4
    '''

    def method_four(self):
        print 'subsysfour'


class Facade:
    '''
    外观类，知道哪些子系统类负责处理请求，
    将客户的请求代理给适当的子系统对象。
    '''

    def __init__(self):
        self.one = SubSystemOne()
        self.two = SubSystemTwo()
        self.three = SubSystemThree()
        self.four = SubSystemFour()

    def method_a(self):
        print 'method a'
        self.one.method_one()
        self.two.method_two()

    def method_b(self):
        print 'method b'
        self.three.method_three()
        self.four.method_four()


def main():
    facade = Facade()
    facade.method_a()
    print '******************************'
    facade.method_b()


if __name__ == '__main__':
    main()
