from bs4 import BeautifulSoup
import gspread
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import pwinput



def codeRedStart():
    driver.get(URL2)
    time.sleep(3)

    while driver.current_url != URL2:
        time.sleep(3)

    codeRed = driver.find_elements(By.CLASS_NAME, 'todo')

    mainRow = len(wks2.col_values(3))
    row = 2

    while mainRow > 1:
        wks2.update_cell(mainRow, 3, "")
        mainRow = mainRow - 1
        time.sleep(3)

    for i in codeRed:
        clientName = i.find_element(By.TAG_NAME, 'a').text
        split2 = clientName.split('— ')
        wks2.update_cell(row, 3, split2[1])
        row = row + 1
        time.sleep(3)

    print("\n\n All tasks migrated. Code Red Sheet is now Updated as well. Thank Jay! <3")
    driver.quit()



def startbitch():
    n = len(wks.col_values(3))
    new_n1 = n + 1
    new_n2 = n + 1
    new_n3 = n + 1

    todo_list = driver.find_elements(By.CLASS_NAME, 'todo_list')



    for i in todo_list: #[0]
        todo = i.find_elements(By.CLASS_NAME, 'todo')
        todo2 = i.find_elements(By.CLASS_NAME, 'todolist')
        for i in todo:
            todoval = i.find_elements(By.TAG_NAME, 'a')
            for i in todoval:
                val = i.text

        for j in todo2:
            #tr is inside todolist
            tr = j.find_elements(By.TAG_NAME, 'tr')
            for j in tr:
                try:
                    fog = j.find_element(By.TAG_NAME, 'a') #test if naay title
                    try:
                        due = j.find_element(By.CLASS_NAME, 'due').text
                        content = j.find_element(By.CLASS_NAME, 'content').text
                        todolisttit = j.find_element(By.CLASS_NAME, 'todolisttitle').text
                        tempval = todolisttit
                        splitter = val.split('— ')
                        wks.update_cell(new_n1, 3, splitter[1])
                        wks.update_cell(new_n1, 19, todolisttit + "  " + content)
                        wks.update_cell(new_n1, 6, due[4:len(due)])
                        wks.update_cell(new_n1, 26, splitter[0])
                        new_n1 = new_n1 + 1
                        time.sleep(3)
                    except NoSuchElementException:
                        print('no date, will not include this shit')

                except NoSuchElementException:
                    print('success nakasud sa except')
                    try:
                        due = j.find_element(By.CLASS_NAME, 'due').text
                        content = j.find_element(By.CLASS_NAME, 'content').text
                        splitter = val.split('— ')
                        wks.update_cell(new_n1, 3, splitter[1])
                        wks.update_cell(new_n1, 6, due[4:len(due)])
                        wks.update_cell(new_n1, 19, tempval + "  " + content)
                        wks.update_cell(new_n1, 26, splitter[0])
                        new_n1 = new_n1 + 1
                        time.sleep(3)
                    except NoSuchElementException:
                        print('no date and no title. double dead')
    codeRedStart()

def testCred():
    user = input("\n\nUsername (TRUSTArc Gmail Account): ")
    password = pwinput.pwinput("Password (TRUSTArc Gmail Password): ")
    print("\n\nTesting Login Credentials. Please wait..")

    driver.get(URL)

    try:
        wits = WebDriverWait(driver, 120).until(EC.presence_of_element_located
        ((By.CLASS_NAME, "action_button")))
    except TimeoutException:
        print("\n\nPage TimeOut, please check your Internet Connection.")
        driver.quit()

    
    driver.find_element(By.CLASS_NAME, "action_button").click()

    driver.maximize_window()


    try:
        wits = WebDriverWait(driver, 120).until(EC.presence_of_element_located
        ((By.ID, "identifierId")))
    except TimeoutException:
        print("\n\nPage TimeOut, please check your Internet Connection.")
        driver.quit()

    driver.find_element(By.ID, "identifierId").send_keys(user)
    driver.find_element(By.ID, "identifierNext").click()

    try:
        wits = WebDriverWait(driver, 10).until(EC.presence_of_element_located
        ((By.NAME, "password")))

    except TimeoutException:
        print("\n\nIncorrect Username! Try Again.")
        testCred()

    time.sleep(2)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.ID, "passwordNext").click()

    driver.minimize_window()


    print("\n\nClick your 2-Factor Authentication on your Phone..")

    try:
        wits = WebDriverWait(driver, 160).until(EC.presence_of_element_located
        ((By.ID, "due_frame")))
    except TimeoutException:
        print("\n\nPage TimeOut, please check your Internet Connection.")
        driver.quit()

    
    print("\n\nCongrats! Scraping Starts now..\n\n")
    startbitch()


    
    
    



cred_file = 'queueautomation-354509-a7b5bd613358.json'
gc = gspread.service_account(cred_file)
database = gc.open("Tech Analyst Queue and Forecast Tracker 2023")
wks = database.worksheet("Tech Team Tracker")
wks2 = database.worksheet("Code Red Clients")

URL = 'https://truste1.basecamphq.com/todo_lists?utf8=%E2%9C%93&responsible_party=12788789&due_frame=next_week'
URL2 = 'https://truste1.basecamphq.com/todo_lists?utf8=%E2%9C%93&responsible_party=12788789&due_frame=all'


# options = Options()
# options.headless = True
driver = webdriver.Chrome(executable_path='./chromedriver')#, options=options)
driver.minimize_window()

testCred()