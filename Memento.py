# coding=utf-8
class Originator:
    '''
    负责创建备忘录memo,用以记录当前时刻它的
    内部状态,并可使用备忘录恢复内部状态.
    '''
    def __init__(self):
        self.state = ''
    def show(self):
        print(self.state)
    def create_memo(self):
        return Memo(self.state)
    def set_memo(self, memo):
        self.state = memo.state

class Memo:
    '''
    负责存储对象originator的内部状态,
    并可防止originator对象以外的其他对象
    访问备忘录memo
    '''
    __state = ''
    def __init__(self, ts):
        self.state = ts

class Caretaker:
    '''
    负责保存备忘录memo
    '''
    memo = ''

if __name__ == '__main__':
    on = Originator()
    on.state = 'on'
    on.show()
    c = Caretaker()
    c.memo = on.create_memo()
    on.state = 'off'
    on.show()
    on.set_memo(c.memo)
    on.show()