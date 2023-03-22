import tkinter

from tkinter import *
from tkinter import ttk
from os import system, name
from datetime import *
from datetime import datetime


import pickle

top = Tk() #size of program
top.geometry("800x800")
main = Frame(top)
final_date = 0
final_time = ""


def StallMenu(aa, bb):
    reset()

    stallsTitle = ["McDonalds Menu: ", "Subway Menu: ", "Soup Delight Menu: ", "Chicken Rice Menu: ", "Mini Wok Menu: ", #stalls
                   "Indian Food Menu: "]
    top.title(stallsTitle[aa])
    with open("StallMenu.data", 'wb') as myFile:
        pickle.dump(Menu, myFile)

    with open('StallMenu.data', 'rb') as myFile:
        MenuList = pickle.load(myFile)

    str1 = MenuList[aa][bb][0]
    str2 = MenuList[aa][bb][1]
    Dish1 = Button(top, text=str1, width=40, height=3, bg='light blue', fg='black', activebackground='light blue', #dishes named below
                   activeforeground='black')
    Dish1.pack()
    Dish2 = Button(top, text=str2, width=40, height=3, bg='light blue', fg='black', activebackground='light blue',
                   activeforeground='black')
    Dish2.pack()
    BackB = Button(top, text ="Back", command = StartPg, width=10, height=1, bg='light blue', fg='black', activebackground='light blue', activeforeground='black')
    BackB.pack()

def OperatingHours(StallNum): 
    reset()
    closingTime = {0: [23, 00],#closing time weekdays
                   1: [22, 00],
                   2: [20, 3],
                   3: [21, 00],
                   4: [20, 3],
                   5: [21, 00]}

    WclosingTime = {0: [22, 00],#closing time weekends
                    1: [21, 00],
                    2: [19, 3],
                    3: [20, 00],
                    4: [19, 3],
                    5: [20, 00]}

    openingTime = {0: [7, 00],#opening times
                   1: [7, 00],
                   2: [8, 3],
                   3: [8, 00],
                   4: [7, 3],
                   5: [8, 00]}

    opening = openingTime.get(StallNum)
    closing = closingTime.get(StallNum)
    Wclosing = WclosingTime.get(StallNum)

    now = datetime.now()

    openTime = now.replace(hour=opening[0], minute=opening[1], second=0, microsecond=0)
    closeTime = now.replace(hour=closing[0], minute=closing[1], second=0, microsecond=0)
    WcloseTime = now.replace(hour=Wclosing[0], minute=Wclosing[1], second=0, microsecond=0)

    textMsg = "Opening Time: 0{}:{}0 hours \n Closing Time (Mon - Fri): {}:{}0 hours \n Closing Time (Sat - Sun): {}:{}0 hours ".format(
        openTime.hour, openTime.minute, closeTime.hour, closeTime.minute, WcloseTime.hour, WcloseTime.minute)

    stallsTitle = ["McDonalds Operating Hours: ", "Subway Operating Hours: ", "Soup Delight Operating Hours: ",
                   "Chicken Rice Operating Hours: ", "Mini Wok Operating Hours: ", "Indian Food Operating Hours: "]
    Label(top, text=stallsTitle[StallNum], width=40, height=3, bg='light blue', fg='black', activebackground='light blue',
          activeforeground='black').pack()
    Label(top, text=textMsg, width=40, height=3, bg='light blue', fg='black', activebackground='light blue',
          activeforeground='black').pack()
    BackB = Button(top, text ="Back", command = StartPg, width=10, height=1, bg='light blue', fg='black', activebackground='light blue', activeforeground='black')
    BackB.pack()

def WaitingTime(StallNo):
    reset()

    def get_value(entryWidget): #input error
        value = entryWidget.get()
        try:
            return int(value)
        except ValueError:
            return None

    def convert(value):
        if value is None:
            return None
        else:
            TimeWait = {0: [2], #calculating time taken/person
                        1: [3],
                        2: [4],
                        3: [6],
                        4: [5],
                        5: [8]}

            wait = TimeWait.get(StallNo)
            TotWait = wait[0] * value
            return TotWait

    def set_label_text(label, entry):
        value = convert(get_value(entry))
        if value is None:
            Label(top, text="Enter number of people in line: ", width=40, height=3, bg='light blue', fg='black',
                  activebackground='light blue', activeforeground='black').pack()
        else:
            WTMsg = "Waiting Time: {} minutes".format(value)
            Label(top, text=WTMsg, width=40, height=3, bg='light blue', fg='black', activebackground='light blue',
                  activeforeground='black').pack()

    Label(top, text="Enter number of people in line: ", width=40, height=3, bg='light blue', fg='black',
          activebackground='light blue', activeforeground='black').pack()
    NoP = Entry(top)
    l = Label(top, text="")
    b = Button(top, text="Enter", command=lambda: set_label_text(l, NoP), width=40, height=3, bg='light blue',
               fg='black', activebackground='light blue', activeforeground='black')

    NoP.pack()
    l.pack()
    b.pack()
    BackB = Button(top, text ="Back", command = StartPg, width=10, height=1, bg='light blue', fg='black', activebackground='light blue', activeforeground='black')
    BackB.pack()

def DateTimeDay(StallNumber):
    reset()
    dateToday = date.today()
    timeNow = datetime.now()
    dayToday = date.today().weekday()
    print(dateToday)
    print(timeNow)

    switcher = {0: "Monday",
                1: "Tuesday",
                2: "Wednesday",
                3: "Thursday",
                4: "Friday",
                5: "Saturday",
                6: "Sunday"}

    dayName = switcher.get(dayToday) #changing date to day
    print(dayName)
    text1 = "{} , {}:".format(dayName, timeNow)
    print(text1)
    Label(top, text=text1, width=40, height=3, bg='light blue', fg='black', activebackground='light blue',
          activeforeground='black').pack()

    openingTime = {0: [7, 0],
                   1: [7, 0],
                   2: [8, 3],
                   3: [8, 0],
                   4: [7, 3],
                   5: [8, 0]}

    afternoonTime = {0: [11, 0],
                     1: [11, 0],
                     2: [12, 3],
                     3: [12, 0],
                     4: [11, 3],
                     5: [12, 0]}

    closingTime = {0: [23, 0],
                   1: [22, 0],
                   2: [20, 3],
                   3: [21, 0],
                   4: [20, 3],
                   5: [21, 0]}

    WclosingTime = {0: [22, 0],
                    1: [21, 0],
                    2: [19, 3],
                    3: [20, 0],
                    4: [19, 3],
                    5: [20, 0]}

    if dayToday == 5 or dayToday == 6: #weekends
        oT_var = openingTime.get(StallNumber)
        aT_var = afternoonTime.get(StallNumber)
        cT_var = WclosingTime.get(StallNumber)

    else: #weekdays
        oT_var = openingTime.get(StallNumber)
        aT_var = afternoonTime.get(StallNumber)
        cT_var = closingTime.get(StallNumber)

    now = datetime.now()

    morning = now.replace(hour=oT_var[0], minute=oT_var[1], second=0, microsecond=0)
    afternoon = now.replace(hour=aT_var[0], minute=aT_var[1], second=0, microsecond=0)
    closing = now.replace(hour=cT_var[0], minute=cT_var[1], second=0, microsecond=0)

    if (dayToday == 0 or dayToday == 2 or dayToday == 4 or dayToday == 6) and (
            timeNow < afternoon and timeNow > morning):
        StallMenu(StallNumber, 0)
    elif (dayToday == 0 or dayToday == 2 or dayToday == 4 or dayToday == 6) and (
            timeNow < closing and timeNow > afternoon):
        StallMenu(StallNumber, 1)
    elif (dayToday == 1 or dayToday == 3 or dayToday == 5) and (timeNow < afternoon and timeNow > morning):
        StallMenu(StallNumber, 2)
    elif (dayToday == 1 or dayToday == 3 or dayToday == 5) and (timeNow < closing and timeNow > afternoon):
        StallMenu(StallNumber, 3)
    else:
        text2 = "The stall is unavailable right now, please try again later!"
        Label(top, text=text2, width=40, height=3, bg='light blue', fg='black', activebackground='light blue',
              activeforeground='black').pack()
        D = Button(top, text="Check Operating Hours", command=lambda: OperatingHours(StallNumber), width=40, height=1, bg='light blue',
                           fg='black', activebackground='light blue', activeforeground='black')
        D.pack()

    BackB = Button(top, text ="Back", command = StartPg, width=10, height=1, bg='light blue', fg='black', activebackground='light blue', activeforeground='black')
    BackB.pack()

def setFinalDate(dayValue):
    global final_date
    final_date = dayValue


def setFinalTime(timeValue):
    global final_time
    final_time = timeValue



def UserDateTimeDay(StallNum):
    reset()


    def userinputDate():
        def GetValDate(entryWidget):
            dateValue = entryWidget.get()
            try:
                return str(dateValue)
            except ValueError:
                return None

        def convertDate(dateValue):
            if dateValue is None:
                return None
            else:
                userDate = datetime.strptime(dateValue, "%d/%m/%Y")
                userDay = userDate.weekday()
                print(userDay)
                return userDay



        def set_label_text_Date(label, entry):
            dayValue = convertDate(GetValDate(entry))
            setFinalDate(dayValue)
            if dayValue is None:
                Label(top, text="Enter Date: (DD/MM/YYYY) ", width=40, height=3, bg='light blue', fg='black',
                      activebackground='light blue', activeforeground='black').pack()
            else:
                
                return dayValue

        Label(top, text="Enter Date: (DD/MM/YYYY) ", width=40, height=3, bg='light blue', fg='black',
              activebackground='light blue', activeforeground='black').pack()
        DateEnt = Entry(top)
        l = Label(top, text="")
        b = Button(top, text="Next", command=lambda: set_label_text_Date(l, DateEnt), width=10, height=1, bg='light blue',
                   fg='black', activebackground='light blue', activeforeground='black')

        DateEnt.pack()
        l.pack()
        b.pack()

    def userinputTime():

        def GetValTime(entryW):
            timeValue = entryW.get()
            try:
                return str(timeValue)
            except ValueError:
                
                return None

        def convertTime(timeValue):
            if timeValue is None:
                return None
            else:
                userTime = datetime.strptime(timeValue, "%H:%M")
                print(userTime)

                return userTime

        def set_label_text_Time(label, entry):
            timeValue = convertTime(GetValTime(entry))
            setFinalTime(timeValue)
            if timeValue is None:
                Label(top, text="Enter Time in 24 hour format: (HH:MM) ", width=40, height=3, bg='light blue',
                      fg='black', activebackground='light blue', activeforeground='black').pack()
            else:
                now = datetime.now()

                userInp = now.replace(hour=timeValue.hour, minute=timeValue.minute, second=0, microsecond=0)
                return userInp
                
        
        Label(top, text="Enter Time in 24 hour format: (HH:MM) ", width=40, height=3, bg='light blue', fg='black',
              activebackground='light blue', activeforeground='black').pack()
        TimeEnt = Entry(top)
        l2 = Label(top, text="")
        b2 = Button(top, text="Enter", command=lambda: set_label_text_Time(l2, TimeEnt), width=10, height=1,
                    bg='light blue', fg='black', activebackground='light blue', activeforeground='black')

        TimeEnt.pack()
        l2.pack()
        b2.pack()

    def getDateandTime(StNo):
        DV = userinputDate()
        
        TV = userinputTime()

        def MenuSelec(SN, DayV, TimeV):
            
            print(TimeV)
            print(DayV)

            openingTime = {0: [7, 0],
                           1: [7, 0],
                           2: [8, 3],
                           3: [8, 0],
                           4: [7, 3],
                           5: [8, 0]}

            afternoonTime = {0: [11, 0],
                             1: [11, 0],
                             2: [12, 3],
                             3: [12, 0],
                             4: [11, 3],
                             5: [12, 0]}

            closingTime = {0: [23, 0],
                           1: [22, 0],
                           2: [20, 3],
                           3: [21, 0],
                           4: [20, 3],
                           5: [21, 0]}

            WclosingTime = {0: [22, 0],
                            1: [21, 0],
                            2: [19, 3],
                            3: [20, 0],
                            4: [19, 3],
                            5: [20, 0]}

            if DayV == 5 or DayV == 6:
                oT_var = openingTime.get(SN)
                aT_var = afternoonTime.get(SN)
                cT_var = WclosingTime.get(SN)

            else:
                oT_var = openingTime.get(SN)
                aT_var = afternoonTime.get(SN)
                cT_var = closingTime.get(SN)

            now = datetime.now()
            
            morning = now.replace(hour = oT_var[0], minute = oT_var[1], second = 0, microsecond = 0)
            afternoon = now.replace(hour = aT_var[0], minute = aT_var[1], second = 0, microsecond = 0)
            closing = now.replace(hour = cT_var[0], minute = cT_var[1], second = 0, microsecond = 0)
            TimeVar = now.replace(hour = TimeV.hour, minute = TimeV.minute, second = 0, microsecond = 0)


            if (DayV == 0 or DayV == 2 or DayV == 4 or  DayV == 6) and (TimeVar < afternoon and TimeVar > morning):
                StallMenu(SN, 0)
            elif (DayV == 0 or DayV == 2 or DayV == 4 or  DayV == 6) and (TimeVar < closing and TimeVar > afternoon):
                StallMenu(SN, 1)
            elif (DayV == 1 or DayV == 3 or DayV == 5) and (TimeVar < afternoon and TimeVar > morning):
                StallMenu(SN, 2)
            elif (DayV == 1 or DayV == 3 or DayV == 5) and (TimeVar < closing and TimeVar > afternoon):
                StallMenu(SN, 3)
            else:
                text2 = "The stall is unavailable right now, please try again later!"
                Label(top, text = text2, width=40, height=3, bg='light blue', fg='black',activebackground='light blue', activeforeground='black').pack()
                D = Button(top, text="Check Operating Hours", command=lambda: OperatingHours(SN), width=40, height=1, bg='light blue',
                           fg='black', activebackground='light blue', activeforeground='black')
                D.pack()
        b3 = Button(top, text="Enter", command=lambda: MenuSelec(StNo, final_date, final_time), width=40, height=3, bg='light blue',
                    fg='black', activebackground='light blue', activeforeground='black')
        b3.pack()

        
    getDateandTime(StallNum)
    BackB = Button(top, text ="Back", command = StartPg, width=10, height=1, bg='light blue', fg='black', activebackground='light blue', activeforeground='black')
    BackB.pack()


def StallNames():
    reset()
    top.title("Real-time Canteen Information System")
    Stalls = Label(top, text = "What would you like to have today?", font=("Helvetica",20))
    Stalls.pack()
    
    A = Button(top, text="McDonalds", command=lambda: ChoicePg(0), width=40, height=3, bg='light blue', fg='black',#stall buttons
               activebackground='light blue', activeforeground='black')
    A.pack()
    B = Button(top, text="Subway", command=lambda: ChoicePg(1), width=40, height=3, bg='light blue', fg='black',
               activebackground='light blue', activeforeground='black')
    B.pack()
    C = Button(top, text="Soup Delight", command=lambda: ChoicePg(2), width=40, height=3, bg='light blue', fg='black',
               activebackground='light blue', activeforeground='black')
    C.pack()
    D = Button(top, text="Chicken Rice", command=lambda: ChoicePg(3), width=40, height=3, bg='light blue', fg='black',
               activebackground='light blue', activeforeground='black')
    D.pack()
    E = Button(top, text="Mini Wok", command=lambda: ChoicePg(4), width=40, height=3, bg='light blue', fg='black',
               activebackground='light blue', activeforeground='black')
    E.pack()
    F = Button(top, text="Indian Food", command=lambda: ChoicePg(5), width=40, height=3, bg='light blue', fg='black',
               activebackground='light blue', activeforeground='black')
    F.pack()
    BackB = Button(top, text ="Back", command = StartPg, width=10, height=1, bg='light blue', fg='black', activebackground='light blue', activeforeground='black')
    BackB.pack()


def reset():#reset function
    for child in top.winfo_children():
        child.destroy()


def ChoicePg(x):#what to do after choosing store
    reset()
    top.title("Real-time Canteen Information System")
    Options = Label(top, text = "Please select one of the following options:", font= ("Helvetica", 20))
    Options.pack()
    
    A = Button(top, text="Check Menu based on Current Date and Time ", command=lambda: DateTimeDay(x), width=40,
               height=3, bg='light blue', fg='black', activebackground='light blue', activeforeground='black')
    A.pack()
    B = Button(top, text="Check Menu based on Other Date and Time", command=lambda: UserDateTimeDay(x), width=40,
               height=3, bg='light blue', fg='black', activebackground='light blue', activeforeground='black')
    B.pack()
    C = Button(top, text="Check Waiting Time", command=lambda: WaitingTime(x), width=40, height=3, bg='light blue',
               fg='black', activebackground='light blue', activeforeground='black')
    C.pack()
    D = Button(top, text="Check Operating Hours", command=lambda: OperatingHours(x), width=40, height=3, bg='light blue',
               fg='black', activebackground='light blue', activeforeground='black')
    D.pack()
    BackB = Button(top, text ="Back", command = StartPg, width=10, height=1, bg='light blue', fg='black', activebackground='light blue', activeforeground='black')
    BackB.pack()


def StartPg():#first page of program enter/quit
    reset()
    top.title("Real-time Canteen Information System")
    Welcome = Label(top, text = "Welcome to North Spine Canteen!", font= ("Helvetica", 20))
    Welcome.pack()

    En = Button(top, text="Enter", command=StallNames, width=40, height=3, bg='light blue', fg='black', #button function to stalls
                activebackground='light blue', activeforeground='black')
    En.pack()
    Ex = Button(top, text="Quit", command=top.destroy, width=40, height=3,  bg='light blue', fg='black', #exit button
                activebackground='light blue', activeforeground='black')
    Ex.pack()



Menu = [[[["Scrambled Eggs: S$3"], ["Sausages: S$4"]],          #menu items
         [["McChicken: S$3"], ["Fillet o Fish: S$2"]],             
         [["Pancakes: S$2.8"], ["Hashbrown: S$1.5"]],
         [["Cheeseburger: S$4"], ["Chicken Nuggets: S$6"]]],
        [[["Chicken Ham: S$4"], ["Classic Tuna: S$4.7"]],
         [["Ham and Cheese: S$6"], ["BBQ Chicken: S$5"]],
         [["Egg and Cheese: S$3.8"], ["Turkey: S$4"]],
         [["Roast Beef: S$5.8"], ["Spicy Italian: S$6"]]],
        [[["Fish Soup: S$5.5"], ["Beef Noodle Soup: S$5.8"]],
         [["Vegetable Soup: S$4"], ["Tom Yum Seafood Soup: S$6"]],
         [["Seafood Soup: S$5.5"], ["Salmon Fish Soup: S$5.6"]],
         [["Clear Vegetable Soup: S$4"], ["Pork Dumblings Soup: S$6.5"]]],
        [[["Soya Sauce Chicken Rice: S$3"], ["Pork Ribs Rice: S$3.4"]],
         [["Roasted Pork Rice: S$3"], ["Oyster Sauce Vegetable: S$4"]],
         [["Char Siew Rice: S$3.6"], ["Steamed Chicken Rice: S$3.4"]],
         [["Bean Sprouts: S$2"], ["Roasted Chicken Rice: S$3.4"]]],
        [[["Sambal Fish Rice: S$3.4"], ["Hokkien Noodles: S$3.5"]],
         [["Mee Goreng: S$3.5"], ["Dry Curry Beef Rice: S$3.8"]],
         [["Vegetable Fried Rice: S$2.4"], ["Black Pepper Beef Rice: S$3.8"]],
         [["Salted Egg Chicken Rice: S$3.1"], ["Pork Chop Rice: S$4"]]],
        [[["Egg Prata: S$2.7"], ["Onion Prata: S$2.3"]],
         [["Butter Chicken: S$3.4"], ["Chicken Curry: S$3"]],
         [["Cheese Prata: S$2"], ["Plain Prata: S$1.7"]],
         [["Rava Dosa: S$1.5"], ["Samosa Chaat: S$2"]]]]

StartPg()

top.mainloop()
