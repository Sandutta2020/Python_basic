url ='https://www.rottentomatoes.com/m/house_of_darkness_2022/reviews/?page=1'
import requests
from bs4 import BeautifulSoup as soup
response = requests.request("GET", url=url)
page_soup = soup(response.content, "lxml")
rows = page_soup.find_all("div", {"class": "row review_table_row"})
for row in rows:
    outrow = []
    user = row.find("div", {"class": "col-sm-17 col-xs-32 critic_name"})
    outrow.append(user.find('a', href=True)['href'])
    name = str(user.find({"a"}).contents[0])
    print(name)
    starRating = row.find("div", {"class": "the_review"}).text
    print(starRating.strip())
