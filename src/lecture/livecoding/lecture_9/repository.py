from lecture.livecoding.lecture_9.domain import Ingredient


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


class IngredientMemoryRepo:
    def __init__(self):
        self._data = {}  # _data is protected => classes derived from IngredientMemoryRepo can access it

    def add(self, ingr: Ingredient):
        # dictionary means (key, value) pairs where keys are immutable and unique
        if ingr.id in self._data:  # is the ingr.id already a key in the dict?
            raise DuplicateIDError("Duplicate ingredient ID")
        self._data[ingr.id] = ingr

    def remove(self, ingr_id: int) -> Ingredient:
        if ingr_id not in self._data:  # is the ingr_id already a key in the dict?
            # NOTE creating and raising exceptions is sloooooooow
            raise IDNotFoundError("ID not found")
        return self._data.pop(ingr_id)

    def find(self, ingr_id: int):
        if ingr_id not in self._data:  # is the ingr_id already a key in the dict?
            return None
        return self._data[ingr_id]

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


class IngredientTextFileRepo(IngredientMemoryRepo):
    def __init__(self):
        super().__init__()
        self.__load_file()

    def add(self, ingr: Ingredient):
        super().add(ingr)
        # if super().add(...) was successful we save the file with the updated ingredients
        self.__save_file()

    def __load_file(self):
        fin = open("ingredients.txt", "rt")
        line = fin.readline()
        while len(line) > 0:
            tokens = line.split(";")
            super().add(Ingredient(int(tokens[0]), tokens[1].strip()))
            # self._data[int(tokens[0])] = Ingredient(int(tokens[0]), tokens[1].strip())
            line = fin.readline()

    def __save_file(self):
        fout = open("ingredients.txt", "wt")  # w - write, t - text
        for ingr in self._data.values():
            fout.write(str(ingr.id) + ";" + ingr.name + "\r\n")
        fout.close()


try:
    repo = IngredientTextFileRepo()
    repo.add(Ingredient(100, "Sugar"))
except FileNotFoundError as e:
    print("yep!")
except RepositoryError as e:
    print(e)

# repo.add(Ingredient(101, "Spice"))
# repo.add(Ingredient(102, "Everything nice"))


# for elem in repo:
#     print(elem)

# print(len(repo))
# print(repo[102])

# data = [1, 2, 3, 4, 5]
# for number in data:
#     print(number)
