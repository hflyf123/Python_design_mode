# coding=utf-8
class BMW:
    '''
    抽象宝马类,有suv和普通轿车两种实现
    '''

    def get_car_type(self):
        pass

    def get_start(self):
        pass


class Benz:
    '''
    抽象奔驰类,有suv和普通轿车两种实现
    '''

    def get_car_type(self):
        pass

    def get_start(self):
        pass


class BMWSuv(BMW):
    '''
    具体产品,宝马suv
    '''

    def get_car_type(self):
        print('This is BMW Suv')

    def get_start(self):
        print('BMW suv is starting..........')


class BMWCar(BMW):
    '''
    具体产品,宝马轿车
    '''

    def get_car_type(self):
        print('This is BMW Suv')

    def get_start(self):
        print('BMW car is starting..........')


class BenzSuv(Benz):
    '''
    具体产品,奔驰suv
    '''

    def get_car_type(self):
        print('This is Benz Suv')

    def get_start(self):
        print('Benz suv is starting..........')


class BenzCar(Benz):
    '''
    具体产品,奔驰轿车
    '''

    def get_car_type(self):
        print('This is Benz Car')

    def get_start(self):
        print('Benz car is starting..........')


class IFactory:
    '''
    抽象工厂,包含所有产品创建的抽象方法
    '''

    def create_Benz(self):
        pass

    def create_BMW(self):
        pass


class SuvFactory(IFactory):
    '''
    具体的工厂,创建具有特定实现的产品对象
    suv工厂,可以生产宝马奔驰suv
    '''

    def create_Benz(self):
        temp = BenzSuv()
        return temp

    def create_BMW(self):
        temp = BMWSuv()
        return temp


class CarFactory(IFactory):
    '''
    具体的工厂,创建具有特定实现的产品对象
    轿车工厂,可以生产宝马奔驰轿车
    '''

    def create_Benz(self):
        temp = BenzCar()
        return temp

    def create_BMW(self):
        temp = BMWCar()
        return temp


if __name__ == '__main__':
    factory = SuvFactory()
    benzsuv = factory.create_Benz()
    bmwsuv = factory.create_BMW()
    benzsuv.get_car_type()
    benzsuv.get_start()
    print('*********************************')
    bmwsuv.get_car_type()
    bmwsuv.get_start()
