import unittest
from movie import Movie
from rental import Rental
from customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        # Create some test movies and rentals
        self.movie_regular = Movie("Regular Movie", Movie.REGULAR)
        self.movie_new_release = Movie("New Release Movie", Movie.NEW_RELEASE)
        self.movie_childrens = Movie("Children's Movie", Movie.CHILDRENS)
        self.rental1 = Rental(self.movie_regular, 3)
        self.rental2 = Rental(self.movie_new_release, 2)
        self.rental3 = Rental(self.movie_childrens, 4)
        self.customer = Customer("Test Customer")

    def test_add_rental(self):
        # Check if rentals are added correctly
        self.customer.add_rental(self.rental1)
        self.customer.add_rental(self.rental2)
        self.assertEqual(len(self.customer._rentals), 2)

    def test_statement(self):
        # Add rentals to the customer
        self.customer.add_rental(self.rental1)
        self.customer.add_rental(self.rental2)
        self.customer.add_rental(self.rental3)

        # Calculate the expected result
        expected_result = "Rental Record for Test Customer\n"
        expected_result += "\tRegular Movie\t3.5\n"
        expected_result += "\tNew Release Movie\t6\n"
        expected_result += "\tChildren's Movie\t3.0\n"
        expected_result += "Amount owed is 12.5\n"
        expected_result += "You earned 4 frequent renter points"

        # expected_html_result = "<p><h1>Rental Record for <em>Test Customer</em></h1></p>\n"        
        # expected_html_result = "\tRegular Movie\t3.5<br>\n"
        # expected_html_result = "\tNew Release Movie\t6<br>\n"
        # expected_html_result = "\tChildren's Movie\t3.0<br>\n"
        # expected_html_result = "<p>Amount owed is<em> 12.5</em>  <p>\n"
        # expected_html_result = "On this rental You earned <em> 4 frequent renter points</p>"

        
        # Check if the statement method produces the correct result
        self.assertEqual(self.customer.statement(), expected_result)
        # self.assertEqual(self.customer.html_statement(), expected_html_result)
        

if __name__ == '__main__':
    unittest.main()
