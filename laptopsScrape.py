
import requests, csv
from bs4 import BeautifulSoup

headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',}

# Doing a get request on the url
res = requests.get("https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops", headers=headers)

# Converting into a beautifulSoup object
soup = BeautifulSoup(res.content, 'html5lib')

# Column Headers for the CSV File
columns = ["Product Name", "Product Price", "Rating", "Reviews Count"]
# Initialising Rows List for the CSV File
rows = []

# Find all the divs that contain laptop details
laptopDivList = soup.find_all("div", attrs={"class":"col-sm-4 col-lg-4 col-md-4"})

for laptopDiv in laptopDivList:

    # Getting the ratings and no of reviews <p>
    RatingReview = laptopDiv.find("div", attrs={"class": "ratings"}).find_all("p")

    # Temperory list that will be inserted as a row in "Rows"
    # Product Name - From <a> tag with title attribute
    # Product Price - First <h4> tag and then getting text from text property
    # Rating - Using the List "RatingReview" at 1 index which gives <p> with attribute "data-rating" that contains rating
    # No of Reviews - Using the List "RatingReview" at 0 index and then splitting the text property with space and using the Review Count at 0 index
    details = [laptopDiv.a["title"], laptopDiv.h4.text, RatingReview[1]["data-rating"], RatingReview[0].text.split(" ")[0]]

    # Append Details list to Rows
    rows.append(details)

# Opening the csv file with 'W' mode
with open('./laptops.csv', 'w', encoding='UTF8', newline='') as laptopCSV:
    
    # Creating a csv writer
    writer = csv.writer(laptopCSV)

    # Writing the header row
    writer.writerow(columns)
    # Writing the rest of rows
    writer.writerows(rows) 



