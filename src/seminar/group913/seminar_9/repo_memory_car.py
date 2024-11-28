from seminar.group913.seminar_9.car import Car


class RepositoryError(Exception):
    # RepositoryError is a Python Exception
    # this means we can raise and catch it
    pass


class CarMemoryRepo:
    def __init__(self, initial_list: list):
        self._data = {}  # this field is protected, as we want to inherit it in a derived class
        # TODO Check that car id's are unique
        for c in initial_list:
            self._data[c.id] = c

    def add(self, car: Car):
        """
        Add a car
        :param car:
        :return:
        :raises: RepositoryError if car with given id already stored
        """
        if car.id in self._data:  # check that car.id is within the keys of self._data
            raise RepositoryError(f"Duplicate id {car.id} is not allowed")
        self._data[car.id] = car  # assign the value car to the key car.id

    def delete(self, car_id: int):
        """
        Delete car with given id
        :param car_id:
        :return:
        :raises: RepositoryError if car with given id does not exist
        """
        if car_id not in self._data:
            raise RepositoryError(f"Car with id {car_id} was not found")
        self._data.pop(car_id)

    def find(self, car_id) -> Car:
        """
        Find car with given id
        :param car_id:
        :return: The Car, None otherwise
        """
        return self._data[car_id] if car_id in self._data else None

    def __len__(self):
        return len(self._data)


def test_car_memory_repo():
    repo = CarMemoryRepo([])
    assert len(repo) == 0

    car_1 = Car(100, "Toyota Corolla")
    repo.add(car_1)
    assert len(repo) == 1

    assert repo.find(100) == car_1
    assert len(repo) == 1

    try:
        repo.add(car_1)
        assert False
    except RepositoryError:
        assert len(repo) == 1

    repo.delete(100)
    assert len(repo) == 0


test_car_memory_repo()
