from selenium import webdriver
import time
import datetime
import os
from playsound import playsound
from notify_run import Notify
notify = Notify()



os.system("cls")

def register():
    return notify.register()
    

def info():
    return notify.info()

def convert(seconds): 
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds) 

def beep(status):
    if status == "online":
        playsound('res/online1.mp3')
    else:
        playsound('res/Beep.mp3')

try:
    wd = webdriver.Chrome('chromedriver.exe')
    print("ok")
except Exception as e:
    print(e)
    print("\n\n\nyou have a error of chromedriver selenium so download chomedriver form here and put in this folder\nhttp://chromedriver.chromium.org/downloads")
    exit()



view = input("this for notification on you phone if you use old url then [N] and if you make new url then [Y] \nyou want to register new notify[y/n]: ")

if view == 'Y' or view == 'y':
    rt = register()
else:
    rt = info()

print(rt)
url = "https://web.whatsapp.com/"

wd.get(url)

input("enter any key")
print("warning: id you enter the name and you don't have a open that chat then after open a \"one more waring\" then you manully open that profile. ")
wd.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]").click()
user = input("enter name :\n")
wd.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]").send_keys(user)

time.sleep(1)
name = wd.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[4]/div/div/div[2]/div[1]/div/span/span/span").text
print("if my program is not open your perfer program then now open maully in this browser and this tab")
if name.lower() == user:
    print("match")
    wd.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[4]/div/div/div[2]/div[1]/div/span/span/span").click()
    s="stop"
    while True:
        try:
            status = wd.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/header/div[2]/div[2]/span").text
            if status=="online":
                if s=="stop":
                    s="start"
                    ini = time.time()
                    print("online")
                    notify.send(name +" is online")
                    beep("online")

        except:
            if s == "start":
                s="stop"
                t = time.time()-ini
                rt = convert(t)
                beep("offline")
                notify.send(name +" is offline now.online duration is "+ rt)
                print("this number is offline now. \nonline duration is ",rt)
        time.sleep(1)