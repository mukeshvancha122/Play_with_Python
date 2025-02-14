class Vehicle:
    country="India"

    # default constructor 
    def __init__():
        pass
    # parameterized constructor 
    def __init__(self,name,price,mileage):
        self.name=name
        self.price=price
        self.mileage=mileage
    def __str__(self):
        return f"""Vehicle details:
                Name: {self.name}, Price: {self.price}, MileageL {self.mileage} """
    def sound():
        return "Sound!"

class EV(Vehicle):
    
    def speak(self):
        return "No Sound!"
    
# instance 1: Bike
Bike=Vehicle("R15",210000,18)
print(Bike)

Car=EV()

print(EV.sound())
# instance 2: EV curv