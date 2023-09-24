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
        
        result = "Rental Record for " + self.get_name() + "\n"

        for rental in self._rentals:                       
            # frequent_renter_points = rental.get_frequent_renter_points()
            # Display figures for this rental
            result += "\t" + rental.get_movie().get_title() + "\t" + str(rental.get_charge()) + "\n"            

        # Add footer lines
        result += "Amount owed is " + str(self.get_total_charge()) + "\n"
        result += "You earned " + str(self.get_total_frequent_renter_points()) + " frequent renter points"

        # print(result)
        return result
    
    

    def amount_for(self, rental):
        # this can be removed since we added get_charge() method to the classes where it access the object
        return rental.get_charge()
    
    def get_total_charge(self):

        result = 0
        for rental in self._rentals:
            result += rental.get_charge()         
        return result

    def get_total_frequent_renter_points(self):
        result = 0
        for rental in self._rentals:
            result += rental.get_frequent_renter_points()     
        return result

