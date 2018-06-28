# -*- coding:utf-8 -*-
'''
四则运算计算器，根据用户的输入产生相应的运算类，用这个运算类处理具体的运算。
'''


class Operation:
    '''
    操作类
    '''
    op1 = 0
    op2 = 0

    def get_result(self):
        pass


class OperationAdd(Operation):
    '''
    加法操作类
    '''

    def get_result(self):
        return self.op1 + self.op2


class OperationSub(Operation):
    '''
    减法操作类
    '''

    def get_result(self):
        return self.op1 - self.op2


class OperationMul(Operation):
    '''
    乘法操作类
    '''

    def get_result(self):
        return self.op1 * self.op2


class OperationDiv(Operation):
    '''
    除法操作类
    '''

    def get_result(self):
        try:
            result = self.op1 / self.op2
            return result
        except:
            print 'error :divided by zero'
            return 0


class OperationUndef(Operation):
    '''
    未识别符号类
    '''

    def get_result(self):
        print 'Undefine operation'
        return 0


class OperationFactory:
    '''
    操作类工厂
    '''
    operation = {}
    operation['+'] = OperationAdd()
    operation['-'] = OperationSub()
    operation['*'] = OperationMul()
    operation['/'] = OperationDiv()

    def create_operation(self, ch):
        if ch in self.operation:
            op = self.operation[ch]
        else:
            op = OperationUndef()
        return op


if __name__ == '__main__':
    op = raw_input('operator:')
    opa = input('a:')
    opb = input('b:')
    factory = OperationFactory()
    ca = factory.create_operation(op)
    ca.op1 = opa
    ca.op2 = opb
    print ca.get_result()
