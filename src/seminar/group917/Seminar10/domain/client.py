class Client:
    def __init__(self, clientId, name):
        self.__id = clientId
        self._name = name

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def __eq__(self, z):
        # don't compare apples to oranges
        if type(z) != Client:
            return False
        # just look at the id field
        return self.id == z.id

    def __str__(self):
        return f"{self.id} - {self.name}"

    def __repr__(self):
        return str(self)


if __name__ == "__main__":
    c1 = Client(1000, "Popescu Ana")
    c2 = Client(1001, "Popescu Ana")
    # print(c1 == c2)
    # print(repr(c1))
    print({1000: c1, 1001: c2})