from lecture.livecoding.lecture_9.domain.bakery_object import BakeryObject
from lecture.livecoding.lecture_9.domain.ingredient import Ingredient


class RepositoryError(Exception):
    pass


class DuplicateIDError(RepositoryError):
    pass


class IDNotFoundError(RepositoryError):
    pass


class RepositoryIterator():
    def __init__(self, data):
        self.__data = data
        self.__pos = -1

    def __next__(self):
        self.__pos += 1
        if len(self.__data) == self.__pos:
            # we have run out of elements in the data structure
            raise StopIteration()

        return self.__data[self.__pos]


class BakeryObjectMemoryRepo:
    def __init__(self):
        self._data = {}  # _data is protected => classes derived from IngredientMemoryRepo can access it

    def add(self, bakery_object: BakeryObject):
        # dictionary means (key, value) pairs where keys are immutable and unique
        if bakery_object.id in self._data:
            raise DuplicateIDError("Duplicate ingredient ID")
        self._data[bakery_object.id] = bakery_object

    def remove(self, bakery_object_id: int) -> BakeryObject:
        if bakery_object_id not in self._data:
            # NOTE creating and raising exceptions is sloooooooow
            raise IDNotFoundError("ID not found")
        return self._data.pop(bakery_object_id)

    def find(self, bakery_object_id: int):
        if bakery_object_id not in self._data:  # is the ingr_id already a key in the dict?
            return None
        return self._data[bakery_object_id]

    def __iter__(self):
        # create an iterator for the repository
        # https://refactoring.guru/design-patterns/iterator
        return RepositoryIterator(list(self._data.values()))

    def __len__(self):
        return len(self._data)

    def __getitem__(self, item):
        if item not in self._data:
            return None
        return self._data[item]


class IngredientTextFileRepo(BakeryObjectMemoryRepo):
    def __init__(self):
        super().__init__()
        self.__load_file()

    def add(self, bakery_object: Ingredient):
        super().add(bakery_object)
        # if super().add(...) was successful we save the file with the updated ingredients
        self.__save_file()

    def remove(self, bakery_object_id: int) -> BakeryObject:
        bakery_object = super().remove(bakery_object_id)
        self.__save_file()
        return bakery_object

    def __load_file(self):
        fin = open("ingredients.txt", "rt")
        line = fin.readline()
        while len(line) > 0:
            tokens = line.split(",")
            super().add(Ingredient(int(tokens[0]), tokens[1].strip(), int(tokens[2])))
            line = fin.readline()

    def __save_file(self):
        fout = open("ingredients.txt", "wt")  # w - write, t - text
        for ingr in self._data.values():
            fout.write(str(ingr.id) + "," + ingr.name + "," + str(ingr.quantity) + "\r\n")
            fout.close()


if __name__ == "__main__":
    try:
        repo = IngredientTextFileRepo()
        # repo.add(Ingredient(100, "Sugar"))

        for ingredient in repo:
            print(ingredient)

    except FileNotFoundError as e:
        print("yep!")
    except RepositoryError as e:
        print(e)
