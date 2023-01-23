import gspread
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as m
import webbrowser
import traceback
from datetime import datetime


alllinks = {}
form = {}
taskproc = {}
genproc = {}
other = {}
leaves = []



# print(current_Day)
# print(current_Month)
# quit()





def checkbutton(hm1, hm2, hm3):
    if hm1.get() == 1:
        webbrowser.open_new_tab(queue)
    if hm2.get() == 1:
        webbrowser.open_new_tab(aws)
    if hm3.get() == 1:
        webbrowser.open_new_tab(meet)    

def openlink(link):
    webbrowser.open_new_tab(alllinks.get(link.get()))
    select()

def lezgo(opt):
    if opt.get() == "Task Processes":
        choices = taskproc.keys()
    elif opt.get() == "General Processes":
        choices = genproc.keys()
    elif opt.get() == "Forms/Notes":
        choices = form.keys()
    elif opt.get() == "Others":
        choices = other.keys()

    for wid in myFrame.winfo_children():
        wid.destroy()

    
    opt2 = StringVar(myFrame)
    opt2.set("Select below: ")

    test = OptionMenu(myFrame, opt2, *choices)
    test.config(width=18)
    test.grid(column=1, row=0, columnspan=2)

    gobut = Button(myFrame, text = "Go!", command = lambda: openlink(opt2))
    gobut.grid(column=1, row=3)
    backbut = Button(myFrame, text = "Back", command=select)
    backbut.grid(column=2, row=3)


# def inspiration():
#     for wid in myFrame.winfo_children():
#         wid.destroy()

#     ran = random.randint(0, 4)

#     img = Image.open(pics[ran])
#     #img.resize((10, 10), Image.Resampling.LANCZOS)
#     imgtest = ImageTk.PhotoImage(img)

#     label = Label(myFrame, image=imgtest)
#     label.image = imgtest
#     label.pack()


def select():
    for wid in myFrame.winfo_children():
        wid.destroy()


    current_Month = datetime.now().strftime('%h')
    current_Day = datetime.now().strftime('%-d')
    dayoftheweek = datetime.today().weekday()


    try:
        cred_file = 'queueautomation-354509-a7b5bd613358.json'
        gc = gspread.service_account(cred_file)
        database = gc.open("Repository Database")
        wks = database.worksheet("Sheet1")

        database = gc.open("GPS Tech Analyst Team 2023 Monthly Calendar")
        wks2 = database.worksheet(str(current_Month)) #str(current_Month)


        type_name = wks.col_values(3)
        name = wks.col_values(1)
        link_name = wks.col_values(2)


        testcell = wks2.find(current_Day) #current_Day
        for i in range(1,6):
            leaves.append(wks2.cell(testcell.row + i, testcell.col).value)

        leaves2 = list(set(leaves))
        leaves2.remove(None)

        

        for i in range(len(type_name)):
            alllinks[name[i]] = link_name[i]

            if type_name[i] == "Task Processes":
                taskproc[name[i]] = link_name[i]
            elif type_name[i] == "General Processes":
                genproc[name[i]] = link_name[i]
            elif type_name[i] == "Forms/Notes":
                form[name[i]] = link_name[i]
            elif type_name[i] == "Others":
                other[name[i]] = link_name[i]
        
        new_type_name = list(set(type_name)) #remove duplicates
        new_type_name.remove('Type')

        queue = wks.cell(row=2, col=12).value
        aws = wks.cell(row=3, col=12).value
        meet = wks.cell(row=4, col=12).value

    
            




    except Exception as e:
        m.showerror(message="Check your Internet Connection bitch!")
        print(e)
        print(traceback.format_exc())
        quit()

    label = Label(myFrame, text="Repository Links: ")
    label.grid(row=0, column=1)

    opt = StringVar(myFrame)
    opt.set("Select Task Processes bitch!")

    test = OptionMenu(myFrame, opt, *new_type_name)
    test.config(width=18)
    test.grid(column=1, row=1)

    gobut = Button(myFrame, text = "Select!", command = lambda: lezgo(opt))
    gobut.grid(column=1, row=3)


    label = Label(myFrame2, text="Tech Analyst on Vacaycay: ", borderwidth=2, relief="groove", padx=5, pady=5)
    label.grid(row=0, column=0)

  
    if dayoftheweek > 4:
        label = Label(myFrame2, text="Weekends today sir")
        label.grid(row=1, column=0)
        label2 = Label(myFrame2, text="Ay sig Werk dha!")
        label2.grid(row=2, column=0)
    else:
        if len(leaves2) > 0:
            for i in range(1, len(leaves2)+1):
                label = Label(myFrame2, text=leaves2[i-1])
                label.grid(row=i, column=0)
        else:
            label = Label(myFrame2, text="Everybody is present Today")
            label2 = Label(myFrame2, text="#PASSION")

            label.grid(row=1, column=0)
            label2.grid(row=2, column=0)

    
    label = Label(myFrame3, text="Quick Links: ")
    label.grid(row=0, columnspan=3)

    hm1 = IntVar()
    hm2 = IntVar()
    hm3 = IntVar()

    queue = Checkbutton(myFrame3, text="Queue", variable=hm1)
    queue.grid(row=1, column=0)

    aws = Checkbutton(myFrame3, text="Aws Sheet", variable=hm2)
    aws.grid(row=1, column=1)

    meet = Checkbutton(myFrame3, text="Meeting Notes", variable=hm3)
    meet.grid(row=1, column=2)


    buttoncheck = Button(myFrame3, text="Open QuickLink(s)!", command= lambda: checkbutton(hm1 ,hm2, hm3))
    buttoncheck.grid(row=2, columnspan=3)

    window.after(3720000, select)

    



    
    







window = Tk()
window.title("Wow Repository! Gwabeha ui.")
width = 430
height = 250
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
window.geometry("%dx%d+%d+%d" % (width, height, x, y))



myFrame = Frame(window, width=250, height=160, highlightbackground='red')
myFrame.grid(row=0, column=0, padx=10, pady=10)
myFrame.propagate(0)

myFrame2 = Frame(window, width=250, height=160, highlightbackground='red')
myFrame2.grid(row=0, column=1, padx=10, pady=10)
myFrame2.propagate(0)

myFrame3 = Frame(window, width=500, height=160)
myFrame3.grid(row=1, columnspan=2)
myFrame3.propagate(0)

# label = Label(myFrame2, text = "Hi KewlKed!")
# label.pack()


select()





window.mainloop()



