
# import unittest module and functionality you want to test
import unittest
from quotes_to_scrape import get_all_quotes, get_random_quote, get_author_details

class QuotesTests(unittest.TestCase):

    def setUp(self):
        self.random_quote_1 = get_random_quote()
        self.random_quote_2 = get_random_quote()

    def test_get_all_quotes(self):
        '''
        make a request to get all quotes from paginated pages
        '''
        self.assertTrue(
                len(get_all_quotes()) == 100
            )

    def test_get_random_quote(self):
        '''
        get 2 separate random quotes and check that they don't equal each other
        '''
        self.assertTrue(
            get_random_quote() != get_random_quote()
        )

    def test_get_author_details(self):
        '''
        get author's href bio
        '''
        self.assertTrue(
            get_author_details(self.random_quote_1)
        )

# run unit tests
if __name__ == "__main__":
    unittest.main()