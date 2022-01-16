'''
TODO webcrawl over blogs by handling pagination to extract data from all pages
    open <span class="page"> that has an anchor tag with an href attribute that can be appended to the end of the url
'''
import requests # handle http requests
from bs4 import BeautifulSoup # html extraction
from csv import writer # write data to file with csv module as a list

# inspect html structure of website with google dev tools
url = "https://www.rithmschool.com/blog"
csv_file_name = "blog_data.csv"
# scrape data by making a html request
response = requests.get(url)

# instantiate new instance
soup = BeautifulSoup(response.text, "html.parser")

# find & get a list of all article html objects
articles = soup.find_all("article")

# write URL, anchor tag text, and date data to a csv file
with open(csv_file_name, "w") as file:
    csv_writer = writer(file)
    # write header row
    csv_writer.writerow(["title", "link", "date"])

    # grab all links from https://www.rithmschool.com/blog
    for article in articles:
        # find & get a list of all anchor html objects
        anchors = article.find("a")
        date = article.find("time")["datetime"]
        title = anchors.get_text()
        url = anchors["href"]

        # while csv is still open and after having looped through elements, write row with data into csv file
        csv_writer.writerow([title, url, date])

