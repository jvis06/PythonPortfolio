from bs4 import BeautifulSoup
import requests
import gspread
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from pathlib import Path
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pwinput









def Scrape():
    global row, count, label

    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    pull = soup.find_all('a', class_="splitview-issue-link")



    for i in pull:
        count = count + 1
        ticket = i.find("span", class_="issue-link-key").text.strip()
        ticketfull = #removed for confidentiality
        wks.update_cell(row, 1, ticketfull)
        summ = i.find("span", class_="issue-link-summary").text
        wks.update_cell(row, 4, summ)
        driver.get(#URL removed for confidentiality)
        time.sleep(10)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        prio = soup.find('span', id="priority-val").text.strip()
        wks.update_cell(row, 2, prio)
        report = soup.find('span', id="reporter-val").text.strip()
        wks.update_cell(row, 3, report)
        dates = soup.find_all('dl', class_="dates")
        wks.update_cell(row, 5, dates[0].find('dd', class_="user-tz").get('title').strip())
        wks.update_cell(row, 7, dates[1].find('dd', class_="user-tz").get('title').strip())
        # create = soup.find('span', id="create-date").text
        # wks.update_cell(row, 5, create)
        stat = soup.find('span', id="status-val").text.strip()
        wks.update_cell(row, 6, stat)
        # update = soup.find('span', id="updated-date").text.strip()
        # wks.update_cell(row, 7, update)
        assign = soup.find('span', id="assignee-val").text.strip()
        wks.update_cell(row, 8, assign)
        templab = soup.find_all('a', class_="lozenge")
        for k in templab:
            templab2 = k.text
            label.append(templab2)
        lab = ', '.join(label)
        wks.update_cell(row, 9, lab)
        label.clear()

        try:
            lastcom = soup.find_all('div', class_="activity-comment")
            lastcomfin = lastcom[-1].find('div', class_="action-body").text.strip()
            commenter = lastcom[-1].find('a', class_="user-avatar").text.strip()
            fullcom = str(commenter) + " - " + str(lastcomfin)
            wks.update_cell(row, 10, fullcom)
        except:
            lastcomfin = soup.find('div', class_="message-container").text.strip()
            wks.update_cell(row, 10, lastcomfin)

        

            
        

        row = row + 1
    #goods na, continue laters

    try: #check if there are multiple pages
        maxpage = soup.find('div', class_="pagination").get("data-displayable-total")
        if (count != int(maxpage)):
            clicker = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[4]/div/div/div/div/div/div/div/div[1]/div[1]/div/div[4]/div[2]/div/a[2]')
            clicker.click()
            time.sleep(10)
            Scrape()
    except NoSuchElementException:
        print("Max Page is only 1. Not Applicable. Everything is working good bebegurl.")
    except:
        print("All goods")











    


  
def testcred():

    driver.get(URL)

    user = input("\n\nUsername (JIRA): ")
    password = pwinput.pwinput("Password (JIRA): ")
    print("\n\nTesting Login Credentials, please wait..\n\n")

    
    

    try:
        wits = WebDriverWait(driver, 120).until(EC.presence_of_element_located
        ((By.ID, "login-form-username")))
    except TimeoutException:
        print("\n\nPage TimeOut, please check your Internet Connection or TRUSTArc VPN.")
        driver.quit()

    time.sleep(2)


    driver.find_element(By.ID, "login-form-username").send_keys(user)
    driver.find_element(By.ID, "login-form-password").send_keys(password)
    driver.find_element(By.ID, "login-form-submit").click()
    time.sleep(7)

    if driver.current_url != URL3:
        print("\n\nLogin Credentials Incorrect: Please try again.")
        testcred()
    else:
        print("\n\nNays ka wan! Starting, please be patient sharewt..")

    driver.get(URL2)

    try:
        wits = WebDriverWait(driver, 120).until(EC.presence_of_element_located
        ((By.ID, "layout-switcher-button")))
    except TimeoutException:
        print("\n\nPage TimeOut, please check your Internet Connection or TRUSTArc VPN.")
        driver.quit()
        

    time.sleep(3)
    driver.find_element(By.ID, "layout-switcher-button").click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//a[@data-layout-key="split-view"]').click()
    time.sleep(2)



    print("\n\nUpdating the files from Gsheet..")


    Scrape()






cred_file = #Cred File removed for confidentiality
gc = gspread.service_account(cred_file)
database = gc.open(#Sheet removed for confidentiality)
wks = database.worksheet("Rebuild")

label = []
row = 2
count = 0



print("\n\nDeleting Previous Data from Gsheet...\n\n")
wks.batch_clear(['A2:J1002'])
print("Deletion done. Starting the app..\n\n")






options = Options()
options.headless = True
driver = webdriver.Chrome(executable_path='./chromedriver', options=options)

URL = #URL removed for confidentiality
URL2 = #URL removed for confidentiality
URL3 = #URL removed for confidentiality





testcred()




print("\n\nScraping Completed! hehe\n\n")

driver.quit()





