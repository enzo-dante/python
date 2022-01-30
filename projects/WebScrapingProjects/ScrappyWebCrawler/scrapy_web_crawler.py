# target website to scrape with easy-to-use scrapy web crawler
    # http://books.toscrape.com/

# to execute scrapy project
    # scrapy runspider -0 {new_file_name.json or new_file_name.csv} {file_name.py}

# python3 -m pip install scrapy
import scrapy

# spiders are classes which define how a certain site will be scraped 
class BookSider(scrapy.Spider):
    name = "bookspider"
    # scrapy will handle get requests with 'start_urls'
    start_urls = ["http://books.toscrape.com/"]

    # scrapy will search for parse the result of start_urls request
    # inspect html structure and access with response.css(html_tag)
    def parse(self, response):
        for article in response.css("article.product_pod"):

            # need to yield to continue instead of return
            yield {
                "price": article.css(".price_color::text").extract_first(),
                "title": article.css("h3 > a::attr(title)").extract_first()
            }

            # use recursion to call parse again to handle pagination
            next = response.css(".next > a::attr(href)").extract_first()
            if next:
                yield response.follow(next, self.parse)
        