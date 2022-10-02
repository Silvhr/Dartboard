import requests
from bs4 import BeautifulSoup

# URL = "https://wikitravel.org/en/Austin"

# r = requests.get(URL)

# soup = BeautifulSoup(r.content, 'html.parser')


# search = soup.find_all('p')

# i = 0
# # for a in search:
# #     print(search[i])
# #     print('\n')
# #     i += 1


# print(search[2].get_text())




def summary(keyword):
    
    if " " in keyword:
        keyword_list = keyword.split(" ")
        keyword = keyword_list[0] + "_" + keyword_list[1]
            
    
    URL = "https://wikitravel.org/en/" + keyword
    r = requests.get(URL)
    
    soup = BeautifulSoup(r.content, 'html.parser')
    search = soup.find_all('p')
    text = search[2].get_text()
    
    return text
    
city = input("Enter a city: ")
print(summary(city))