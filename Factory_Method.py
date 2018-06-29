# coding=utf-8
class LeiFeng:
    '''
    雷锋类
    '''

    def sweep(self):
        print 'LeiFeng sweep'


class Student(LeiFeng):
    '''
    学生类(雷锋类子类)
    '''

    def sweep(self):
        print 'Studnet sweep'


class Violent(LeiFeng):
    '''
    志愿者类(雷锋类子类)
    '''

    def sweep(self):
        print 'Violent sweep'


class LeiFengFactory:
    '''
    雷锋工厂
    '''

    def create_LeiFeng(self):
        lf = LeiFeng()
        return lf


class StudentFactory(LeiFengFactory):
    '''
    学生工厂(雷锋工厂类子类)
    '''

    def create_student(self):
        st = Student()
        return st


class ViolentFactory(LeiFengFactory):
    '''
    志愿者工厂(雷锋工厂子类)
    '''

    def create_violent(self):
        vi = Violent()
        return vi


def main():
    st = StudentFactory()
    vi = ViolentFactory()
    lf = LeiFengFactory()
    s = st.create_student()
    v = vi.create_violent()
    l = lf.create_LeiFeng()
    s.sweep()
    v.sweep()
    l.sweep()


if __name__ == '__main__':
    main()
