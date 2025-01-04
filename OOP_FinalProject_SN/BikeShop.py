class class1(object):
    """description of class"""
       
class BikeRental:
    
    stock = []
    daily_revenue = 0
    daily_bikes_rented = 0

    def __init__(self, bikename, stock=0):
        self.bikename = bikename
        self.stock = stock 
        BikeRental.stock.append(self)

    @classmethod
    def displaystock(self):
        for bike in self.stock:
            print(f"We currently have {bike.stock} {bike.bikename} available to rent.")

    @classmethod
    def end_of_day(self):
        print("End of Day Summary:")
        print(f"Total Bikes Rented: {self.daily_bikes_rented}")
        print(f"Daily Revenue Collected: ${self.daily_revenue:.2f}")

    @classmethod
    def rentBikeOnHourlyBasis(self, bikename, n):
        if n <= 0:
            print("Number of bikes should be positive!")
            return None
        
        for bike in self.stock:
            if bike.bikename == bikename:
                if n > bike.stock:
                    print(f"Sorry! We currently have {bike.stock} {bikename} bikes available to rent.")
                    return None
                else:
                    print(f"You have rented {n} {bike.bikename} on an hourly basis.")
                    print("You will be charged $5 for each hour per bike.")
                    print("We hope that you enjoy our service.")
                    bike.stock -= n
                    self.daily_bikes_rented += n
                    return

    @classmethod
    def rentBikeOnDailyBasis(self, bikename, n):
        if n <= 0:
            print("Number of bikes should be positive!")
            return None
        
        for bike in self.stock:
            if bike.bikename == bikename:
                if n > bike.stock:
                    print(f"Sorry! We currently have {bike.stock} {bikename} bikes available to rent.")
                    return None
                else:
                    print(f"You have rented {n} {bike.bikename} on a daily basis.")
                    print("You will be charged $20 for each day per bike.")
                    print("We hope that you enjoy our service.")
                    bike.stock -= n
                    self.daily_bikes_rented += n
                    return

    @classmethod
    def rentBikeOnWeeklyBasis(self, bikename, n):
        if n <= 0:
            print("Number of bikes should be positive!")
            return None
        
        for bike in self.stock:
            if bike.bikename == bikename:
                if n > bike.stock:
                    print(f"Sorry! We currently have {bike.stock} {bikename} bikes available to rent.")
                    return None
                else:
                    print(f"You have rented {n} {bike.bikename} on a weekly basis.")
                    print("You will be charged $60 for each week per bike.")
                    print("We hope that you enjoy our service.")
                    bike.stock -= n
                    self.daily_bikes_rented += n
                    return
    
    @classmethod
    def returnBike(self, name, ID, biketype, bikes, rentalBasis, rentalTime):
        """
        1. Accept a rented bike from a customer
        2. Replenish the inventory
        3. Return a bill
        """
        bill = 0
        if rentalTime and rentalBasis and bikes:
            for bike in self.stock:
                if bike.bikename == biketype:
                    bike.stock += bikes

            # Calculate the bill
            if rentalBasis == "Hour":
                bill = 5 * bikes * rentalTime
            elif rentalBasis == "Day":
                bill = 20 * bikes * rentalTime
            elif rentalBasis == "Week":
                bill = 60 * bikes * rentalTime

            discount = input("Enter discount code (if any): ")
            if discount and discount.endswith("BBP"):
                bill *= 0.9

            # Family discount calculation
            if 3 <= bikes <= 5:
                print("You are eligible for Family rental promotion of 30% discount")
                bill *= 0.7

            print("Thanks for returning your bike. Hope you enjoyed our service!")
            print(f"That would be ${bill:.2f}")

            self.daily_revenue += bill 
            return 
        
        else:
            print("Are you sure you rented a bike with us?")
            return None


class Customer:

    customers = []

    def __init__(self, name, ID, biketype, bikes, rentalBasis, rentalTime):
        """
        Constructor method to instantiate customer objects.
        """
        self.name = name
        self.ID = ID
        self.biketype = biketype
        self.bikes = bikes
        self.rentalBasis = rentalBasis
        self.rentalTime = rentalTime
        self.bill = 0
        self.discount = 0
        Customer.customers.append(self)


    def get_name():
        name = input("Name: ")
        if name == "":
            raise Exception("Must Enter a Name.")
        else:
            return name

    def get_ID():
        ID = input("Enter an ID: ")
        if ID == "":
            raise Exception("Must Enter an ID.")
        else:
            return ID



    def biketype_selection():
        biketype = input("Would you like to rent a Mountain Bike, Touring Bike, or a Road Bike? (Enter 'M', 'T', or 'R'): ").strip().upper()
        if biketype == "":
            raise Exception("Must enter 'M' to select Mountain Bike, 'T' to select Touring Bike, or 'R' to select Road Bike.")
        elif biketype == "M":
            return "Mountain Bikes"
        elif biketype == "R":
            return "Road Bikes"
        elif biketype == 'T':
            return "Touring Bikes"
        else:
            raise Exception("Must enter 'M' to select Mountain Bike, 'T' to select Touring Bike, or 'R' to select Road Bike.")


    def requestBike():
        """
        Takes a request from the customer for the number of bikes.
        """
                      
        bikes = input("How many bikes would you like to rent?: ")
        
        # implement logic for invalid input
        try:
            bikes = int(bikes)
        except ValueError:
            raise Exception("That's not a positive integer!")
            return -1
        if bikes < 1:
            raise Exception("Invalid input. Number of bikes should be greater than zero!")
        else:
            return bikes
     

    def Basis_Selection():
        basis = input("Would you like to pay for the hour, day, or week?('H' for Hour, 'D' for Day, 'W' for Week): ").strip().upper()
        if basis == "":
            raise Exception("Must enter 'H' to select Hour, 'D' to select Day, or 'W' to select Week.")
        elif basis == "H":
            return "Hour"
        elif basis == "D":
            return "Day"
        elif basis == 'W':
            return "Week"
        else:
            raise Exception("Must enter 'H' to select Hour, 'D' to select Day, or 'W' to select Week.")

    def Time(basis):
        time = input(f"How many {basis}s would you like to rent for?: ")
        try:
            time = int(time)
        except ValueError:
            print("Must enter an integer that is positive")
        if time < 1:
            raise Exception("Must enter a number greater than 0.")
        elif time > 99:
            raise Exception(f"Can only rent for up to 99 {Basis}s.")
        else:
            return time



    def returnBike(self):
        """
        Allows customers to return their bikes to the rental shop.
        """
        if self.rentalBasis and self.rentalTime and self.bikes:
            return self.rentalTime, self.rentalBasis, self.bikes  
        else:
            return 0,0,0

    @classmethod
    def displayCustomers(cls):
        for i in cls.customers:
            print(f"Name: {i.name}, ID: {i.ID}      Order: rented {i.bikes} {i.biketype}(s) for {i.rentalTime} {i.rentalBasis}s.")
