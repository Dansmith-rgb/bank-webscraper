from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import csv
from plotly.graph_objs import Bar
from plotly import offline
import numpy as np

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
num = []
name = []
list1 = []
list2 = []

def lloydsbank(num, name):
    driver.get("https://www.lloydsbank.com/savings.html?wt.ac=products/navigation/savings")
    print(driver.title)
    count = 0
    #num = []
    #name = []

    try:
        driver.implicitly_wait(5)
        main = driver.find_element_by_tag_name("tbody")

        interest = main.find_elements_by_tag_name("tr")

        td_count = 0

        for tr in interest:
            coloumns = tr.find_elements_by_tag_name("td")
            for td in coloumns:
                td_count += 1
                try:
                    coloumnss = td.find_element_by_tag_name("div")
                    deep = coloumnss.find_element_by_tag_name("h4")
                    count2 = 0
                    count += 1
                    with open("banks.csv", mode="a") as b:
                        f = csv.writer(b, delimiter=',')
                        f.writerow([deep.text])
                    if count % 2 == 0:
                        num.append(deep.text)
                        print(num)
                    if count % 2 == 1 or 0:
                        name.append(deep.text)
                        print(name)
                except:
                    coloumns2 = td.find_element_by_tag_name("div")
                    deep2 = coloumns2.find_element_by_tag_name("p")
                    with open("banks.csv", mode="a") as b:
                        f = csv.writer(b, delimiter=',')
                        f.writerow([deep2.text])
                        count += 1
                        if count % 2 == 0:
                            num.append(deep2.text)
                            print(num)
                        if count % 2 == 1 or 0:
                            name.append(deep2.text)
                            print(name)
                
                if td_count == 2:
                    td_count = 0
                    break
            #print(coloumns.text)
    except Exception as e:
        print(str(e))
        driver.quit()

#n = np.array(name)

#make_dict

        

#num.sort()
#print(num)
def graph_data(name, num):
    #printn)
    data = [{
        'type': 'bar',
        'x': list1,
        'y': list2,
    }]

    my_layout = {
        'title': 'Banks',
        'xaxis': {'title': 'Accounts'},
        'yaxis': {'title': 'Interest rates'}
    }

    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename='banks_graphs.html')

lloydsbank(name, num)
m = name.index(max(name))
print(m)
print(num[m])
list1.append(num[m])
list2.append(name[m])
graph_data(name, num)
