# coding=utf-8

class Mediator:
    '''
    抽象中介者
    '''
    def send(self, message, col):
        pass


class Colleague:
    '''
    抽象通信对象
    '''
    def __init__(self, temp):
        self.mediator = temp


class Colleague1(Colleague):
    '''
    具体通信对象1
    '''
    def send(self, message):
        self.mediator.send(message, self)

    def notify(self, message):
        print('Colleague1 get a message: %s') % message


class Colleague2(Colleague):
    '''
    具体通信对象2
    '''
    def send(self, message):
        self.mediator.send(message, self)

    def notify(self, message):
        print('Colleague2 get a message: %s') % message


class ConcreteMediator(Mediator):
    '''
    具体中介者
    '''
    def send(self, message, col):
        if col == col1:
            col2.notify(message)
        else:
            col1.notify(message)


if __name__ == '__main__':
    m = ConcreteMediator()
    col1 = Colleague1(m)
    col2 = Colleague2(m)
    m.col1 = col1
    m.col2 = col2
    col1.send('How are you')
    col2.send('fine')
