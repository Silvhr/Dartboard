import requests
from bs4 import BeautifulSoup
import cchardet

URL = "https://www.biggestuscities.com/2"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'lxml')

search = soup.find_all('tr')

file = open("City_Data.txt", 'a')


for i in range(1,101):
    
    
    print("\n")
    print("-" * 30)
    
    entry = search[i]
    city_text = entry.get_text()
    
    
    city_data = city_text.split("\n")
    
    city_data = list(filter(None, city_data))
    
    
    Rank = str(city_data[0])
    Location = city_data[1]
    
    Location = Location.split(",")
    City = str(Location[0])
    State = str(Location[1])
    
    
    
    Pop = city_data[2]
    Pop = Pop.replace(" ", "")
    
    try:
        Growth = str(city_data[4])
        Growth = Growth.replace(" ", "")
    except:
        Growth = "N/A"
    
    
    
    print(Rank, City, State, Pop, Growth)
    
    row = Rank + "," + City + "," + State + "," + Pop + "," + Growth + "," + "\n"    
    file.write(row)


file.close()