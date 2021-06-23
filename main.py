import requests, re
from bs4 import BeautifulSoup
import sys

def get_data(soup, url):
    """
    Takes as input a beautiful soup object and returns a tuple. All values are strings.
    Tuple format: (Length, Elevation Gain, Highest Point, Location, Rating out of 5, url)"""

    try:
        stats = soup.find_all("div", class_="hike-stat")

        location = stats[0].find("div").get_text().split(", ")[0]

        length = stats[1].find("div", id="distance").find("span").get_text().split(", ")[0]

        height = stats[2].find_all("div")
        elev_gain = height[0].find("span").get_text() + " ft."
        highest = height[1].find("span").get_text() + " ft."

        rating = soup.find("div", class_="current-rating").get_text().split(" out of ")[0]

        print((length, elev_gain, highest, location, rating))
        return	(length, elev_gain, highest, location, rating, url)
    
    except IndexError:
        return None

def extract_datas(urls):
    """
    Extracts the data from each url in the given list of urls.
    Returns a list of tuples containing the data.
    Tuple format: (Length, Elevation Gain, Highest Point, Location, Rating out of 5, url)"""

    texts = []
    for url in urls:
        print(url)
        texts.append((requests.get(url).text, url))

    
    return [get_data(BeautifulSoup(text, "html.parser"), url) for text, url in texts]


def assemble_csv(datas):
    """
    Takes a list of tuples in the formpat provided by get_data.
    Returns a string containing the csv."""

    string = "Length,Elevation Gain,Highest Point,Location,Rating\n"

    string += "\n".join([",".join(data) for data in datas if data is not None])

    return string


if __name__ == "__main__":
    
    urls = ""
    with open("urls.txt", "r") as f:
        urls = f.readlines()
        urls = list([url.strip() for url in urls])

    datas = extract_datas(urls)
    csv =  assemble_csv(datas)

    with open("out.csv", "w") as f:
        f.write(csv)
        

