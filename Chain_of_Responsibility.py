# coding=utf-8
# coding=utf-8

class Request:
    '''
    申请类
    '''
    def __init__(self, tcontent, tnum):
        self.content = tcontent
        self.num = tnum


class Manager:
    '''
    管理者类,设置管理者上级
    申请请求
    '''
    def __init__(self, temp):
        self.name = temp

    def set_successor(self, temp):
        self.manager = temp

    def get_request(self, req):
        pass


class CommonManager(Manager):
    '''
    普通经理,遇到处理不了的请求
    将会传递给上级
    '''
    def get_request(self, req):
        if req.num >= 0 and req.num < 10:
            print('%s handled %d request.') % (self.name, req.num)
        else:
            self.manager.get_request(req)


class MajorDomo(Manager):
    '''
    总监
    '''
    def get_request(self, req):
        if req.num >= 10:
            print('%s handled %d request.') % (self.name, req.num)


if __name__ == '__main__':
    common = CommonManager('Zhang')
    major = MajorDomo('Lee')
    common.set_successor(major)
    req = Request('rest', 33)
    common.get_request(req)
    req2 = Request('salary', 3)
    common.get_request(req2)
