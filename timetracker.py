import gspread
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as m
import datetime
import time

try:
    cred_file = 'queueautomation-354509-a7b5bd613358.json'
    gc = gspread.service_account(cred_file)
    database = gc.open("Tech Team Attendance Tracker")
    wks = database.worksheet("Sheet1")
except:
    m.showerror(message="Check your Internet Connection bitch!")
    quit()

user = "Tetow Mackie d' Great"
date = datetime.date.today()
date2 = date.strftime("%m-%d-%Y")




def loginwarning():
    try:
        try:
            if out == None:
                warn = m.askokcancel(title="Pagsyor dha", message="Sure jud ka ani?")
                if warn == True:
                    login()
                else:
                    initialWindow()
            else:
                warn = m.askokcancel(title="Pagsyor dha", message="Naka OUT naman ka for today Booords. Sure jud ka mo IN ka balik?")
                if warn == True:
                    cell = cell + 1
                    login()
                else:
                    initialWindow()
        except Exception as e:
            print(e)
            warn = m.askokcancel(title="Pagsyor dha", message="Sure jud ka ani?")
            if warn == True:
                login()
            else:
                initialWindow()
    except:
        m.showerror(message="Check your Internet Connection bitch!")
        window.destroy()



def logoutwarning():
    try:
        warn = m.askokcancel(title="Pagsyor dha", message="Sure jud ka aning Logout?")
        if warn == True:
            logout()
        else:
            login()
    except:
        m.showerror(message="Check your Internet Connection bitch!")
        window.destroy()

def login():
    try:
        try:
            if out == None:
                wks.update_cell(cell+1, 1, user)
                wks.update_cell(cell+1, 2, date2)
                wks.update_cell(cell+1, 3, time.strftime("%H:%M"))
        except NameError:
            wks.update_cell(cell, 1, user)
            wks.update_cell(cell, 2, date2)
            wks.update_cell(cell, 3, time.strftime("%H:%M"))
        
        label.config(text="Expected Time-Out: " + str(wks.cell(cell, 22).value))
        label2.config(text="Remaining Break-Time: " + str(wks.cell(cell, 20).value))
        breakoutBtn.config(state='disabled')
        loginBtn.config(state='disabled')
        breakinBtn.config(state='normal')
        logoutBtn.config(state='normal')
    except:
        m.showerror(message="Check your Internet Connection bitch!")
        window.destroy()

def breakk():
    try:
        if wks.cell(cell, 4).value == None:
            wks.update_cell(cell, 4, time.strftime("%H:%M"))
        elif wks.cell(cell, 6).value == None:
            wks.update_cell(cell, 6, time.strftime("%H:%M"))
        elif wks.cell(cell, 8).value == None:
            wks.update_cell(cell, 8, time.strftime("%H:%M"))
        elif wks.cell(cell, 10).value == None:
            wks.update_cell(cell, 10, time.strftime("%H:%M"))
        elif wks.cell(cell, 12).value == None:
            wks.update_cell(cell, 12, time.strftime("%H:%M"))

        label.config(text="Expected Time-Out: " + str(wks.cell(cell, 22).value))
        label2.config(text="Remaining Break-Time: " + str(wks.cell(cell, 20).value))
        loginBtn.config(state='disabled')
        breakoutBtn.config(state='normal')
        breakinBtn.config(state='disabled')
        logoutBtn.config(state='disabled')

    except:
        m.showerror(message="Check your Internet Connection bitch!")
        window.destroy()

def back():
    try:
        if wks.cell(cell, 5).value == None:
            wks.update_cell(cell, 5, time.strftime("%H:%M"))
        elif wks.cell(cell, 7).value == None:
            wks.update_cell(cell, 7, time.strftime("%H:%M"))
        elif wks.cell(cell, 9).value == None:
            wks.update_cell(cell, 9, time.strftime("%H:%M"))
        elif wks.cell(cell, 11).value == None:
            wks.update_cell(cell, 11, time.strftime("%H:%M"))
        elif wks.cell(cell, 13).value == None:
            wks.update_cell(cell, 13, time.strftime("%H:%M"))

        label.config(text="Expected Time-Out: " + str(wks.cell(cell, 22).value))
        label2.config(text="Remaining Break-Time: " + str(wks.cell(cell, 20).value))
        breakoutBtn.config(state='disabled')
        loginBtn.config(state='disabled')
        breakinBtn.config(state='normal')
        logoutBtn.config(state='normal')
    except:
        m.showerror(message="Check your Internet Connection bitch!")
        window.destroy()

def logout():
    try:
        wks.update_cell(cell, 21, time.strftime("%H:%M"))

        breakinBtn.config(state='disabled')
        breakoutBtn.config(state='disabled')
        logoutBtn.config(state='disabled')
        loginBtn.config(state='normal')
        window.destroy()
    except:
        m.showerror(message="Check your Internet Connection bitch!")
        window.destroy()
    



def initialWindow():
    loginBtn.config(state='normal',)
    breakinBtn.config(state='disabled')
    breakoutBtn.config(state='disabled')
    logoutBtn.config(state='disabled')


window = Tk()
window.title("Wow Tracker! Gwabeha ui.")
width = 400
height = 150
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
window.geometry("%dx%d+%d+%d" % (width, height, x, y))


myFrame = Frame(window)
myFrame.pack(padx=10, pady=10)


myFrame2 = Frame(window)
myFrame2.pack(padx=10, pady=10)

label = Label(myFrame, text = "Hi KewlKed!")
label.pack()
label2 = Label(myFrame, text = "")
label2.pack()




loginBtn = Button(myFrame2, text = "Time In",command=loginwarning)
breakinBtn = Button(myFrame2, text = "Break", command=breakk)
breakoutBtn = Button(myFrame2, text = "Back", command=back)
logoutBtn = Button(myFrame2, text = "Out", command=logoutwarning)

loginBtn.grid(column = 1, row = 1)
breakinBtn.grid(column = 2, row = 1)
breakoutBtn.grid(column = 3,row = 1)
logoutBtn.grid(column = 4, row = 1)




try:
    cell = wks.findall(user)
    cell = len(cell) + 1
    dateforcell = wks.cell(cell, 2).value
    
    
    if dateforcell == date2:
        
        break1 = wks.cell(cell, 4).value
        break2 = wks.cell(cell, 6).value
        break3 = wks.cell(cell, 8).value
        break4 = wks.cell(cell, 10).value
        break5 = wks.cell(cell, 12).value
        back1 = wks.cell(cell, 5).value
        back2 = wks.cell(cell, 7).value
        back3 = wks.cell(cell, 9).value
        back4 = wks.cell(cell, 11).value
        back5 = wks.cell(cell, 13).value
        out = wks.cell(cell, 20).value

        if out == None:
            if break1 != None:
                if back1 == None:
                    breakk()
                else:
                    if break2 != None:
                        if back2 == None:
                            breakk()
                        else:
                            if break3 != None:
                                if back3 == None:
                                    breakk()
                                else:
                                    if break4 != None:
                                        if back4 == None:
                                            breakk()
                                        else:
                                            if break5 != None:
                                                if back5 == None:
                                                    breakk()
                                            back()
                                    else:
                                        back()
                            else:
                                back()
                    else:
                        back()
            else:
                back()

        else:
            initialWindow()
    else:
        cell = len(cell) + 2
        initialWindow()
    
except Exception as e:
    cell = len(wks.col_values(2)) + 1
    initialWindow()
except:
    m.showerror(message="Check your Internet Connection bitch!")
    window.destroy()
    quit()




window.mainloop()