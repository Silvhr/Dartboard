import requests
from bs4 import BeautifulSoup
import os
import cchardet









def keywordFixer(keyword):
    ''' Takes a keyword and replaces spaces with underscores '''
    
    new_keyword = keyword
    
    if " " in keyword:
        keyword_list = keyword.split(" ")
        new_keyword = ""
        for i in range(len(keyword_list) - 1):
            new_keyword += keyword_list[i] + "_"
        new_keyword += keyword_list[-1]
        
        
        
        
    ####### Fix capitalization here #######    
    
    
        
    
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
    
    keyword= keywordFixer(keyword)
    
    URL = "https://en.wikivoyage.org/wiki/" + keyword
    r = requests.get(URL)
    
    soup = BeautifulSoup(r.text, 'lxml')
    search = soup.find_all('img')

        
    image_src = search[2]["src"]
    
    return image_src
    

city = input("Enter a city: ")
print(banner(city))


