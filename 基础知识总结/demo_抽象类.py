
import abc

class Car(metaclass=abc.ABCMeta):
    # ___metaclass__=abc.ABCMeta

    @abc.abstractclassmethod
    def Activate(self):
        '''
        启动
        :return:
        '''
        return

    @abc.abstractclassmethod
    def Run(self):
        '''
        行驶
        :return:
        '''
        return


class Bus(Car):

    def Activate(self):
        print("公交车启动了")

    # def Run(self):
    #     print("公交车在行驶")

# Car.register(Bus)、


def main():
    bus=Bus()
    # bus.Activate()
    # bus.Run()

if __name__ == '__main__':
    main()
