class Ingredient(object):  # a class is by default derived from Python's object class
    def __init__(self, ingr_id: int, name: str):
        self.__id = ingr_id
        self.__name = name

    # id is a read-only property (it has no setter)
    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_value: str):
        # NOTE We can add proper validation here
        self.__name = new_value

    def __str__(self):
        # super() - goes to the base class of this
        # return super().__str__() + "abcd"
        return f"Ingredient id={self.id} is {self.name}"


class Flour(Ingredient):
    """
    class Flour is a subclass of Ingredient, all Flour objects are also Ingredient objects
    Non-private fields and methods of class Ingredient are available in Flour

    """

    def __init__(self, flour_id: int, name: str, grain_type: str):
        # we call Ingredient.__init__ to initialize the Ingredient part of Flour
        super().__init__(flour_id, name)
        self.__grain_type = grain_type

    @property
    def grain_type(self):
        return self.__grain_type

    def __str__(self):
        return super().__str__() + f" with grain type {self.grain_type}"

if __name__ == "__main__":
    ingr = Ingredient(100, "Sugar")
    flour = Flour(101, "Bakery flour", "wheat")
    # print(flour)

    print(type(ingr), type(flour))
    print(type(ingr) == type(flour))
    print(isinstance(flour, Flour))
    print(isinstance(flour, Ingredient))
    print(isinstance(ingr, Flour))
