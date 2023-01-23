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


def printer():
    print("\n\nData Migration starts now..")
    n = len(wks.col_values(3))
    new = n + 1

    for i in range(len(caseNum)):
        try:
            wks.update_cell(new, 3, account[i])
            wks.update_cell(new, 6, onHold[i])
            wks.update_cell(new, 19, str("'" + caseNum[i]))
            wks.update_cell(new, 26, tam[i])
            new = new + 1
            time.sleep(3)
        except:
            print("Nawad an ka kadyots ug internet. booooo!")
            driver.quit()


    print("\n\nAll Done bitches!")
    driver.quit()

def startbitch():
    soup = BeautifulSoup(driver.page_source, "html.parser")

    allTR = soup.find_all('tr')


    for i in range(1, len(allTR)):
        caseNum.append(allTR[i].find('th').text.strip())
        listed = allTR[i].find_all('td')
        account.append(listed[2].text.strip())
        onHold.append(listed[6].text.strip())
        tam.append(listed[10].text.strip())

    
    printer()



def testcred():
    user = input("\n\nUsername (SFDC): ")
    password = pwinput.pwinput("Password (SFDC): ")
    print("\n\nTesting Login Credentials. Please wait..")

    driver.get(URL)

    try:
        wits = WebDriverWait(driver, 120).until(EC.presence_of_element_located
        ((By.ID, "username")))
    except TimeoutException:
        print("\n\nPage TimeOut, please check your Internet Connection.")
        driver.quit()

    driver.find_element(By.ID, "username").send_keys(user)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "Login").click()

    time.sleep(5)

    if str(driver.current_url).find(URL2) != -1:
        print("\n\nSuccess! Please check your Mobile Authenticator.")
    else:
        print("\n\nIncorrect Login Credentials. Try again.")
        testcred()

    while driver.current_url != URL:
        time.sleep(2)

    
    time.sleep(10)
    
    startbitch()
    
        

    




cred_file = 'queueautomation-354509-a7b5bd613358.json'
gc = gspread.service_account(cred_file)
database = gc.open("Tech Analyst Queue and Forecast Tracker 2023")
wks = database.worksheet("Tech Team Tracker")


URL = 'https://trustarc.my.salesforce.com/500/x?fcf=00B8a00000DxNz6&rpp_sticky=0&rowsperpage=1000'
URL2 = 'https://trustarc.my.salesforce.com/_ui/identity/verification/method/ToopherVerificationFinishUi'

caseNum = []
onHold = []
tam = []
account = []

options = Options()
options.headless = True
driver = webdriver.Chrome(executable_path='./chromedriver', options=options)
# driver.minimize_window()

testcred()