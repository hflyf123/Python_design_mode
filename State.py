# coding=utf-8
class State:
    '''
    state
    抽象状态类,定义一个接口以封装与context的
    一个特定状态相关的行为
    '''
    def write_program(self, w):
        pass

class Work:
    '''
    context
    维护一个具体状态子类的实例,这个实例
    定义当前的状态
    '''
    def __init__(self):
        self.hour = 9
        self.current = ForenoonState()
    def set_state(self, temp):
        self.current = temp
    def write_program(self):
        self.current.write_program(self)

class NoonState(State):
    '''
    concrete_state
    具体状态,每一个子类实现一个与context
    的一个状态
    '''
    def write_program(self, w):
        print('noon working')
        if w.hour < 13:
            print('fun')
        else:
            print('need to rest')

class ForenoonState(State):
    def write_program(self, w):
        if w.hour < 12:
            print('morning working')
            print('energetic')
        else:
            w.set_state(NoonState())
            w.write_program()

if __name__ == '__main__':
    mywork = Work()
    mywork.hour = 9
    mywork.write_program()
    mywork.hour = 14
    mywork.write_program()

