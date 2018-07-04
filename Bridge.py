# coding=utf-8
class Soft(object):
    '''
    被提炼的抽象
    '''

    def run(self):
        pass


class Game(Soft):
    '''
    抽象
    '''

    def run(self):
        print('Game')


class AddressList(Soft):
    '''
    抽象
    '''

    def run(self):
        print('Address list')


class Brand(object):
    '''
    实现
    '''

    def __init__(self):
        self.m_soft = None

    def set_soft(self, temp):
        self.m_soft = temp

    def run(self):
        pass


class BrandA(Brand):
    '''
    具体实现A
    '''

    def run(self):
        if not self.m_soft == None:
            print('BrandA')
            self.m_soft.run()


class BrandB(Brand):
    '''
    具体实现B
    '''

    def run(self):
        if not self.m_soft == None:
            print('BrandB')
            self.m_soft.run()


if __name__ == '__main__':
    brandA = BrandA()
    brandA.set_soft(Game())
    brandA.run()
    brandA.set_soft(AddressList())
    brandA.run()
