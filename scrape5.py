import requests
from bs4 import BeautifulSoup
import os
import cchardet









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



# keyword = input("Enter a keyword: ")
# print(keywordFixer(keyword))
    



def summary(keyword):
    
    keyword = keywordFixer(keyword)
    
    URL = "https://en.wikivoyage.org/wiki/" + keyword
    r = requests.get(URL)
    
    soup = BeautifulSoup(r.content, 'lxml')
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
        
    
    return text
    


def banner(keyword):
    
    keyword = keywordFixer(keyword)
    
    URL = "https://en.wikivoyage.org/wiki/" + keyword
    r = requests.get(URL)
    
    soup = BeautifulSoup(r.text, 'lxml')
    search = soup.find_all('img')
        
    image_src = search[2]["src"]
    

    
    return image_src
    

city = input("Enter a city: ")


print("\n")
print(summary(city))
print("\n")
print(banner(city))

