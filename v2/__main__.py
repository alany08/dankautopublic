from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from random import randint as rand
from random import choice as choose
from bs4 import BeautifulSoup as soup
import requests
import re
import pyautogui
import string
from threading import Thread
import sys
from discord_webhook import DiscordWebhook as DH
from datetime import date
import datetime
import json

#Use dict for commands, timeouts, last run etc... while true check the each command, only run 1 each loop and sleep random at the end of loop. Detect if the command was "cooled down" or not

trivpath = "\\".join(__file__.split("\\")[0:-1]) + "\\trivia.json"

#email = input("Email: ")
#pwd = input("Password: ")

"""
try:
    if "me" in sys.argv[1]:
        me = True
    elif "rohit" in sys.argv[1]:
        me = False
except:
    me = True
"""

try:
    if sys.argv[1] == "alan":
        #my alts
        #Presaved comfig, New email/pwd
        #That's boredperson
        #email = "fisifi5756@wii999.com"
        email = "alanyu08+coinfarmeralt@gmail.com"
        pwd = "New Passcode"
        usekno = False
        useapple = True
        usepizza = False
        usespinner = True
        usecandy = True
        autosell = False
        serverindex = 0
        channelindex = 4
        loggingurl = "https://discord.com/api/webhooks/902771079519567963/YDk0JOwXEr1U1op-98268ByaSVT_bz7v4DhqvkIgPgHjRqGJhzGjviBy9RZGdRk-5vNZ"
        sleeptime = 10800
        chromepath = "C:\\Users\\ning\\Documents\\chromedriver.exe"
        keepawake = False
    elif sys.argv[1] == "wisdom":
        email="JeffLikesRoblox@gmail.com"
        pwd="LynbrookHighSchool!"
        usekno = False
        useapple = True
        usepizza = False
        usespinner = True
        usecandy = True
        autosell = False
        serverindex = 0
        channelindex = 5
        loggingurl = "https://discord.com/api/webhooks/903138699196366929/b3xkErARLmrm36kbWiEgtlpgUtvzzr5ezfOaakh87SLfZwmqgZ3mwqHFYfCgSf_4Cg1U"
        sleeptime = 10800
        chromepath = "C:\\Users\\wisdo\\OneDrive\\Documents\\chromedriver.exe"
        keepawake = True
    elif sys.argv[1] == "nathan":
        email = "dankmemerfarmNZ@gmail.com"
        pwd = "yesyes123yesyes"
        usekno = False
        useapple = True
        usepizza = False
        usespinner = True
        usecandy = True
        autosell = False
        serverindex = 1
        channelindex = 8
        loggingurl = "https://discord.com/api/webhooks/903132342376353802/_PAoAotn0rrveEU1UC8MTPcceppfJKXEpSYhHDK4EQPQo0hDyfZCq0emtnMc714FTN-a"
        sleeptime = 10800
        chromepath = "/Users/nathanzhao/Downloads/chromedriver"
        keepawake = True
    elif sys.argv[1] == "rohit":
        #Rohit's alt
        email = "tbob13574@gmail.com"
        pwd = "thisisalt"
        usekno = False
        useapple = True
        usepizza = False
        usespinner = True
        usecandy = True
        autosell = False
        serverindex = 0
        channelindex = 11
        loggingurl = "https://discord.com/api/webhooks/901862585756942376/UjIKVenNaeEi2Qs6ry98nrC_Bu1WSYApkbL0w4JcDSrvWUncFsl8Cslkcoyzz9ckd_I8"
        sleeptime = 10800
        chromepath = "\\"
        keepawake = True
    else:
        args = sys.argv
        args.pop(0)
        for arg in args:
            try:
                if "email" in arg:
                    email = arg.split("=")[1]
                elif "pass" in arg:
                    pwd = arg.split("=")[1]
                elif "usekno" in arg:
                    usekno = True
                elif "useapple" in arg:
                    useapple = True
                elif "usepizza" in arg:
                    usepizza = True
                elif "usespinner" in arg:
                    usespinner = True
                elif "usecandy" in arg:
                    usecandy = True
                elif "autosell" in arg:
                    autosell = True
                elif "serverindex" in arg:
                    serverindex = int(arg.split("=")[1])
                elif "channelindex" in arg:
                    channelindex = int(arg.split("=")[1])
                elif "loggingurl" in arg:
                    loggingurl = arg.split("=")[1]
                elif "sleeptime" in arg:
                    sleeptime = int(arg.split("=")[1])
                elif "chromepath" in arg:
                    chromepath = arg.split("=")[1]
                elif "keepawake" in arg:
                    keepawake = True
                else:
                    raise SyntaxError("Invalid arg")
            except:
                print("Invalid argument \"" + str(arg) + "\"")
                print("Required args: email, pass, serverindex, channelindex, chromepath")
                print("Example: python [file path] email=asdf@asdf.com pass=password serverindex=0 channelindex=0 chromepath=chromedriver.exe")
                print("Use the arguments usekno, useapple, usepizza, usespinner, usecandy, autosell to automatically use certain items")
                print("The arguments serverindex and channelindex are used to select the server and channel")
                print("The optional loggingurl argument is so you can make a discord webhook and have all the events logged there")
                sys.exit()

        try:
            email
        except:
            print("No email provided")
            print("Required args: email, pass, serverindex, channelindex, chromepath")
            print("Example: python [file path] email=asdf@asdf.com pass=password serverindex=0 channelindex=0 chromepath=chromedriver.exe")
            print("Use the arguments usekno, useapple, usepizza, usespinner, usecandy, autosell to automatically use certain items")
            print("The arguments serverindex and channelindex are used to select the server and channel")
            print("The optional loggingurl argument is so you can make a discord webhook and have all the events logged there")
            sys.exit()
        try:
            pwd
        except:
            print("No password provided")
            print("Required args: email, pass, serverindex, channelindex, chromepath")
            print("Example: python [file path] email=asdf@asdf.com pass=password serverindex=0 channelindex=0 chromepath=chromedriver.exe")
            print("Use the arguments usekno, useapple, usepizza, usespinner, usecandy, autosell to automatically use certain items")
            print("The arguments serverindex and channelindex are used to select the server and channel")
            print("The optional loggingurl argument is so you can make a discord webhook and have all the events logged there")
            sys.exit()
        try:
            usekno
        except:
            usekno = False
        try:
            useapple
        except:
            useapple = False
        try:
            usepizza
        except:
            usepizza = False
        try:
            usespinner
        except:
            usespinner = False
        try:
            usecandy
        except:
            usecandy = False
        try:
            autosell
        except:
            autosell = False
        try:
            serverindex
        except:
            print("No serverindex provided")
            print("Required args: email, pass, serverindex, channelindex, chromepath")
            print("Example: python [file path] email=asdf@asdf.com pass=password serverindex=0 channelindex=0 chromepath=chromedriver.exe")
            print("Use the arguments usekno, useapple, usepizza, usespinner, usecandy, autosell to automatically use certain items")
            print("The arguments serverindex and channelindex are used to select the server and channel")
            print("The optional loggingurl argument is so you can make a discord webhook and have all the events logged there")
            sys.exit()
        try:
            channelindex
        except:
            print("No channelindex provided")
            print("Required args: email, pass, serverindex, channelindex, chromepath")
            print("Example: python [file path] email=asdf@asdf.com pass=password serverindex=0 channelindex=0 chromepath=chromedriver.exe")
            print("Use the arguments usekno, useapple, usepizza, usespinner, usecandy, autosell to automatically use certain items")
            print("The arguments serverindex and channelindex are used to select the server and channel")
            print("The optional loggingurl argument is so you can make a discord webhook and have all the events logged there")
            sys.exit()
        try:
            loggingurl
        except:
            loggingurl = None
        try:
            sleeptime
        except:
            sleeptime = 10800
        try:
            chromepath
        except:
            print("No chromepath provided")
            print("Required args: email, pass, serverindex, channelindex, chromepath")
            print("Example: python [file path] email=asdf@asdf.com pass=password serverindex=0 channelindex=0 chromepath=chromedriver.exe")
            print("Use the arguments usekno, useapple, usepizza, usespinner, usecandy, autosell to automatically use certain items")
            print("The arguments serverindex and channelindex are used to select the server and channel")
            print("The optional loggingurl argument is so you can make a discord webhook and have all the events logged there")
            sys.exit()
        try:
            keepawake
        except:
            keepawake = False
except:
    print("No arguments provided")
    print("Required args: email, pass, serverindex, channelindex, chromepath")
    print("Example: python [file path] email=asdf@asdf.com pass=password serverindex=0 channelindex=0 chromepath=chromedriver.exe")
    print("Use the arguments usekno, useapple, usepizza, usespinner, usecandy, autosell to automatically use certain items")
    print("The arguments serverindex and channelindex are used to select the server and channel")
    print("The optional loggingurl argument is so you can make a discord webhook and have all the events logged there")
    sys.exit()

if keepawake:
    #Don't let computer turn off
    def keepawake():
        while True:
            print("Keep awake movements initiated")
            for i in range(0, 10):
                pyautogui.move(rand(-10, 10), rand(-10, 10))
                pyautogui.press("shift")
            print("Keep awake movements stopped")
            #print("Clicking random buttons just in case any were missed...")
            #for i in range(0, 3):
            #    choosebutton()
            time.sleep(180)

    Thread(target=keepawake, daemon=True).start()

pyautogui.FAILSAFE = False

if not loggingurl == None:
    _print = print

    def newprint_t(text, nowebhook = False):
        text = str(text)
        today = date.today()
        d = today.strftime("%m/%d/%Y")
        t = time.localtime()
        ms = str(time.time()).split(".")[1]
        t_now = str(t.tm_hour).zfill(2) + ":" + str(t.tm_min).zfill(2) + ":" + str(t.tm_sec).zfill(2) + "." + ms
        _print("[" + t_now + " - " + d + "] " + text)
        if not nowebhook:
            try:
                code = DH(url = loggingurl, content = "`[" + t_now + " - " + d + "] " + text + "`", rate_limit_retry=True).execute().status_code
                if not code == 200:
                    _print("Ratelimited, skipping log...")
            except:
                _print("Ratelimited, skipping log...")

    def newprint(text, nowebhook = False):
        Thread(target=newprint_t, args=(text, nowebhook), daemon=True).start()

    print = newprint
else:
    _print = print

    def newprint_t(text, nowebhook = False):
        text = str(text)
        today = date.today()
        d = today.strftime("%m/%d/%Y")
        t = time.localtime()
        ms = str(time.time()).split(".")[1]
        t_now = str(t.tm_hour).zfill(2) + ":" + str(t.tm_min).zfill(2) + ":" + str(t.tm_sec).zfill(2) + "." + ms
        _print("[" + t_now + " - " + d + "] " + text)

    def newprint(text, nowebhook = False):
        Thread(target=newprint_t, args=(text, nowebhook), daemon=True).start()

    print = newprint

def send(msg):
    for i in range(0, 30):
        try:
            for char in msg + "\n":
                while True:
                    try:
                        driver.find_elements_by_class_name("slateTextArea-1Mkdgw")[0].send_keys(char)
                        time.sleep(rand(10, 60)/10000)
                        break
                    except:
                        pass
            break
        except:
            print("Failed to send message")
        time.sleep(0.1)

def count(str, match):
    return len(list(re.finditer(match, str)))

def google(query):
    t = requests.get("http://google.com/search?q=" + query).text
    t = soup(t, "html.parser")
    t = t.find(id="main").text
    return t

def dotrivia():
    try:
        #Not that accurate
        #Stale element? IDK why...
        starttime = time.time()
        while True:
            if not (time.time() - starttime > 10):
                try:
                    question = driver.find_elements_by_class_name("embedDescription-1Cuq9a")[-1].find_elements_by_tag_name("strong")[0].text
                    break
                except:
                    pass
            else:
                choosebutton()
                raise ValueError("Stale element, timed out waiting...")
        btns = driver.find_elements_by_class_name("children-2goeSq")[-1]
        btns = btns.find_elements_by_class_name("component-1IAYeC")
        options = []
        for btn in btns:
            options.append([btn.text.lower(), btn])
        try:
            print("Checking database for trivia answers...")
            f = open(trivpath, "r", encoding="utf-8")
            database = json.load(f)
            f.close()
            ans = database[question.lower()]
            print("Answer found: " + ans)
            for opt in options:
                if opt[0] == ans:
                    opt[1].click()
                    return
            #Answer is invalid if not returned yet
            print("Database error, invalid option. Fixing...")
            database.pop(question.lower())
            f = open(trivpath, "w", encoding="utf-8")
            json.dump(database, f, indent=4)
            f.close()
        except KeyError:
            print("Not in database")
        results = google(question)
        results = results.lower()
        results = results.translate(str.maketrans("", "", string.punctuation))
        most_popular = [["filler", "element"], 0]
        for option in options:
            tempcount = 0
            for word in option[0].split(" "):
                tempcount = tempcount + count(results, word.translate(str.maketrans("", "", string.punctuation)))
            if tempcount > most_popular[1]:
                most_popular = [option, tempcount]
        if not most_popular[1] == 0:
            print("Answer for question \"" + question + "\" is \"" + most_popular[0][0] + "\" with token match count " + str(most_popular[1]))
            for i in range(0, 30):
                try:
                    most_popular[0][1].click()
                    break
                except:
                    pass
                time.sleep(0.1)
        else:
            print("Couldn't find answer for question \"" + question + "\"")
            choosebutton()
        starttime = time.time()
        while True:
            #Don't dwell here if there's no response
            if not (time.time() - starttime > 10):
                #Refresh just incase trivia hasn't been revealed yet
                #Stale element? IDK why...
                starttime2 = time.time()
                while True:
                    if not (time.time() - starttime2 > 10):
                        try:
                            question = driver.find_elements_by_class_name("embedDescription-1Cuq9a")[-1].find_elements_by_tag_name("strong")[0].text
                            break
                        except:
                            pass
                    else:
                        choosebutton()
                        raise ValueError("Stale element, timed out waiting...")
                latestbtn = driver.find_elements_by_class_name("children-2goeSq")[-1]
                finds = latestbtn.find_elements_by_class_name("colorGreen-29iAKY")
                if not finds == []:
                    print("Answer to trivia revealed")
                    break
            else:
                print("Timed out waiting for answer")
                return
        f = open(trivpath, "r", encoding="utf-8")
        all_q = json.load(f)
        f.close()
        #Eh just keep this here
        ans = latestbtn.find_elements_by_class_name("colorGreen-29iAKY")[-1]
        ans = ans.text.lower()
        print("Correct answer is \"" + ans + "\"")
        all_q.update({question.lower(): ans})
        f = open(trivpath, "w", encoding="utf-8")
        json.dump(all_q, f, indent=4)
        f.close()
    except Exception as e:
        print("ERROR IN TRIVIA: \n" + str(e))
        choosebutton()

def checkdragon():
    #This would be the actual message container's child nodes, including the padding and dragon location
    #document.querySelector('[data-list-item-id="chat-messages___chat-messages-900881479284977664"]').childNodes[0].childNodes[2].childNodes
    #This would be the 3 buttons in order from left to right
    #document.querySelector('[data-list-item-id="chat-messages___chat-messages-900881479284977664"]').childNodes[1].childNodes[0].childNodes[0].childNodes[0].childNodes
    #All are assuming the message id etc etc. Use a different selector, but still select the "same" element
    """for the sake of something"""
    latest = driver.find_elements_by_class_name("messageContent-2qWWxC")[-1]
    if "fireball" in latest.text.lower():
        print("DRAGON DETECTED")
        try:
            print("Waiting for text change...")
            oldtext = latest.text.lower()
            starttime = time.time()
            while True:
                if not (time.time() - starttime > 10):
                    if not oldtext == latest.text.lower():
                        print("Fireball moved, continuing")
                        break
                else:
                    print("Timed out waiting for fireball to move")
                    break
            #Returning blanks?
            #prespace = latest.find_elements_by_css_selector("*")[3].text
            identifier = latest.get_property("id")
            text = driver.execute_script("return document.getElementById('" + identifier + "').innerText")
            prespace = text.split("\n")[2]
            print("Padding/prespace length: " + str(len(prespace)))
            #The functions that find by xpath returns a list, just use indicies zero or some other way/different function
            btns = latest.find_elements_by_xpath("..")[0].find_elements_by_xpath("..")[0].find_elements_by_class_name("children-2goeSq")[0].find_elements_by_tag_name("button")
            if prespace == "":
                #It's at the very left
                print("Fireball at left")
                btns[2].click()
            elif prespace == "              ":
                #Very right
                btns[0].click()
                print("Fireball at right")
            else:
                #Probably middle
                print("Fireball at middle")
                if rand(0, 1) == 1:
                    btns[0].click()
                else:
                    btns[2].click()
        except Exception as e:
            print("ERROR CLICKING BUTTON:\n" + str(e))
            choosebutton()
    else:
        print("NO DRAGON")

def checkfish():
    latest = driver.find_elements_by_class_name("messageContent-2qWWxC")[-1]
    if "catch the fish" in latest.text.lower():
        print("FISH DETECTED")
        try:
            oldtext = latest.text.lower()
            print("Waiting for text change...")
            starttime = time.time()
            while True:
                if not (time.time() - starttime > 10):
                    if not oldtext == latest.text.lower():
                        print("Fish moved, continuing...")
                        break
                else:
                    print("Timed out waiting for fish to move")
                    break
            #List index outta range for one of these, no need for the childnode, just use latest.text
            #print(latest.find_elements_by_css_selector("*")[0].text)
            #prespace = latest.find_elements_by_css_selector("*")[0].text.split("\n")[1]
            #print("\"" + latest.text + "\"")
            #prespace = latest.text.split("\n")[1]
            #document.querySelectorAll(".messageContent-2qWWxC")[37].innerText
            #Screw that use JavaScript
            identifier = latest.get_property("id")
            text = driver.execute_script("return document.getElementById('" + identifier + "').innerText")
            prespace = text.split("\n")[1]
            print("Padding/prespace length: " + str(len(prespace)))
            btns = latest.find_elements_by_xpath("..")[0].find_elements_by_xpath("..")[0].find_elements_by_class_name("children-2goeSq")[0].find_elements_by_tag_name("button")
            if prespace == "              ":
                print("Fish at right")
                btns[2].click()
            elif prespace == "":
                print("Fish at left")
                btns[0].click()
            else:
                print("Fish in middle")
                btns[1].click()
        except Exception as e:
            print("ERROR CLICKING BUTTON:\n" + str(e))
            choosebutton()
    else:
        print("NO FISH")

def sellsomething():
    global autosell
    if autosell:
        send("pls sell " + choose(["cookie", "duck", "boar", "skunk", "junk", "trash", "jellyfish", "garbage", "deer", "seaweed", "sand", "exoticfish", "bread", "rarefish", "rabbit", "stick", "ladybug", "worm", "ant"]) + " all")

def choosebutton():
    for i in range(0, 30):
        try:
            driver.find_elements_by_class_name("secondaryButton-BIo-2g")[0].click()
        except:
            pass
        try:
            parent = driver.find_elements_by_class_name("children-2goeSq")[-1]
            choose(parent.find_elements_by_tag_name("button")).click()
            break
        except:
            print("No buttons to click", nowebhook = True)
            try:
                driver.find_elements_by_class_name("secondaryButton-BIo-2g")[0].click()
            except:
                pass
        time.sleep(0.1)

def deposit():
    send("pls dep all")
    time.sleep(rand(200, 500)/100)

def highlow():
    try:
        parent = driver.find_elements_by_css_selector(".embedMargin-UO5XwE.embedDescription-1Cuq9a")[-1]
        prompt = int(parent.find_elements_by_tag_name("strong")[0].text)
        parent = driver.find_elements_by_class_name("children-2goeSq")[-1]
        buttons = parent.find_elements_by_tag_name("button")
        time.sleep(rand(100, 150)/100)
        print("Prompt number for highlow: " + str(prompt))
        if prompt < 45+rand(-5, 5):
            buttons[2].click()
            print("Higher")
        elif prompt > 55+rand(-5, 5):
            buttons[0].click()
            print("Lower")
        else:
            buttons[1].click()
            print("Jackpot!")
    except:
        choosebutton()


driver = webdriver.Chrome(chromepath)

driver.get("https://discord.com/app")

while True:
    try:
        driver.find_element_by_name("email").send_keys(email + "\t")
        time.sleep(rand(0, 100)/100)
        driver.find_element_by_name("password").send_keys(pwd + "\n")
        break
    except:
        print("Could not find elements", nowebhook = True)
    time.sleep(0.1)

time.sleep(1)

captcha = False

while True:
    try:
        try:
            driver.find_elements_by_css_selector('[role="treeitem"]')[serverindex].click()
        except:
            driver.find_element_by_css_selector('[aria-label="Close"]').click()
            time.sleep(rand(0, 100)/100)
            driver.find_elements_by_css_selector('[role="treeitem"]')[serverindex].click()
        break
    except:
        try:
            if not captcha:
                captchaframe = driver.find_elements_by_css_selector('[title="widget containing checkbox for hCaptcha security challenge"]')[0]
                driver.switch_to.frame(captchaframe)
                driver.find_elements_by_css_selector("#anchor-tc")[0].click()
                driver.switch_to.default_content()
                print("Solve captcha plz I'm a dumb bot and I can't solve it...")
                captcha = True
        except Exception as e:
            print("Could not select server", nowebhook = True)
    time.sleep(0.1)

time.sleep(1)

while True:
    try:
        driver.find_elements_by_class_name("channelName-2YrOjO")[channelindex].click()
        break
    except:
        print("Could not select channel", nowebhook = True)
    time.sleep(0.1)

time.sleep(1 + rand(0, 100)/100)

while True:
    try:
        #Always switch to a random command,
        #depdending on how much time is left in their timeout.
        #Also set an inacurracy, like if the delta is neglible, then select random.
        #I don't care if the cooldown warning occurs.
        #Keep a list of the cooldowns for each command!

        send("pls use horseshoe")
        time.sleep(rand(100, 150)/100)

        send("pls hunt")
        time.sleep(rand(150, 200)/100)
        checkdragon()
        time.sleep(rand(100, 150)/100)

        send("pls fish")
        time.sleep(rand(150, 200)/100)
        checkfish()
        time.sleep(rand(100, 150)/100)

        send("pls dig")
        time.sleep(rand(100, 150)/100)

        if useapple:
            send("pls use apple")
            time.sleep(rand(100, 150)/100)

        deposit()

        send("pls search")
        time.sleep(rand(250, 350)/100)
        choosebutton()
        time.sleep(rand(100, 150)/100)

        sellsomething()
        time.sleep(rand(100, 150)/100)

        if usespinner:
            send("pls use spinner")
            time.sleep(rand(100, 150)/100)

        send("pls pm")
        time.sleep(rand(250, 350)/100)
        choosebutton()
        time.sleep(rand(100, 150)/100)

        send("pls beg")
        time.sleep(rand(100, 150)/100)

        if usepizza:
            send("pls use pizza")
            time.sleep(rand(100, 150)/100)

        deposit()

        send("pls crime")
        time.sleep(rand(250, 350)/100)
        choosebutton()
        time.sleep(rand(100, 150)/100)

        sellsomething()
        time.sleep(rand(100, 150)/100)

        send("pls hl")
        time.sleep(rand(100, 150)/100)
        highlow()
        time.sleep(rand(100, 150)/100)

        if usecandy:
            send("pls use candy")
            time.sleep(rand(100, 150)/100)

        send("pls trivia")
        #time.sleep(rand(200, 300)/100)
        time.sleep(rand(250, 350)/100)
        #Actually search for answers DONE!!
        #choosebutton()
        dotrivia()
        time.sleep(rand(100, 150)/100)

        #Only run once a day, with some inaccuracies. Maybe include 1 day in the cooldowns?
        send("pls daily")
        time.sleep(rand(100, 150)/100)

        if usekno:
            send("pls use kno")
            time.sleep(rand(100, 150)/100)

        sellsomething()
        time.sleep(rand(100, 150)/100)

        deposit()

        print("Clicking button just in case any were missed...")
        choosebutton()

        p = rand(30, 60)
        print("TIMEOUT " + str(p) + "...")
        time.sleep(p)
        print("TIMEOUT END")

        if rand(0, 10) == 1:
            p = rand(60, 600)
            print("PAUSING " + str(p) + "...")
            time.sleep(p)
            print("PAUSE END")
        #Less random AFK times, maybe fuzzy numbers around certain hours? DONE
        h = time.localtime().tm_hour
        m = time.localtime().tm_min
        s = time.localtime().tm_sec
        sec_of_day = s + m*60 + h*60*60
        if ((sec_of_day > (sleeptime + rand(-3600, 3600))) and (sec_of_day < (sleeptime + rand(-3600, 3600)))) or ((sec_of_day < (sleeptime + rand(-3600, 3600))) and (sec_of_day > (sleeptime + rand(-3600, 3600)))):
            p = rand(10800, 14400)
            print("AFK (SLEEPING...)" + str(p) + "...")
            time.sleep(p)
            print("AFK (SLEEP) END")
    except KeyboardInterrupt:
        print("Exiting...")
        sys.exit()
    except Exception as e:
        print("ERROR:\n" + str(e))