# coding=utf-8
class Observer:
    '''
    抽象观察者类,为所有的具体观察者定义一个接口,
    在得到主题时的通知时更新自己
    '''

    def __init__(self, strname, strsub):
        self.name = strname
        self.sub = strsub

    def update(self):
        pass


class StackObserver(Observer):
    '''
    具体观察者类,实现抽象观察者角色所要求的更新接口,
    以便使本身的状态与主题的状态相协调
    '''

    # no need to rewrite __init__()
    def update(self):
        print '%s:%s, stop watching stock and go on work' % (self.name, self.sub.action)


class NBAObserver(Observer):
    '''
    具体观察者类，实现抽象观察者角色所要求的更新接口，
    以便使本身的状态与主题的状态相协调
    '''

    def update(self):
        print '%s:%s, stop watching NBA and go on work' % (self.name, self.sub.action)


class SecretaryBase:
    '''
    抽象的主题类，把所有观察者对象的引用保存在一个聚集里，每个主题
    都可以有任何数量的观察者，抽象主题提供一个接口，可以增加或删除观察者对象
    '''

    def __init__(self):
        self.observers = []

    def add_observer(self, new_observer):
        pass

    def remove_observer(self, observer):
        pass

    def notify(self):
        pass


class Secretary(SecretaryBase):
    '''
    具体主题，将有关状态存入具体观察者对象，
    在具体主题的内部状态改变时，
    给所有登记过的观察者发出通知
    '''

    def add_observer(self, new_observer):
        self.observers.append(new_observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for o in self.observers:
            o.update()


if __name__ == '__main__':
    p = Secretary()
    s1 = StackObserver('XiaoMing', p)
    s2 = NBAObserver('LiGang', p)
    p.add_observer(s1)
    p.add_observer(s2)
    p.action = 'WARING:BOSS'
    p.notify()
