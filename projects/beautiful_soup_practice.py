from bs4 import BeautifulSoup

html = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
'''

# parse (must be html.parser, and not xml.parser)
soup = BeautifulSoup(html, 'html.parser')
# print(soup.body)

# find and return all elements that has attribute data-example that is set to yes as an dictionary
# attrs = soup.find('div').attrs
# attrs = soup.find('div')['id']
# print(attrs)

# data = soup.find_all(attrs={'data-example': 'yes'})
# print(data)

# select elements with css
# data = soup.select('#first')
# data = soup.select('.special')
# data = soup.select('[data-example]')

# for el in data:
#     print(el.name)

# to access nested elements

# data = soup.body.contents[1].next_sibling.next_sibling
# data = soup.find(class_='special').parent.parent

data = soup.find('h3').find_parent('html')

# you can chain these commands together
# data = soup.find(id='first').find_next_sibling()
# data = soup.find(id='first').find_next_sibling().find_next_sibling()

# data = soup.find(id='first').find_previous_sibling()
# data = soup.find(id='first').find_previous_siblings()

print(data)

