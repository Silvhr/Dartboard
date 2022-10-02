import requests
from bs4 import BeautifulSoup
import random


# def keywordFixer(keyword):
#     ''' Takes a keyword and replaces spaces with underscores '''


#     keyword_list = keyword.split(" ")
#     new_keyword = ""

#     for i in range(len(keyword_list)):

#         # print(keyword_list[i][0]) ## The first char in each word
#         # print(keyword_list[i][1:]) ## The rest of the word


#         first_char = keyword_list[i][0]
#         rest_of_word = keyword_list[i][1:]
#         new_keyword += first_char.upper() + rest_of_word

#         if (i < len(keyword_list) - 1):
#             new_keyword += "_"


#     return new_keyword


def keywordFixer(keyword):
    ''' Takes a keyword and replaces spaces with underscores '''

    keyword_list = keyword.split(" ")
    new_keyword = ""

    for i in range(len(keyword_list)):

        # print(keyword_list[i][0]) ## The first char in each word
        # print(keyword_list[i][1:]) ## The rest of the word

        first_char = keyword_list[i][0]
        rest_of_word = keyword_list[i][1:]
        new_keyword += first_char.upper() + rest_of_word

        if (i < len(keyword_list) - 1):
            new_keyword += "_"

    return new_keyword


# city = input("Enter a city: ")
# state = input("Enter a state: ")
# print(keywordFixer(city, state))


def wikiVoyage(city):
    ''' scrapes wikiVoyage for a banner, and a summary '''

    keyword = keywordFixer(city)

    URL = "https://en.wikivoyage.org/wiki/" + keyword
    r = requests.get(URL)

    soup = BeautifulSoup(r.content, "html.parser")
    search = soup.find_all('p')
    text = search[1].get_text()

    if "There is more than one place called" in text:
        state = str(input("Please choose a state: "))
        state = "_(" + state + ")"
        keyword += state

        URL = "https://en.wikivoyage.org/wiki/" + keyword
        r = requests.get(URL)

        soup = BeautifulSoup(r.content, 'lxml')
        search = soup.find_all('p')
        text = search[1].get_text()

    search = soup.find_all('img')

    image_src = search[2]["src"]

    output = text + image_src

    file = open("summary","w")
    file.write(output)
def randomCity():
    file = open("City_Data.txt", "r")
    file_text = file.read()
    file_split = file_text.split("\n")
    r = random.randint(0, 199)
    random_city = file_split[r]
    random_city_split = random_city.split(",")
    city = random_city_split[1]
    state = random_city_split[2]
    return city
# city = input("Enter a city: ")
if __name__ == "__main__":
    wikiVoyage(randomCity())


