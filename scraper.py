# Importing all the modules
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


# Defining the lists and the chrome driver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
num = []
name = []
list1 = []
list2 = []

def lloydsbank(num, name):
    # Getting the url to scrape from.
    driver.get("https://www.lloydsbank.com/savings.html?wt.ac=products/navigation/savings")
    print(driver.title)
    count = 0
    

    try:
        # Telling the driver to wait for 5 seconds
        driver.implicitly_wait(5)
        # Getting elements
        main = driver.find_element_by_tag_name("tbody")

        interest = main.find_elements_by_tag_name("tr")

        td_count = 0

        for tr in interest:
            coloumns = tr.find_elements_by_tag_name("td")
            for td in coloumns:
                td_count += 1
                # Used try and except because to get the percentage and name they are in different elements
                try:
                    coloumnss = td.find_element_by_tag_name("div")
                    deep = coloumnss.find_element_by_tag_name("h4")
                    count2 = 0
                    count += 1
                    # Write it to a csv file
                    with open("banks.csv", mode="a") as b:
                        f = csv.writer(b, delimiter=',')
                        f.writerow([deep.text])
                    # Printing out every other life
                    if count % 2 == 0:
                        num.append(deep.text)
                        print(num)
                    if count % 2 == 1 or 0:
                        name.append(deep.text)
                        print(name)
                except:
                    coloumns2 = td.find_element_by_tag_name("div")
                    deep2 = coloumns2.find_element_by_tag_name("p")
                    count += 1
                    # Write to a csv file
                    with open("banks.csv", mode="a") as b:
                        f = csv.writer(b, delimiter=',')
                        f.writerow([deep2.text])
                        
                    # Printing out every other line
                    if count % 2 == 0:
                        num.append(deep2.text)
                        print(num)
                    if count % 2 == 1 or 0:
                        name.append(deep2.text)
                        print(name)
                
                if td_count == 2:
                    td_count = 0
                    break
    except Exception as e:
        print(str(e))
        driver.quit()


def graph_data(name, num):
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
# Calling function
lloydsbank(name, num)
# Getting the max number to plot on the graph but also keeping the right name with it.
m = name.index(max(name))
print(m)
print(num[m])
list1.append(num[m])
list2.append(name[m])
# Calling function
graph_data(name, num)
