class Car(object):
    """
    Unless otherwise specified, all classes are subclasses of object

    """

    def __init__(self, car_id: int, model: str):
        self.__id = car_id  # __ means private => cannot be accessed from outside the class
        self.__model = model

    # if you want to read the id but not allow changing it, we can implement a read-only property

    @property
    def id(self):
        return self.__id

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value: str):
        self.__model = new_value

    def __str__(self):
        return str(self.id) + " " + self.__model  # __str__ is inside the class so it can access __model


class Bus(Car):
    """
    class Bus is derived from class Car
    what this means:
        1. All objects of type Bus are also objects of type Car
        1. a Bus has all the non-private fields and methods of a Car
    """

    def __init__(self, bus_id: int, model: str, no_seats: int):
        # we initialize the Car specific fields using the Car constructor
        super().__init__(bus_id, model)
        # we initialize the Bus-specific parts (what separates the bus from a car)
        self.__seats = no_seats

    @property
    def seats(self):
        return self.__seats


if __name__ == "__main__":
    car = Car(100, "Toyota Auris")
    # bus = Bus(101, "Volvo C18")
    car.model += "Audi"  # <=> car.model = car.model + "Audi"

    # print(car.id)
    # print(str(car))
    # print(bus.model, bus.seats)
    # print(car.seats)
