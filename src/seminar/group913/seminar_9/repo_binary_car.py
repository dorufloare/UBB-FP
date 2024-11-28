from seminar.group913.seminar_9.car import Car

import pickle

from seminar.group913.seminar_9.repo_memory_car import CarMemoryRepo


class CarBinaryRepo(CarMemoryRepo):
    def __init__(self, initial_list: list):
        super().__init__(initial_list)
        self.__load()

    def add(self, car: Car):
        super().add(car)  # calls the add() method in class CarMemoryRepo
        # save the updated list of cars to file
        # if super().add(car) raised an exception, it means nothing was changed. This means we can exit
        # this method with the same execption without saving the file
        self.__save()

    def __load(self):
        try:
            file_in = open("cars.bin", "rb")  # r - read
            self._data = pickle.load(file_in)
            file_in.close()
        except FileNotFoundError:
            pass

    def __save(self):
        file_out = open("cars.bin", "wb")  # w = write, b = binary
        pickle.dump(self._data, file_out)
        file_out.close()


# car = Car(100, "Toyota Auris")

repo = CarBinaryRepo([])
# repo.add(Car(100, "Toyota Auris"))
print(len(repo))
# repo.add(car)

# print(len(repo))

# data = [Car(100, "Toyota Auris"), Car(101, "Toyota Corolla"), Car(102, "Audi A2")]
# data.append(data)

# file_out = open("cars.bin", "wb")  # w = write, b = binary
# pickle.dump(data, file_out)
# file_out.close()

# file_in = open("cars.bin", "rb")  # r - read
# object = pickle.load(file_in)
# print(type(object))
