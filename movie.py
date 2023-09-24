class Movie:
    CHILDRENS = 2
    REGULAR = 0
    NEW_RELEASE = 1

    def __init__(self, title, price_code):
        self._title = title
        self._price_code = price_code

    def get_price_code(self):
        return self._price_code

    def set_price_code(self, arg):
        self._price_code = arg

    def get_title(self):
        return self._title
    
    def get_charge(self, days_rented):

        this_amount = 0
        # Determine the rental amount based on the movie's price code and rental duration
        if self.get_price_code() == self.REGULAR:
            this_amount += 2
            if days_rented > 2:
                this_amount += (days_rented - 2) * 1.5
        elif self.get_price_code() == self.NEW_RELEASE:
            this_amount += days_rented * 3
        elif self.get_price_code() == self.CHILDRENS:
            this_amount += 1.5
            if days_rented > 3:
                this_amount += (days_rented - 3) * 1.5
        return this_amount
    
    def get_frequent_renter_points(self, days_rented):

        if self.get_price_code() == self.NEW_RELEASE and days_rented > 1:
            return 2
        else:
            return 1
