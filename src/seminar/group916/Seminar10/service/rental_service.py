from Seminar916.Seminar10.domain.rentalValidator import RentalValidator
from Seminar916.Seminar10.repository.text_repo import RentalRepository, ClientTextFileRepository, CarTextFileRepository
from Seminar916.Seminar10.service.car_service import CarService
from seminar10.domain.rental import Rental
from seminar10.repository.memory_repo import MemoryRepository
from Seminar916.Seminar10.service.client_service import ClientService
from datetime import date
from Seminar916.Seminar10.domain.car import Car
from Seminar916.Seminar10.domain.client import Client

class CarRentalDaysDTO:
    # Data Transfer Object between service and UI layer
    def __init__(self, car, rental_days):
        self._car = car
        self._rental_days = rental_days

    @property
    def car(self):
        return self._car

    @property
    def days(self):
        return self._rental_days

    def __le__(self, other):
        # NOTE for sorting
        #return self._car.model < other.model
        pass

    def __str__(self):
        return str(self.days) + " for car " + str(self.car)

class RentalService:
    def __init__(self, repo: MemoryRepository, clientService: ClientService, carService: CarService, rentalValidator: RentalValidator):
        self.__repo = repo
        self.__clientService = clientService
        self.__carService = carService
        self.__rentalValidator = rentalValidator

    def get(self, rental_id: int) -> Rental:
        return self.__repo[rental_id]

    def getAll(self):
        return self.__repo

    def add(self, id: int, end: date, start: date, client: Client, car: Car):
        # TODO add checks that car and client are indeed actual valid instances from carService and clientService
        newRental = Rental(id, start, end, client, car)

        self.__rentalValidator.validate(newRental)
        self.__repo.add(newRental)

    def statistic_cars_by_rental_days(self):
        # NOTE keys are car ids, values are total rental days
        rental_dict = {}

        for rental in self.__repo:
            print(rental)
            if rental.car.id not in rental_dict:
                rental_dict[rental.car.id] = len(rental)
            else:
                rental_dict[rental.car.id] += len(rental)

        # TODO add all cars that were never rented
        result = []
        for key in rental_dict:
            car = self.__carService.get(key)
            result.append(CarRentalDaysDTO(car, rental_dict[key]))

        # sort by number of rental days
        result.sort(key=lambda x: x.days, reverse=True)
        return result

if __name__=="__main__":
    rentalRepo = RentalRepository()

    clientRepo = ClientTextFileRepository("clients.txt")
    clientService = ClientService(clientRepo)

    carRepo = CarTextFileRepository("cars.txt")
    carService = CarService(carRepo)

    rentalValidator = RentalValidator()

    rentalService = RentalService(rentalRepo, clientService, carService, rentalValidator)

    car1 = Car(99, "BN 99 USB", "Dacia", "Sandero", "pink")
    client = Client(555, "Ion Ion")

    rentalService.add(90, date(2025, 1, 1), date(2025, 1, 1), client, car1)


