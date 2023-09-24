from movie import Movie

class Customer:
    def __init__(self, name):
        self._name = name
        self._rentals = []

    def add_rental(self, arg):
        self._rentals.append(arg)

    def get_name(self):
        return self._name


    def statement(self):
        total_amount = 0
        frequent_renter_points = 0
        result = "Rental Record for " + self.get_name() + "\n"

        for rental in self._rentals:
            # decomposed -> breaking code into small chunks. 
            # extract method
            this_amount = rental.get_charge()           

            # Add bonus for a two-day new release rental
            if rental.get_movie().get_price_code() == Movie.NEW_RELEASE and rental.get_days_rented() > 1:
                frequent_renter_points += 1

            # Display figures for this rental
            result += "\t" + rental.get_movie().get_title() + "\t" + str(this_amount) + "\n"
            total_amount += this_amount

        # Add footer lines
        result += "Amount owed is " + str(total_amount) + "\n"
        result += "You earned " + str(frequent_renter_points) + " frequent renter points"

        # print(result)
        return result
    
    

    def amount_for(self, rental):
        # this can be removed since we added get_charge() method to the classes where it access the object
        return rental.get_charge()
