# coding=utf-8
class Context:
    '''
    包含解释器以外的一些全局信息
    '''
    def __init__(self):
        self.input = ''
        self.output = ''


class AbstractExpersstion:
    '''
    抽象表达式,声明一个抽象的解释操作,
    这个接口为抽象语法树中的所有节点共享
    '''
    def interpret(self, context):
        pass

class Expression(AbstractExpersstion):
    def interpret(self, context):
        print('terminal interpret')

class NonterminalExpression(AbstractExpersstion):
    def interpret(self, context):
        print('Non terminal interpret')

if __name__ == '__main__':
    context = ''
    c = []
    c = c + [Expression()]
    c = c + [NonterminalExpression()]
    c = c + [Expression()]
    c = c + [Expression()]
    for a in c:
        a.interpret(context)