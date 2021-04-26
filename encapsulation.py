class Encapsulation():

    def __init__(self, name):
        self.__name = name

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, value):
        self.__name = value

    @staticmethod
    def ReturnStaticMethodMessage():
        print('That`s the static method!')

Encapsulation.ReturnStaticMethodMessage()

enc1 = Encapsulation('1')
print(enc1.Name)

enc1.Name = '2'
print(enc1.Name)

# class Car:
#
#     # создаем конструктор класса Car
#     def __init__(self, model):
#         # Инициализация свойств.
#         self.model = model
#
#     # создаем свойство модели.
#     @property
#     def model(self):
#         return self.__model
#
#     # Сеттер для создания свойств.
#     @model.setter
#     def model(self, model):
#         if model < 2000:
#             self.__model = 2000
#         elif model > 2018:
#             self.__model = 2018
#         else:
#             self.__model = model
#
#     def getCarModel(self):
#         return "Год выпуска модели " + str(self.model)
#
#
# carA = Car(2088)
# print(carA.getCarModel())