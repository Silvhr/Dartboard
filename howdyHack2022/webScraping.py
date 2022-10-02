#from bs4 import BeautifulSoup
#import requests
import time
import json
#import sys
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#import csv
from summary import wikiVoyage,randomCity

def thingstodo(city=""):

    #chrom driver path in your computer
    chromePath = Service("/Users/aboodhb_/Documents/PycharmProjects/howdyHack2022/chromedriver")
    try :
        url = "https://www.tripadvisor.com/Search?q=" + city + "&searchSessione&sid=59ADC4D2AB939D2613ABD3C3DA9ED0C51664661938160&blockRedirect=true&ssrc=A&rf=1"
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        driver = webdriver.Chrome(service=chromePath,options=option)
        driver.get(url)
        time.sleep(2)
        container = driver.find_element(By.XPATH, "//div[@class='ui_columns is-multiline is-mobile']")
        container_img = driver.find_element(By.XPATH, "//div[@class='ui_columns is-multiline is-mobile']")
        all = open("all", "w")
        allimgs = open("allImg","w")
        #all.write("City: "+city+"\n")
        all.write(container.text)
        allimgs.write(container_img.get_attribute('innerHTML'))
        all.close()
        allimgs.close()
        driver.quit()

        '''def cleandata(file):
            all = open(file, "r")
            clean = open("Activities", "w")
            allimgs = open("allImg", "r")
            list = []

            allimgs = allimgs.read().split("\"")
            imgsNot = []
            for i in allimgs:
                if "background-image:url(" in i:
                    imgsNot.append(i[21:len(i)-2])
            i=0
            imgs = []
            while i < len(imgsNot)/3:
                imgs.append(imgsNot[i])
                i+=3
            for i in all:
                list.append(i)
            i = 2
            j = 0
            while i < len(list) and i < 48 and j < 8:
                # place
                clean.write(list[i])
                i += 1
                # address
                clean.write(list[i])
                clean.write(imgs[j] + "\n")
                j += 1
                i += 4
                clean.write("\n")

            all.close()
            clean.close()'''
        def cleandata(file):
            all = open(file, "r")
            clean = open("Activities", "w")
            allimgs = open("allImg", "r")
            list = []
            for i in all:
                list.append(i)
            allimgs = allimgs.read().split("\"")
            imgsNot = []
            for i in allimgs:
                if "background-image:url(" in i:
                    imgsNot.append(i[21:len(i)-2])
            i=0
            imgs = []
            while i < len(imgsNot)/3:
                imgs.append(imgsNot[i])
                i+=3

            i = 1
            j = 0
            while i < len(list) and i < 48:
                # place
                clean.write(list[i])
                i += 2
                # address
                clean.write(list[i])
                clean.write(imgs[j] + "\n")
                j += 1
                i += 4

            all.close()
            clean.close()
        cleandata("all")
    except :
        print("ERROR")


def hotels(city=""):

    #chrom driver path in your computer
    chromePath = Service("/Users/aboodhb_/Documents/PycharmProjects/howdyHack2022/chromedriver")
    try :
        url = "https://www.tripadvisor.com/Search?q=" + city + "&searchSessionId=EA3EC871B81767CBB385D67F3A24C3641664672549088ssid&searchNearby=false&sid=2EE8D5DDC9F148F6BC624B5C7B575CC11664672559515&blockRedirect=true&ssrc=h&rf=3"
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        driver = webdriver.Chrome(service=chromePath,options=option)
        driver.get(url)
        time.sleep(2)
        container = driver.find_element(By.XPATH, "//div[@class='ui_columns is-multiline is-mobile']")
        container_img = driver.find_element(By.XPATH, "//div[@class='ui_columns is-multiline is-mobile']")
        all = open("all", "w+")
        allimgs = open("allImg", "w")
        #all.write("City: "+city+"\n")
        all.write(container.text)
        allimgs.write(container_img.get_attribute('innerHTML'))
        all.close()
        allimgs.close()
        driver.quit()

        def cleandata(file):
            all = open(file, "r")
            clean = open("Hotels", "w")
            allimgs = open("allImg", "r")
            list = []
            for i in all:
                list.append(i)
            allimgs = allimgs.read().split("\"")
            imgsNot = []
            for i in allimgs:
                if "background-image:url(" in i:
                    imgsNot.append(i[21:len(i)-2])
            i=0
            imgs = []
            while i < len(imgsNot)/3:
                imgs.append(imgsNot[i])
                i+=3

            i = 1
            j = 0
            while i < len(list) and i < 48:
                # place
                clean.write(list[i])
                i += 2
                # address
                clean.write(list[i])
                clean.write(imgs[j] + "\n")
                j += 1
                i += 4

            all.close()
            clean.close()
        cleandata("all")
    except :
        print("ERROR")

    # By.CLASS_NAME this is working for class
    # "name" this is working for name
    # By.xpath

def toJson(file):
    txt = open(file,"r")
    list = txt.read()
    list = list.split("\n")
    i=0
    dictionary = {"Item":[],"Address":[],"Img":[]}
    while i < len(list):
        if i != len(list)-4:
            dictionary["Item"].append(list[i])
            dictionary["Address"].append(list[i+1])
            dictionary["Img"].append(list[i+2])
            i+=3
        if i == len(list) -4:
            dictionary["Item"].append(list[i])
            dictionary["Address"].append(list[i + 1])
            dictionary["Img"].append(list[i + 2])
            break

    json_object = json.dumps(dictionary, indent=3)
    with open(file +".json", "w") as outfile:
        outfile.write(json_object)
def toJson_sum(file):
    txt = open(file,"r")
    list = txt.read()
    list = list.split("\n")

    dictionary = {"Summary":list[0],"Img":list[1]}

    json_object = json.dumps(dictionary, indent=3)
    with open(file +".json", "w") as outfile:
        outfile.write(json_object)

if __name__ == "__main__":
    city = randomCity()
    thingstodo(city)
    hotels(city)
    wikiVoyage(city)
    toJson("Hotels")
    toJson("Activities")
    toJson_sum("summary")


