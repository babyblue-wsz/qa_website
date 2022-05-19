class BenzCar:
    brand = '奔驰'
    country = '德国'

    @staticmethod
    def pressHorn():
        print('嘟嘟~~~~~~')

    def __init__(self, color, engineSN):
        self.color = color  # 颜色
        self.engineSN = engineSN  # 发动机编号

    def changeColor(self, newColor):
        self.color = newColor


class Benz2016(BenzCar):
    price = 580000
    model = 'Benz2016'


class Benz2018(BenzCar):
    price = 880000
    model = 'Benz2018'

    # def __init__(self, color, engineSN, weight):
    #     # 先调用父类的初始化方法
    #     BenzCar.__init__(self, color, engineSN)
    #     self.weight = weight  # 车的重量
    #     self.oilweight = 0  # 油的重量
    #
    def __init__(self, color, engineSN, weight):
        super().__init__(color, engineSN)
        self.weight = weight  # 车的重量
        self.oilweight = 0  # 油的重量
# 加油
    def fillOil(self, oilAdded):
        self.oilweight += oilAdded
        self.weight += oilAdded

if __name__ == '__main__':
    car2 = Benz2018('blue', '111135545988', 1500)
    print(car2.oilweight)
    print(car2.weight)
    car2.fillOil(50)
    print(car2.oilweight)
    print(car2.weight)

