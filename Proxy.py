# coding=utf-8
class Subject:
    '''
    Subject类，定义了RealSubject和Proxy的共用接口
    这样在任何使用RealSubject的地方都能使用代理类
    '''

    def request(self):
        return 0


class RealSubject(Subject):
    '''
    RealSubject类，定义代理类所代表的真实实体
    '''

    def request(self):
        print 'Real request'


class Proxy(Subject):
    '''
    代理类，通过调用此类来访问subject的方法
    '''

    def request(self):
        self.real = RealSubject()
        self.real.request()


def main():
    p = Proxy()
    p.request()


if __name__ == '__main__':
    main()
