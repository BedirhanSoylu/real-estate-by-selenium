# -*- coding: utf-8 -*-
# *** Spyder Python Console History Log ***
import pandas as pd
import numpy as np
from msedge.selenium_tools import Edge, EdgeOptions

#DataFrame oluşturma
column = ['Link','Il','Semt','Yakıt','Durum','KM','Renk','Garanti','Hasar Kaydı','Fiyat']
df = pd.DataFrame(columns= column)
options = EdgeOptions()
options.use_chromium = True
driver = Edge(r'C:\Users\Bedirhan\Desktop', options= options)

options = ChromeOptions()
driver = webdriver.Chrome(options=options)

#Daire linklerini cekme
f = open('C:\\Users\Bedirhan\Desktop\Dump\samsunfiyatdaire.txt','r')
sntcs = f.read()
lnk = sntcs.split('\n')
for query in lnk:
    driver.get(query)
    price= driver.find_element_by_xpath('/html/body/div[5]/div[4]/div[1]/div/div[2]/div[2]/h3').text
    price = np.array([price[0]+price[2:4]+price[6:8]])
    price = int(price)
    print(price)
    
    il = driver.find_element_by_xpath('//*[@id="classifiedDetail"]/div/div[2]/div[2]/h2/a[1]').text
    semt = driver.find_element_by_xpath('//*[@id="classifiedDetail"]/div/div[2]/div[2]/h2/a[2]').text
    yakit = driver.find_element_by_xpath('//*[@id="classifiedDetail"]/div/div[2]/div[2]/ul/li[7]/span').text
    durum = driver.find_element_by_xpath('//*[@id="classifiedDetail"]/div/div[2]/div[2]/ul/li[9]/span').text
    km = int(driver.find_element_by_xpath('//*[@id="classifiedDetail"]/div/div[2]/div[2]/ul/li[10]/span').text)
    renk = driver.find_element_by_xpath('//*[@id="classifiedDetail"]/div/div[2]/div[2]/ul/li[16]/span').text
    garanti =driver.find_element_by_xpath('//*[@id="classifiedDetail"]/div/div[2]/div[2]/ul/li[17]/span').text
    hasar = driver.find_element_by_xpath('//*[@id="classifiedDetail"]/div/div[2]/div[2]/ul/li[18]/span').text
    
    
    
    feature = np.array([query,il,semt,yakit,durum,km,renk,garanti,hasar,fiyat])
    added_df = pd.DataFrame(feature,columns=column)
    df = pd.concat([df,added_df])

driver.quit()

