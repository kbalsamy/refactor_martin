from movie import Movie

class Rental:
    def __init__(self, movie, days_rented):
        self._movie = movie
        self._days_rented = days_rented

    def get_days_rented(self):
        return self._days_rented

    def get_movie(self):
        return self._movie
    
    
    def get_charge(self):

        this_amount = 0
        # Determine the rental amount based on the movie's price code and rental duration
        if self.get_movie().get_price_code() == Movie.REGULAR:
            this_amount += 2
            if self.get_days_rented() > 2:
                this_amount += (self.get_days_rented() - 2) * 1.5
        elif self.get_movie().get_price_code() == Movie.NEW_RELEASE:
            this_amount += self.get_days_rented() * 3
        elif self.get_movie().get_price_code() == Movie.CHILDRENS:
            this_amount += 1.5
            if self.get_days_rented() > 3:
                this_amount += (self.get_days_rented() - 3) * 1.5
        return this_amount
    
    def get_frequent_renter_points(self):
        # Add bonus for a two-day new release rental
        if self.get_movie().get_price_code() == Movie.NEW_RELEASE and self.get_days_rented() > 1:
            return 2
        else:
            return 1