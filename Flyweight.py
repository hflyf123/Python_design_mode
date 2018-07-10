# coding=utf-8

class WebSite:
    '''
    所有具体享元类的超类或接口,通过这个接口,
    Flyweight可以接受并作用与外部状态
    '''
    def use(self, *args):
        pass


class ConcreteWebSite(WebSite):
    '''
    继承Flyweight超类或实现Flyweight接口,
    并为内部状态增加存储空间
    '''
    def __init__(self, str_name):
        self.name = str_name

    def use(self, user):
        print('website type:%s,user:%s' % (self.name, user))


class UnShareWebSite(WebSite):
    '''
    指那些不需要共享的Flyweight子类,以为flyweight
    接口共享成为可能,但他并不强制共享
    '''
    def __init__(self, strName):
        self.name = strName

    def use(self, user):
        print('UnShare Website type:%s,user:%s' % (self.name, user))


class WebFactory:
    '''
    一个享元工厂,用来创建并管理Flyweight对象,它主要是用来确保合理地共享
    Flyweight,当用户请求一个Flyweight时,FlyweightFactory对象提供一个已
    创建的实例或者创建一个(如果不存在的话)
    '''
    def __init__(self):
        test = ConcreteWebSite('test')
        self.webtype = {'test':test}
        self.count = {'test':0}
    def get_web(self,webtype):
        if webtype not in self.webtype:
            temp = ConcreteWebSite(webtype)
            self.webtype[webtype] = temp
            self.count[webtype] = 1
        else:
            temp = self.webtype[webtype]
            self.count[webtype] += 1
        return temp
    def get_count(self):
        for key in self.webtype:
            print('type:%s,count:%d' % (key, self.count[key]))

if __name__ == '__main__':
    f = WebFactory()
    ws = f.get_web('blog')
    ws.use('Lee')
    ws2 = f.get_web('show')
    ws2.use('jack')
    ws3 = f.get_web('blog')
    ws3.use('chen')
    ws4 = UnShareWebSite('test')
    ws4.use('Mr.q')
    print(f.webtype)
    f.get_count()


