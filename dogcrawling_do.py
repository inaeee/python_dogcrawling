import requests
import time
import urllib
import argparse
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
from multiprocessing import Pool
from lxml.html import fromstring
import os, sys

#text = 'chowchowbaby'
#url='https://www.google.co.kr/search?q=' + text + '&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiF2fPLn7zdAhUBEbwKHSLWBowQ_AUICigB&biw=809&bih=868&dpr=1.13'

def search(url):
    #Create a browser
    browser=webdriver.Chrome(executable_path='C:\\Users\\inaee\\Downloads\\chromedriver_win32\\chromedriver.exe')

    #Open the link
    browser.get(url)
    time.sleep(1)

    element=browser.find_element_by_tag_name("body")

    #Scroll down
    for i in range(30):
        element.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)

    browser.find_element_by_id("smb").click()

    for i in range(50):
        element.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)

    time.sleep(1)

    #Get page source and close the browser
    source=browser.page_source
    browser.close()

    return source


def download_image(link):
    # Use a random user agent header
    headers = {"User-Agent": ua.random}

    # Get the image link
    try:
        r = requests.get("https://www.google.com" + link.get("href"), headers=headers)
    except:
        print("Cannot get link.")
    title = str(fromstring(r.content).findtext(".//title"))
    link = title.split(" ")[-1]

    # Download the image
    print("At : " + os.getcwd() + ", Downloading from " + link)
    try:
        if link.split(".")[-1] == ('jpg' or 'png' or 'jpeg'):

            urllib.request.urlretrieve(link, link.split("/")[-1])
    except:
        pass


if __name__ == "__main__":
    # parse command line options

    parser = argparse.ArgumentParser()
    parser.add_argument("keyword", help="the keyword to search")
    args = parser.parse_args()

    # set stack limit
    sys.setrecursionlimit(100000000)

    # get user input and search on google
    query = args.keyword


    #query = input("Enter the name you want to search")



    url = "https://www.google.com/search?as_st=y&tbm=isch&as_q=" + query + \
              "&as_epq=&as_oq=&as_eq=&cr=&as_sitesearch=&safe=images&tbs=isz:lt,islt:svga,itp:photo,ift:jpg"
    source = search(url)

    # Parse the page source and download pics
    soup = BeautifulSoup(str(source), "html.parser")
    ua = UserAgent()

    # check directory and create if necessary
    if not os.path.isdir(args.keyword):
        os.makedirs(args.keyword)

    os.chdir(str(os.getcwd()) + "/" + str(args.keyword))
    # get the links
    links = soup.find_all("a", class_="rg_l")

    # open some processes to download
    with Pool() as pool:
        pool.map(download_image, links)
    





# 검색어
#search = 'chowchowbaby'
#url='https://www.google.co.kr/search?q=' + search + '&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiF2fPLn7zdAhUBEbwKHSLWBowQ_AUICigB&biw=809&bih=868&dpr=1.13'
# url
#driver = webdriver.Chrome(executable_path="C:\\Users\\inaee\\Downloads\\chromedriver_win32\\chromedriver.exe")
#driver.get(url)
#driver.implicitly_wait(2)


#num_of_pagedowns = 50
#elem = driver.find_element_by_xpath('/html/body') 

#i = 0
#count = 1
#img = driver.find_elements_by_tag_name("img")

#while i < num_of_pagedowns:
#for item in img:
#    if(count>0 and count<502):
#            elem.send_keys(Keys.DOWN)
#            time.sleep(1)
#        full_name = "C:\\Program Files\\Python35\\강아지크롤러\\chowchowbaby\\" + str(count) + "_chowchowbaby.jpg"
#        try:
#            urllib.request.urlretrieve(item.get_attribute('src'), full_name)
#            tfp=open(full_name,url)
#            print(item.get_attribute('src')[:30] + " : ")
#        except:
#            urllib.request.urlretrieve(item.get_attribute('data-src'), full_name)
#            tfp=open(full_name,url)
#            print(item.get_attribute('data-src')[:30] + " : ")
#    count = count+1
#    i =i+1

    
#driver.Quit()
#print("Done.")
