from bs4 import BeautifulSoup
import gspread
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pwinput






def getData():
    supps = wks.col_values(9)

    for i in gdict:
        final = -1

        driver.get("https://jira.truste.com/browse/" + str(gdict[i]))

        try:
            wits = WebDriverWait(driver, 10).until(EC.presence_of_element_located
            ((By.ID, "priority-val")))
        except TimeoutException:
            print("\n\nPage TimeOut, please check your Internet or TRUSTArc VPN Connection.\n\n")
            driver.quit()

        try:
            driver.find_element(By.CLASS_NAME, "collapsed-comments").click() #click collapsed comments just in case
            print("Clicked the Collapsed Comments")
            time.sleep(2)

            

        except:
            print("Expected Exception kay walay Collapsed Comments hehe")

        try:
            soup = BeautifulSoup(driver.page_source, "html.parser")
            com = soup.find_all('div', class_="activity-comment")
        except Exception as e:
            print("Connection Interrupted, please check your Internet or TrustArc VPN Connection.")
            print(e)

        if len(com) == 0:
            namedata = ""
            comdata = "There are no comments yet on this issue."
            comdatedata = ""

            wks.update_cell(i, 3, namedata)
            wks.update_cell(i, 4, comdata)
            wks.update_cell(i, 5, comdatedata)
            time.sleep(2)
            continue

        else:
            for j in com:
                try:
                    name = j.find('a', class_="user-avatar").text.strip()
                    compare.append(name)

                except AttributeError:
                    name = j.find('span', class_="user-avatar").text.strip()
                    compare.append(name)

                except Exception as e:
                    print(e)
                    print("Chata si Jay if muguwas ni kay naay unaccounted Exception")
                
    

            for k in range(len(compare)):
                if compare[k] not in supps:
                    final = k
                    break
                

            
            
            if final == -1:
                wks.update_cell(i, 3, "")
                wks.update_cell(i, 4, "No Comment from Non-Support")
                wks.update_cell(i, 5, "")

                time.sleep(3)

                compare.clear()
                continue

            else:
                try:
                    name2 = com[final].find('a', class_="user-avatar").text.strip()
                    commentdescript = com[final].find('div', class_="action-body").text.strip()
                    commentdate = com[final].find('span', class_="user-tz").get('title')
                
                    wks.update_cell(i, 3, str(name2))
                    wks.update_cell(i, 4, str(commentdescript))
                    wks.update_cell(i, 5, str(commentdate))
                    time.sleep(3)

                except AttributeError:
                    name2 = com[final].find('span', class_="user-avatar").text.strip()
                    commentdescript = com[final].find('div', class_="action-body").text.strip()
                    commentdate = com[final].find('span', class_="user-tz").get('title')

                    wks.update_cell(i, 3, str(name2))
                    wks.update_cell(i, 4, str(commentdescript))
                    wks.update_cell(i, 5, str(commentdate))
                    time.sleep(3)

                except Exception as e:
                    print("wa madakpi nga error")
                    print("Chata si Jay nya iSS ni nga error")
                    print(e)
                    driver.quit()
                    quit()

                finally:
                    compare.clear()
            

    # for i in range(len(namedata)):
    #     wks.update_cell(i + 2, 3, namedata[i])
    #     wks.update_cell(i + 2, 4, comdata[i])
    #     wks.update_cell(i + 2, 5, comdatedata[i])
    #     time.sleep(1)
    


    print("\n\nData Input Completed. Congrats lods!")
    driver.quit()


                    

    




def testcred():
    user = input("\n\nUsername (JIRA): ")
    password = pwinput.pwinput("Password (JIRA): ")
    print("\n\nTesting Login Credentials, please wait...")


    driver.get(URL)

    time.sleep(2)
    
    try:
        wits = WebDriverWait(driver, 10).until(EC.presence_of_element_located
        ((By.ID, "login-form-username")))
    except TimeoutException:
        print("\n\nPage TimeOut, please check your Internet or TrustArc VPN Connection.")
        driver.quit()

    driver.find_element(By.ID, "login-form-username").send_keys(user)
    driver.find_element(By.ID, "login-form-password").send_keys(password)
    driver.find_element(By.ID, "login-form-submit").click()

    time.sleep(5)

    if driver.current_url != URL2:
        print("\n\nIncorrect Credentials: Please Try Again.")
        testcred()
    else:
        print("\n\nPerfect! App Running. Please wait while I gather the info...\n\n")
        getData()



namedata = []
comdata = []
comdatedata = []
gdict = {}

compare = []


cred_file = 'jiralocatecomment-e4a6d2b5b760.json'
gc = gspread.service_account(cred_file)
database = gc.open("JIRA Comment Locator")
wks = database.worksheet("Sheet1")

a = wks.col_values(1)
b = wks.col_values(20)




for i in range(2, len(a)+1):
    if b[i-1] == "None":
        gdict[i] = a[i-1]






options = Options()
options.headless = True
driver = webdriver.Chrome(executable_path='./chromedriver', options=options)


URL = "https://jira.truste.com/login.jsp?os_destination=%2Fsecure%2FDashboard.jspa"
URL2 = "https://jira.truste.com/secure/Dashboard.jspa"

testcred()
