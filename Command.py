# coding=utf-8

class Barbucer:
    '''
    receiver类,知道如何实施与执行一个请求相关
    的操作,任何类都可能作为一个接受者
    '''

    def make_mutton(self):
        print 'Mutton'

    def make_chicken_wing(self):
        print 'Chicken wing'


class Command:
    '''
    command类接口，
    用来声明执行操作的接口
    '''

    def __init__(self, temp):
        self.receiver = temp

    def execute_cmd(self):
        pass


class BakeMuttonCmd(Command):
    '''
    将一个接收者对象绑定于一个动作,调用接收者
    相应的操作,实现execute
    '''

    def execute_cmd(self):
        self.receiver.make_mutton()


class ChickenWingCmd(Command):
    '''
    将一个接收者对象绑定于一个动作,调用接收者
    相应的操作,实现execute
    '''

    def execute_cmd(self):
        self.receiver.make_chicken_wing()


class Waiter:
    '''
    invoker类
    要求改命令执行这个请求
    '''
    def __init__(self):
        self.order = []

    def set_cmd(self, command):
        self.order.append(command)
        print 'order has been added'

    def notify(self):
        executed = []
        for cmd in self.order:
            cmd.execute_cmd()
            executed.append(self.order.index(cmd))
        # for i in executed:
        #     del self.order[i]


def main():
    barbucer = Barbucer()
    cmd = BakeMuttonCmd(barbucer)
    cmd2 = ChickenWingCmd(barbucer)
    girl = Waiter()
    girl.set_cmd(cmd)
    girl.set_cmd(cmd2)
    girl.notify()
    print girl.order


if __name__ == '__main__':
    main()
