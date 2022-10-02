import requests
from bs4 import BeautifulSoup
import cchardet

URL = "https://www.biggestuscities.com/1"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'lxml')

search = soup.find_all('tr')



for i in range(1,101):
    
    
    print("\n")
    print("-" * 30)
    
    entry = search[i]
    city_text = entry.get_text()
    
    
    city_data = city_text.split("\n")
    
    city_data = list(filter(None, city_data))
    
    
    Rank = city_data[0]
    Location = city_data[1]
    
    Location = Location.split(",")
    City = Location[0]
    State = Location[1]
    
    
    
    Pop = city_data[2]
    Pop = Pop.replace(" ", "")
    
    try:
        Growth = city_data[4]
        Growth = Growth.replace(" ", "")
    except:
        Growth = "N/A"
    
    
    
    print(Rank, City, State, Pop, Growth)
