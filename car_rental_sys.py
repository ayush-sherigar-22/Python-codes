class Car:
    def __init__(self,car_id, brand, model):
        self.car_id=car_id
        self.brand=brand
        self.model=model
        self.is_available=True

    def display_details(self):
        print(f"Car ID :{self.car_id}")
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")
        print(f"Available: {'Yes' if self.is_available else 'No'}")
        print("-------------------------------------")

class RentalSystem :
    def __init__(self):
        self.available_cars=[]

    def add_car(self, car):
        if isinstance(car,Car):
            self.available_cars.append(car)
            print(f"Car {car.car_id} added to the rental system.")
        else: 
            print("Invalid car object")

    def rent_car (self, car_id):
        for car in self.available_cars:
            if car.car_id==car_id and car.is_available:
                car.is_available=False
                print(f"\nCar {car.car_id} rented successfully. ")
                return
        print("Car not available for rent. ")
    
    def return_car(self, car_id):
        for car in self.available_cars:
            if car.car_id == car_id and car.is_available:
                car.is_available=True
                print(f"Car {car.car_id} returned successfully.")
                return
        print("Invalid car return request. ")

    def display_availabale_car(self):
        print("\nAvailable Cars for Rent: ")
        for car in self.available_cars:
            if car.is_available:
                car.display_details()
                
    def display_rented_cars(self):
        print("Rented cars: ")
        for car in self.available_cars:
            if not car.is_available:
                car.display_details()

    

class Customers:
    def __init__(self, customer_id, name):
        self.customer_id=customer_id
        self.name = name 
        self.rented_cars=[]

    def rent_car(self, rental_system, car_id):
        rental_system.rent_car(car_id)
        self.rented_cars.append(car_id)

    def return_car(self, rental_system, car_id):
        rental_system.return_car(car_id)
        if car_id in self.rented_cars:
            self.rented_cars.remove(car_id)
    
    def display_rented_cars(self, rental_system):
        print(f"Rented Cars by {self.name}:")
        for car_id in self.rented_cars:
            for car in rental_system.available_cars:
                if car.car_id == car_id:
                    car.display_details()

if __name__=="__main__":
    car1=Car(1,"Toyota","Corolla")
    car2=Car(2,"Honda","Civic")
    car3=Car(3,"Ford","Mustang")

    rental_system=RentalSystem()
    rental_system.add_car(car1)
    rental_system.add_car(car2)
    rental_system.add_car(car3)

    customer1=Customers(101,"Alice")
    customer2=Customers(102,"Bob")

    customer1.rent_car(rental_system,1)
    customer2.rent_car(rental_system,2)

    rental_system.display_availabale_car()
    rental_system.display_rented_cars()

    customer1.display_rented_cars(rental_system)



    
    