class Encapsulation:

    def __init__(self, name):
        self.__name = name

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, value):
        self.__name = value

    @staticmethod
    def return_static_method_message():
        print('That`s the static method!')

# staticmethod
# is callable without initialization
Encapsulation.return_static_method_message()

enc1 = Encapsulation('1')
print(enc1.Name)

enc1.Name = '2'
print(enc1.Name)

class Car:

    # initialize class Car
    def __init__(self, model):
        # initialization of the property
        self.model = model

    # create the model property
    @property
    def model(self):
        return self.__model

    # setter for creating properties
    @model.setter
    def model(self, model):
        if model < 2000:
            self.__model = 2000
        elif model > 2018:
            self.__model = 2018
        else:
            self.__model = model

    def get_car_model(self):
        return "Год выпуска модели " + str(self.model)


carA = Car(2088)
print(carA.get_car_model())