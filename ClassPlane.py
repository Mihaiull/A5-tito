from colorama import Fore, Style

class Plane:
    def __init__(self, name, company, seats, destination):
        self.__name = name
        self.__company = company
        self.__seats = seats
        self.__destination = destination
        self.__passengers = []

    @property
    def name(self):
        return self.__name
    @name.setter
    def setName(self, name):
        self.__name = name

    @property
    def company(self):
        return self.__company
    @company.setter
    def setCompany(self, company):
        self.__company = company

    @property
    def seats(self):
        return self.__seats
    @seats.setter
    def setSeats(self, seats):
        self.__seats = seats

    @property
    def destination(self):
        return self.__destination
    @destination.setter
    def setDestination(self, destination):
        self.__destination = destination

    @property
    def passengers(self):
        return self.__passengers
    @passengers.setter
    def setPassengers(self, passengers):
        self.__passengers = passengers

    def __str__(self):
        return "(Plane: " + Fore.LIGHTMAGENTA_EX + self.__name + Style.RESET_ALL + ", Company: " + Fore.LIGHTBLUE_EX + self.__company + Style.RESET_ALL + ", Seats: " + Fore.LIGHTBLUE_EX + str(self.__seats) + Style.RESET_ALL + ", Destination: " + Fore.LIGHTBLUE_EX + self.__destination + Style.RESET_ALL + ", Passengers: " + Fore.LIGHTYELLOW_EX + str(self.__passengers) + Style.RESET_ALL +")"
    def __repr__(self):
        return str(self)
    
    def __eq__(self, other):
        return self.__name == other.__name and self.__company == other.__company and self.__seats == other.__seats and self.__destination == other.__destination and self.__passengers == other.__passengers