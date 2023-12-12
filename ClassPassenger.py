from colorama import Fore, Style

class Passenger:
    def __init__ (self, firstName, lastName, passportNr):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__passportNr = passportNr

    @property
    def firstName(self):
        return self.__firstName
    @firstName.setter
    def setFirstName(self, firstName):
        self.__firstName = firstName

    @property
    def lastName(self):
        return self.__lastName
    @lastName.setter
    def setLastName(self, lastName):
        self.__lastName = lastName

    @property
    def passportNr(self):
        return self.__passportNr
    @passportNr.setter
    def setPassportNr(self, passportNr):
        self.__passportNr = passportNr

    def __str__(self):
        return "(Passenger: " + Fore.LIGHTMAGENTA_EX + self.__firstName + Style.RESET_ALL + " " + Fore.LIGHTMAGENTA_EX + self.__lastName + Style.RESET_ALL + ", PassportNr: " + Fore.LIGHTBLUE_EX + str(self.__passportNr) + Style.RESET_ALL + ")"
    def __repr__(self):
        return str(self)
    
    def __eq__(self, other):
        return self.__firstName == other.__firstName and self.__lastName == other.__lastName and self.__passportNr == other.__passportNr