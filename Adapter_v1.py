# coding=utf-8

class Target:
    '''
    客户所期待的接口，目标可以是
    具体或抽象的类，也可以是接口
    '''

    def request(self):
        adapter = Adapter()
        adapter.request()



class Adaptee(Target):
    '''
    需要适配的类
    '''

    def sepcific_request(self):
        print('specific request')


class Adapter(Target):
    '''
    通过在内部包装一个Aadptee对象，把源接口
    抓换成目标接口
    '''

    def __init__(self):
        self.adaptee = Adaptee()

    def request(self):
        self.adaptee.sepcific_request()


if __name__ == '__main__':
    target = Target()
    target.request()
