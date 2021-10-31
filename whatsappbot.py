from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,datetime
from ttkthemes import ThemedStyle
import tkinter as tk
from tkinter import ttk


launched=False
global driver

class web:
#intializing GUI in constructor
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Whatsapp Automater')

        style = ThemedStyle(self.root)
        style.set_theme("arc")

        self.canvas1 = tk.Canvas(self.root, width=500, height=500)
        self.canvas1.pack()

        label1 = ttk.Label(self.root, text='Whatsapp Automation')
        label1.config(font=('helvetica', 14))
        self.canvas1.create_window(250, 25, window=label1)

        label2 = ttk.Label(self.root, text='Type the Message:')
        label2.config(font=('helvetica', 10))
        self.canvas1.create_window(100, 100, window=label2)

        label3 = ttk.Label(self.root, text='Type the Group name')
        label3.config(font=('helvetica', 10))
        self.canvas1.create_window(100, 140, window=label3)

        label4 = ttk.Label(self.root, text='Enter the number of  iteration')
        label4.config(font=('helvetica', 10))
        self.canvas1.create_window(100, 180, window=label4)

        label5 = ttk.Label(self.root, text='Time to send (format hh-mm) 24* :')
        label5.config(font=('helvetica', 10))
        self.canvas1.create_window(100, 220, window=label5)

        entry1 = ttk.Entry(self.root)
        self.canvas1.create_window(310, 100, window=entry1)

        entry2 = ttk.Entry(self.root)
        self.canvas1.create_window(310, 140, window=entry2)

        entry3 = ttk.Entry(self.root)
        self.canvas1.create_window(310, 180, window=entry3)

        entry4 = ttk.Entry(self.root)
        self.canvas1.create_window(310, 220, window=entry4)

        def tmsg():
            self.msg = entry1.get()
            self.time = entry4.get()
            self.iterate = entry3.get()
            self.name = entry2.get()
            label9 = ttk.Label(self.root, text=f"Reciver: {self.name} \nMessage: {self.msg} \nTime: {self.time}")
            self.canvas1.create_window(250, 350, window=label9)
            self.settimeMessages()

        def rmsg():
            self.msg = entry1.get()
            self.time = entry4.get()
            self.iterate = entry3.get()
            self.name = entry2.get()
            self.repMessages()
            label0 = ttk.Label(self.root, text=f"Reciver: {self.name} \nMessage: {self.msg} \nTime: {self.time}")
            self.canvas1.create_window(250, 350, window=label0)

        button1 = ttk.Button(text='Repeated Message', command=rmsg)
        self.canvas1.create_window(100, 450, window=button1)

        button1 = ttk.Button(text='Timed Message', command=tmsg)
        self.canvas1.create_window(400, 450, window=button1)

        self.root.mainloop()

#GUI program ends

    def settimeMessages(self):
        try:
            global launched
            global driver
            name=self.name
            messages=self.msg
            iteration=int(self.iterate)
            settime=self.time
            nowtimeHour,minute=datetime.datetime.now().hour,datetime.datetime.now().minute
            print(nowtimeHour,minute)
            nowinsecond=(nowtimeHour*60**2)+(minute*60)
            print(nowinsecond)
            assignedHour,assignedminute=int(settime[:2]),int(settime[3:])
            assignedinseconds=(assignedHour*60**2)+(assignedminute*60)
            print(assignedinseconds)
            whensend=assignedinseconds-nowinsecond
            print(type(whensend), whensend)
            time.sleep(whensend)
        except Exception as e:
            label9 = ttk.Label(self.root, text=e)
            self.canvas1.create_window(300, 400, window=label9)

        if launched==False:
            driver=webdriver.Chrome("chromedriver.exe")
            #driver.maximize_window()
            driver.get("https://web.whatsapp.com/")
            # driver objuct loads web.whatsapp.com
            time.sleep(5)
            launched=True
        pointingname = driver.find_element_by_xpath('//span[@title="{}"]'.format(name)).click()
        text_box = driver.find_element_by_class_name("p3_M1")

        for i in range(iteration):
            time.sleep(2)
            text_box.send_keys(messages)
            time.sleep(2)
            text_box.send_keys(Keys.ENTER)
        exit()


    def repMessages(self):
        global launched,driver
        name=self.name
        messages=self.msg
        iteration=int(self.iterate)
        if launched==False:
            driver=webdriver.Chrome("chromedriver.exe")
            #driver.maximize_window()
            driver.get("https://web.whatsapp.com/")
            # driver objuct loads web.whatsapp.com
            time.sleep(5)
            launched=True
        pointingname=driver.find_element_by_xpath('//span[@title="{}"]'.format(name)).click()
        text_box=driver.find_element_by_class_name("p3_M1")

        for i in range(iteration):
            time.sleep(2)
            text_box.send_keys(messages)
            time.sleep(2)
            text_box.send_keys(Keys.ENTER)
        exit()

#main function
if __name__ == '__main__':
    p=web()