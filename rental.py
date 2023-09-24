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
        return self._movie.get_charge(self.get_days_rented())
    
    def get_frequent_renter_points(self):
        # Add bonus for a two-day new release rental
        return self._movie.get_frequent_renter_points(self.get_days_rented())