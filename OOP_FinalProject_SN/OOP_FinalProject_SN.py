import BikeShop as BS


objShop1 = BS.BikeRental("Mountain Bikes", 10)
objShop2 = BS.BikeRental("Touring Bikes", 10)
objShop3 = BS.BikeRental("Road Bikes", 10)


def New_Customer():
    name = BS.Customer.get_name()
    ID = BS.Customer.get_ID()
    biketype = BS.Customer.biketype_selection()
    bikes = BS.Customer.requestBike()
    rentalBasis = BS.Customer.Basis_Selection()
    rentalTime = BS.Customer.Time(rentalBasis)
    if rentalBasis == "Hour":
        BS.BikeRental.rentBikeOnHourlyBasis(biketype, bikes)
    elif rentalBasis == "Day":
        BS.BikeRental.rentBikeOnDailyBasis(biketype, bikes)
    elif rentalBasis == "Week":
        BS.BikeRental.rentBikeOnWeeklyBasis(biketype, bikes)
    objCus = BS.Customer(name, ID, biketype, bikes, rentalBasis, rentalTime)



def main():
    

    while True:
        print("\nWelcome to the Bike Rental Shop")
        print("1. New Customer Rental")
        print("2. Rental Return")
        print("3. Show Inventory")
        print("4. End of Day")
        print("5. Exit Program")
        choice = input("Please make a selection: ")
        print("")

        if choice == '1':
            New_Customer()
        elif choice == '2':
            name = input("Enter your name: ")
            ID = int(input("Enter your ID: "))
            for customer in BS.Customer.customers:
                if customer.name == name:
                    biketype = customer.biketype
                    bikes = customer.bikes
                    rentalBasis = customer.rentalBasis
                    rentalTime = customer.rentalTime
                    BS.BikeRental.returnBike(name, ID, biketype, bikes, rentalBasis, rentalTime)
                else:
                    print("Your information could not be located, please try again.")
                    main()
        elif choice == '3':
            BS.BikeRental.displaystock()
        elif choice == '4':
            BS.BikeRental.end_of_day()
            BS.Customer.displayCustomers()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()