# from abc import ABC, abstractmethod

class Price():

    def __init__(self):
        pass
    
    def get_price_code():
        pass
    
    def get_charge(self, days_rented):
        pass 
        # this_amount = 0
        # # Determine the rental amount based on the movie's price code and rental duration
        # if self.get_price_code() == Movie.REGULAR:
        #     this_amount += 2
        #     if days_rented > 2:
        #         this_amount += (days_rented - 2) * 1.5
        # elif self.get_price_code() == Movie.NEW_RELEASE:
        #     this_amount += days_rented * 3
        # elif self.get_price_code() == Movie.CHILDRENS:
        #     this_amount += 1.5
        #     if days_rented > 3:
        #         this_amount += (days_rented - 3) * 1.5
        # return this_amount

    def get_frequent_renter_points(self, days_rented):

        # if self.get_price_code() == Movie.NEW_RELEASE and days_rented > 1:
        #     return 2
        # else:
        return 1

class ChildrensPrice(Price):    

    def get_price_code(self):
        return Movie.CHILDRENS

    def get_charge(self, days_rented):
        this_amount = 0
        if self.get_price_code() == Movie.CHILDRENS:
            this_amount += 1.5
            if days_rented > 3:
                this_amount += (days_rented - 3) * 1.5
        return this_amount
    

    
    
class NewReleasePrice(Price):
    
    def get_price_code(self):
        return Movie.NEW_RELEASE
    
    def get_charge(self, days_rented):
        this_amount = 0
        if self.get_price_code() == Movie.NEW_RELEASE:
            this_amount += days_rented * 3
        return this_amount

    def get_frequent_renter_points(self, days_rented):

        if self.get_price_code() == Movie.NEW_RELEASE and days_rented > 1:
            return 2
        else:
            return 1
   
    
class RegularPrice(Price):
    def get_price_code(self):
        return Movie.REGULAR
    
    def get_charge(self, days_rented):
        this_amount = 0
        if self.get_price_code() == Movie.REGULAR:
            this_amount += 2
            if days_rented > 2:
                this_amount += (days_rented - 2) * 1.5
        return this_amount
        
        
    




class Movie:

    CHILDRENS = 2
    REGULAR = 0
    NEW_RELEASE = 1

    def __init__(self, title, price_code):
        self._title = title        
        self._price = self.set_price_code(price_code)
    

    def get_price_code(self):
        return self._price.get_price_code()

    def set_price_code(self, arg):        
        
        if arg == self.REGULAR:
            return RegularPrice()
        elif arg == self.CHILDRENS:
            return ChildrensPrice()
        elif arg == self.NEW_RELEASE:
            return NewReleasePrice()
        else:
            return None
            # raise Exception("Incorrect price code")
        

    def get_title(self):
        return self._title
    
    def get_charge(self, days_rented):        
        return self._price.get_charge(days_rented)
    
    def get_frequent_renter_points(self, days_rented):

        return self._price.get_frequent_renter_points(days_rented)

        # if self.get_price_code() == self.NEW_RELEASE and days_rented > 1:
        #     return 2
        # else:
        #     return 1

    

movie = Movie("my movie", 2)

print(movie._price)