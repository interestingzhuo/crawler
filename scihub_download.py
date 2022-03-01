from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from scidownl.scihub import *
import pdb
import pandas as pd
import os
import time
def run(title,out):
    '''
    download pdf from sci-hub
    '''
    
    driver.get('https://www.cnki.net/')
    
    print("title: {0}".format(title))
    input_element = driver.find_element_by_id("txt\_SearchText")
    input_element.clear()
    input_element.send_keys(title)
    input_element.send_keys(Keys.ENTER)
    time.sleep(5)
    download = driver.find_element_by_class_name('operat')
    href = download.find_element_by_tag_name('a').get_attribute('href')
    print('href:',href)
    driver.get(href)
    
    '''
    driver.get('http://www.sci-hub.ren/')
    
    print("title: {0}".format(title))
    input_element = driver.find_element_by_name("request")
    input_element.clear()
    input_element.send_keys(title)
    input_element.send_keys(Keys.ENTER)
    url = driver.current_url
    
    
    url = url.split('st')[-1][1:]
    print('url:',url)
    SciHub(url, out).download(choose_scihub_url_index=3)
    '''

    

if __name__ == '__main__':
    driver = webdriver.Chrome()
    folder = 'D:\\Download\\liudan\\GoogleScholarCrawler-master\\中文'
    for keyword in os.listdir(folder):
        file_name = os.path.join(folder,keyword)
        print("file name: ",file_name)
        data = pd.read_excel(file_name, sheet_name = 1)
        titles = [data['title'][i] for i in range(1,len(data['title'])+1)]
        for title in titles:
            try:
                run(title,None)
            except:
                continue;
            
    driver.quit()