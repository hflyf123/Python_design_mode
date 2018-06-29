# coding=utf-8
class TestPaper:
    '''
    考试卷
    '''

    def Answer1(self):
        return ''

    def Answer2(self):
        return ''

    def test_questions1(self):
        print 'Test1:A. B. C. D.'
        print '(%s)' % self.Answer1()

    def test_questions2(self):
        print 'Test1:A. B. C. D.'
        print '(%s)' % self.Answer2()


class TestPaperA(TestPaper):
    '''
    考试卷,a学生作答结果
    '''

    def Answer1(self):
        return 'B'

    def Answer2(self):
        return 'C'


class TestPaperB(TestPaper):
    '''
    考试卷,b学生作答结果
    '''

    def Answer1(self):
        return 'A'

    def Answer2(self):
        return 'D'


if __name__ == '__main__':
    s1 = TestPaperA()
    s2 = TestPaperB()
    print 'student1'
    s1.test_questions1()
    s1.test_questions2()
    print 'student2'
    s2.test_questions1()
    s2.test_questions2()
