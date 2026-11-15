from abc import ABC, abstractmethod
class Car(ABC):
    @abstractmethod
    def drive(self):
        pass
class Ecar(ABC):
    def drive(self):
        print("driving")
class Motor(Car):
    def drive(self):
        print("Motor Drive")
class CarMotor(Car):
    def drive(self):
        print("Self driving")


drive = Motor()
Selfdrive = CarMotor()
drive.drive()
Selfdrive.drive()

