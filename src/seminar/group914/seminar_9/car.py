class Car(object):
    # class names should start with uppercase letter
    def __init__(self, car_id: int, license_plate: str, color: str = "yellow"):
        self.__id = car_id
        self.__license_plate = license_plate
        self.__color = color

    # let's use properties as setters/getters
    # suppose we want to read the id but we don't want to change it
    #  => in this case we make a read-only property

    @property
    def id(self):
        return self.__id

    @property
    def license(self):
        return self.__license_plate

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, new_value: str):
        if new_value == "grey":
            raise ValueError("No grey cars allowed")
        self.__color = new_value

    # def __repr__(self):
    #     return str(self)

    def __str__(self):
        return str(self.id) + " " + self.license + " " + self.color


if __name__ == "__main__":
    cary = Car(100, "CJ 99 ABC")
    cary.color = "blue"
    cary.color += "y"  # <=> car.color = car.color + "y"
    print(cary)
