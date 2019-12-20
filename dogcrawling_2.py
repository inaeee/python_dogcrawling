import requests
import urllib.request
import random
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import os


def make_folder(folder_name):
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)


# 검색어
search = 'Sapsaree adult'
# url
driver = webdriver.Chrome(executable_path="C:\\Users\\inaee\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get('https://www.google.co.kr/search?q=' + search + '&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiM5YDD75LZAhUEtpQKHaF3DM0Q_AUIDCgD&biw=767&bih=740')
driver.implicitly_wait(2)


root_dir = "C:\\강아지크롤러"
work_dir = root_dir + "\\" + search
make_folder(work_dir)

elem = driver.find_element_by_xpath('/html/body')


#1 선 스크롤 1
for i in range(0,50):
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.1)

#결과 더보기 클릭
driver.find_element_by_xpath('//*[@id="smbw"]').click()

#1 선 스크롤 2
for i in range(0,50):
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.1)


count = 0
img = driver.find_elements_by_tag_name("img")

for item in img:
    if(count < 502):
        full_name = work_dir + "\\" + str(count-1) + "_Sapsareeadult.jpg"
        try:
            urllib.request.urlretrieve(item.get_attribute('src'), full_name)
            print(item.get_attribute('src')[:30] + " : ")
        except:
            try:
                urllib.request.urlretrieve(item.get_attribute('data-src'), full_name)
                print(item.get_attribute('data-src')[:30] + " : ")
            except:
                print("둘 다 오류..")
        print("{0}. Saving : {1}".format(count,full_name))
        count = count+1


    
driver.Quit()
print("Saved!")
