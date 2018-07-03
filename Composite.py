# coding=utf-8
class Componet:
    '''
    组合中的对象声明接口,
    在适当情况下,声明一个
    接口用于访问和管理Componet
    的子部件
    '''

    def __init__(self, str_name):
        self.m_str_name = str_name

    def add(self, com):
        pass

    def display(self, ndepth):
        pass

    def remove(self, index):
        pass


class Leaf(Componet):
    def add(self, com):
        print('leaf can\'t add')

    def display(self, ndepth):
        str_temp = ''
        for i in range(ndepth):
            str_temp = str_temp + '-'
        str_temp = str_temp + self.m_str_name
        print(str_temp)

    def remove(self, index):
        print('leaf can\'t remove')


class Composite(Componet):
    '''
    定义有枝节点行为,
    用来存储子部件,在component接口中实现
    与子部件有关的操作,比如add和remove
    '''

    def __init__(self, str_name):
        Componet.__init__(self, str_name)
        self.m_str_name = str_name
        self.c = []

    def add(self, com):
        self.c.append(com)

    def remove(self, index):
        self.c.remove(index)

    def display(self, ndepth):
        str_temp = ''
        for i in range(ndepth):
            str_temp = str_temp + '-'
        str_temp = str_temp + self.m_str_name
        print(str_temp)
        for com in self.c:
            com.display(ndepth + 2)


if __name__ == '__main__':
    p = Composite('wong')
    p.add(Leaf('lee'))
    p.add(Leaf('zhao'))
    pl = Composite('wu')
    pl.add(Leaf('san'))
    p.add(pl)
    p.display(1)
