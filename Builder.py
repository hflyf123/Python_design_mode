# coding=utf-8
class Person:
    '''
    Builder类，创建一个product对象的各个部件指定的抽象接口
    '''

    def creat_head(self):
        pass

    def creat_hand(self):
        pass

    def creat_body(self):
        pass

    def creat_leg(self):
        pass


class ThinPerson(Person):
    '''
    具体建造者，实现builder接口，
    构造和装配各个部件
    '''

    def creat_head(self):
        print 'Thin head'

    def creat_hand(self):
        print 'Thin hand'

    def creat_body(self):
        print 'Thin body'

    def creat_leg(self):
        print 'Thin leg'


class ThickPerson(Person):
    '''
    具体建造者，实现builder接口，
    构造和装配各个部件
    '''

    def creat_head(self):
        print 'Thick head'

    def creat_hand(self):
        print 'Thick hand'

    def creat_body(self):
        print 'Thick body'

    def creat_leg(self):
        print 'Thick leg'


class Director:
    '''
    指挥者，是构建一个使用Builder
    接口的对象
    '''

    def __init__(self, temp):
        self.p = temp

    def create(self):
        self.p.creat_head()
        self.p.creat_body()
        self.p.creat_hand()
        self.p.creat_leg()


if __name__ == '__main__':
    p = ThickPerson()
    d = Director(p)
    d.create()
