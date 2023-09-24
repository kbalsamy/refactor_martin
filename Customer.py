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
            this_amount = self.amount_for(rental)            

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
        this_amount = 0
        # Determine the rental amount based on the movie's price code and rental duration
        if rental.get_movie().get_price_code() == Movie.REGULAR:
            this_amount += 2
            if rental.get_days_rented() > 2:
                this_amount += (rental.get_days_rented() - 2) * 1.5
        elif rental.get_movie().get_price_code() == Movie.NEW_RELEASE:
            this_amount += rental.get_days_rented() * 3
        elif rental.get_movie().get_price_code() == Movie.CHILDRENS:
            this_amount += 1.5
            if rental.get_days_rented() > 3:
                this_amount += (rental.get_days_rented() - 3) * 1.5
        return this_amount
