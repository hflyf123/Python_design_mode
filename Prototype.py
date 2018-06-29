# coding=utf-8
import copy


# class WorkExp:
#     place = ''
#     year = 0


class Resume:
    name = ''
    age = 0

    def __init__(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_work_exp(self, place, year):
        self.place = place
        self.year = year

    def display(self):
        print self.age
        print self.place
        print self.year

    def clone(self):
        # 不是克隆，只是返回了自身
        return self

if __name__ == '__main__':
    a = Resume('lyf')
    b = a.clone()
    c = copy.copy(a)
    d = copy.deepcopy(a)
    a.set_age(7)
    b.set_age(12)
    c.set_age(15)
    d.set_age(18)
    a.set_work_exp('PrimarySchool', 1996)
    b.set_work_exp('MidSchool', 2001)
    c.set_work_exp('HighSchool', 2004)
    d.set_work_exp('University', 2007)
    a.display()
    b.display()
    c.display()
    d.display()

