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
from numpy.random import gamma
from random import shuffle
from selenium.webdriver.chrome.options import Options
import webbrowser
import ctypes
import traceback
import gc

#Garbage collector??
gc.enable()

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
#Fuzziness calculation
def gendiff(cooldown):
    if cooldown < 500:
        if rand(0, 5) == 1:
            return -gamma(cooldown/60, cooldown/(cooldown-(cooldown/1.2)))
        else:
            return gamma(cooldown/60, cooldown/(cooldown-(cooldown/1.2)))
    elif cooldown >= 500 and cooldown < 1000:
        if rand(0, 5) == 1:
            return -gamma(cooldown/75, cooldown/(cooldown-(cooldown/3)))
        else:
            return gamma(cooldown/75, cooldown/(cooldown-(cooldown/3)))
    elif cooldown >= 1000 and cooldown < 10000:
        if rand(0, 5) == 1:
            return -gamma(cooldown/90, cooldown/(cooldown-(cooldown/5)))
        else:
            return gamma(cooldown/90, cooldown/(cooldown-(cooldown/5)))
    elif cooldown >= 10000 and cooldown < 100000:
        if rand(0, 5) == 1:
            return -gamma(cooldown/250, cooldown/(cooldown-(cooldown/1.1)))
        else:
            return gamma(cooldown/250, cooldown/(cooldown-(cooldown/1.1)))

global_weblogging_enabeled = False

try:
    elif sys.argv[1] == "your preset name as the program argument":
        token = "Your discord account token"
        start_url = "Channel url to start in"
        usekno = #Automatically use these corresponding items (bool)
        useapple = #Automatically use these corresponding items (bool)
        usepizza = #Automatically use these corresponding items (bool)
        usespinner = #Automatically use these corresponding items (bool)
        usecandy = #Automatically use these corresponding items (bool)
        autosell = #Automatically use these corresponding items (bool)
        usepod = #Automatically use these corresponding items (bool)
        loggingurl = "Webook to send logs to"
        sleeptime = #Amount of time to pause (int) at around 2am
        chromepath = "Path to chrome driver"
        keepawake = #Keep the computer on or not (bool)
except:
    print("No arguments provided")
    print("Required args: email, pass, serverindex, channelindex, chromepath")
    print("Example: python [file path] email=asdf@asdf.com pass=password serverindex=0 channelindex=0 chromepath=chromedriver.exe")
    print("Use the arguments usekno, useapple, usepizza, usespinner, usecandy, autosell to automatically use certain items")
    print("The arguments serverindex and channelindex are used to select the server and channel")
    print("The optional loggingurl argument is so you can make a discord webhook and have all the events logged there")
    sys.exit()

pyautogui.FAILSAFE = False

if keepawake:
    #Don't let computer turn off
    ctypes.windll.kernel32.SetThreadExecutionState(0x80000041)

if not loggingurl == None:
    _print = print

    def newprint_t(text, nowebhook = False, override = False):
        global global_weblogging_enabeled
        text = str(text)
        today = date.today()
        d = today.strftime("%m/%d/%Y")
        t = time.localtime()
        ms = str(time.time()).split(".")[1]
        t_now = str(t.tm_hour).zfill(2) + ":" + str(t.tm_min).zfill(2) + ":" + str(t.tm_sec).zfill(2) + "." + ms
        _print("[" + t_now + " - " + d + "] " + text)
        if ((not nowebhook) and global_weblogging_enabeled) or override:
            try:
                #Don't retry or else ip ban
                code = DH(url = loggingurl, content = "`[" + t_now + " - " + d + "] " + text + "`", rate_limit_retry=False).execute().status_code
                if not code == 200:
                    _print("Ratelimited, skipping log...")
            except:
                _print("Ratelimited, skipping log...")

    def newprint(text, nowebhook = False, override = False):
        Thread(target=newprint_t, args=(text, nowebhook, override), daemon=True).start()

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
                        driver.find_elements_by_class_name("slateTextArea-27tjG0")[0].send_keys(char)
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
                    question = driver.find_elements_by_class_name("embedDescription-1DrJxZ")[-1].find_elements_by_tag_name("strong")[0].text
                    break
                except:
                    pass
            else:
                choosebutton()
                raise ValueError("Stale element, timed out waiting...")
        print("Question: " + question)
        btns = driver.find_elements_by_class_name("children-2XdE_I")[-1]
        btns = btns.find_elements_by_class_name("component-ifCTxY")
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
            print("Database error, invalid option. Fixing...", override = True)
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
                            question = driver.find_elements_by_class_name("embedDescription-1DrJxZ")[-1].find_elements_by_tag_name("strong")[0].text
                            break
                        except:
                            pass
                    else:
                        choosebutton()
                        raise ValueError("Stale element, timed out waiting...")
                latestbtn = driver.find_elements_by_class_name("children-2XdE_I")[-1]
                finds = latestbtn.find_elements_by_class_name("colorGreen-3y-Z79")
                if not finds == []:
                    print("Answer to trivia revealed")
                    break
            else:
                print("Timed out waiting for answer", override = True)
                return
        f = open(trivpath, "r", encoding="utf-8")
        all_q = json.load(f)
        f.close()
        #Eh just keep this here
        ans = latestbtn.find_elements_by_class_name("colorGreen-3y-Z79")[-1]
        ans = ans.text.lower()
        print("Correct answer is \"" + ans + "\"")
        all_q.update({question.lower(): ans})
        f = open(trivpath, "w", encoding="utf-8")
        json.dump(all_q, f, indent=4)
        f.close()
    except Exception as e:
        e = "".join(traceback.format_exception(type(e), e, e.__traceback__))
        print("ERROR IN TRIVIA: \n" + str(e), override = True)
        choosebutton()

def checkdragon():
    orig = time.time()
    while True:
        if not time.time() - orig > 5:
            try:
                #This would be the actual message container's child nodes, including the padding and dragon location
                #document.querySelector('[data-list-item-id="chat-messages___chat-messages-900881479284977664"]').childNodes[0].childNodes[2].childNodes
                #This would be the 3 buttons in order from left to right
                #document.querySelector('[data-list-item-id="chat-messages___chat-messages-900881479284977664"]').childNodes[1].childNodes[0].childNodes[0].childNodes[0].childNodes
                #All are assuming the message id etc etc. Use a different selector, but still select the "same" element
                """for the sake of something"""
                latest = driver.find_elements_by_class_name("messageContent-2t3eCI")[-1]
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
                        btns = latest.find_elements_by_xpath("..")[0].find_elements_by_xpath("..")[0].find_elements_by_class_name("children-2XdE_I")[0].find_elements_by_tag_name("button")
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
                        e = "".join(traceback.format_exception(type(e), e, e.__traceback__))
                        print("ERROR CLICKING BUTTON:\n" + str(e), override = True)
                        choosebutton()
                else:
                    print("NO DRAGON")
                break
            except KeyboardInterrupt:
                sys.exit()
            except Exception as e:
                e = "".join(traceback.format_exception(type(e), e, e.__traceback__))
                print("Error in checkdragon: " + str(e), override = True)
        else:
            print("Timed out waiting for stale element to be reattatched...", override = True)
            break

def checkfish():
    orig = time.time()
    while True:
        if not time.time() - orig > 5:
            try:
                latest = driver.find_elements_by_class_name("messageContent-2t3eCI")[-1]
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
                        #document.querySelectorAll(".messageContent-2t3eCI")[37].innerText
                        #Screw that use JavaScript
                        identifier = latest.get_property("id")
                        text = driver.execute_script("return document.getElementById('" + identifier + "').innerText")
                        prespace = text.split("\n")[1]
                        print("Padding/prespace length: " + str(len(prespace)))
                        btns = latest.find_elements_by_xpath("..")[0].find_elements_by_xpath("..")[0].find_elements_by_class_name("children-2XdE_I")[0].find_elements_by_tag_name("button")
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
                        e = "".join(traceback.format_exception(type(e), e, e.__traceback__))
                        print("ERROR CLICKING BUTTON:\n" + str(e), override = True)
                        choosebutton()
                else:
                    print("NO FISH")
                break
            except KeyboardInterrupt:
                sys.exit()
            except Exception as e:
                e = "".join(traceback.format_exception(type(e), e, e.__traceback__))
                print("Error in checkfish: " + str(e), override = True)
        else:
            print("Timed out waiting for stale element to be reattatched...", override = True)
            break

def checkdig():
    orig = time.time()
    while True:
        if not time.time() - orig > 5:
            try:
                latest = driver.find_elements_by_class_name("messageContent-2t3eCI")[-1]
                latest_id = latest.get_attribute("id")
                if "remember words" in latest.text.lower():
                    #Remember the words
                    print("Remember the words minigame!")
                    words = latest.find_elements_by_css_selector("code")
                    words_parsed = []
                    for word in words:
                        words_parsed.append(word.text)
                    print("Words are: " + str(words_parsed))
                    old_txt = latest.text
                    starttime = time.time()
                    while True:
                        if not (time.time() - starttime) > 15:
                            latest = driver.find_element_by_id(latest_id)
                            if not latest.text == old_txt:
                                break
                        else:
                            print("Timed out waiting for text change...")
                            break
                    time.sleep(rand(500, 1500)/1000)
                    buttons = driver.find_elements_by_class_name("children-2XdE_I")[-1]
                    buttons = buttons.find_elements_by_css_selector("button")
                    btns = {}
                    for button in buttons:
                        btns.update({
                            button.text: buttons.index(button)
                        })
                    print("Buttons appeared: " + str(btns))
                    for word in words_parsed:
                        driver.find_elements_by_class_name("children-2XdE_I")[-1].find_elements_by_css_selector("button")[btns[word]].click()
                        print(word + " Clicked!", nowebhook = True)
                        time.sleep(rand(3500, 6000)/1000)
                elif "hit the ball" in latest.text.lower():
                    #Score the soccer ball
                    print("Soccer ball minigame!")
                    try:
                        print("Waiting for text change...")
                        oldtext = latest.text.lower()
                        starttime = time.time()
                        while True:
                            if not (time.time() - starttime > 10):
                                if not oldtext == latest.text.lower():
                                    print("Person moved, continuing")
                                    break
                            else:
                                print("Timed out waiting for person to move")
                                break
                        prespace = driver.execute_script("return document.querySelector('#" + latest_id + "').childNodes[4].textContent")
                        prespace = prespace.replace("\n", "")
                        print("Padding/prespace length: " + str(len(prespace)))
                        #The functions that find by xpath returns a list, just use indicies zero or some other way/different function
                        btns = latest.find_elements_by_xpath("..")[0].find_elements_by_xpath("..")[0].find_elements_by_class_name("children-2XdE_I")[0].find_elements_by_tag_name("button")
                        if prespace == "":
                            #It's at the very left
                            print("Soccerball at left")
                            btns[2].click()
                        elif prespace == "              ":
                            #At right
                            print("Soccerball at right")
                            btns[0].click()
                        else:
                            #Probably middle
                            print("Soccerball at middle")
                            if rand(0, 1) == 1:
                                btns[0].click()
                            else:
                                btns[2].click()
                    except Exception as e:
                        e = "".join(traceback.format_exception(type(e), e, e.__traceback__))
                        print("ERROR CLICKING BUTTON:\n" + str(e), override = True)
                        choosebutton()
                elif "dunk the ball" in latest.text.lower():
                    #Score the basketball thingy
                    print("Dunk the ball minigame!")
                    try:
                        oldtext = latest.text.lower()
                        print("Waiting for text change...")
                        starttime = time.time()
                        while True:
                            if not (time.time() - starttime > 10):
                                if not oldtext == latest.text.lower():
                                    print("Ball moved, continuing...")
                                    break
                            else:
                                print("Timed out waiting for ball to move")
                                break
                        prespace = driver.execute_script("return document.querySelector('#" + latest_id + "').childNodes[4].textContent")
                        prespace = prespace.replace("\n", "")
                        print("Padding/prespace length: " + str(len(prespace)))
                        btns = latest.find_elements_by_xpath("..")[0].find_elements_by_xpath("..")[0].find_elements_by_class_name("children-2XdE_I")[0].find_elements_by_tag_name("button")
                        if prespace == "              ":
                            print("Ball at right")
                            btns[2].click()
                        elif prespace == "":
                            print("Ball at left")
                            btns[0].click()
                        else:
                            print("Ball in middle")
                            btns[1].click()
                    except Exception as e:
                        e = "".join(traceback.format_exception(type(e), e, e.__traceback__))
                        print("ERROR CLICKING BUTTON:\n" + str(e), override = True)
                        choosebutton()
                else:
                    print("Nothing special for dig/unrecognized minigame", nowebhook = True)
                break
            except KeyboardInterrupt:
                sys.exit()
            except Exception as e:
                e = "".join(traceback.format_exception(type(e), e, e.__traceback__))
                print("Error in checkdig: " + str(e), override = True)
        else:
            print("Timed out waiting for stale element to be reattatched...", override = True)
            break

def sellsomething():
    global autosell
    if autosell:
        send("pls sell " + choose(["cookie", "duck", "boar", "skunk", "junk", "trash", "jellyfish", "garbage", "deer", "seaweed", "sand", "exoticfish", "bread", "rarefish", "rabbit", "stick", "ladybug", "worm", "ant"]) + " all")

def choosebutton(retry = True):
    if retry:
        for i in range(0, 30):
            try:
                parent = driver.find_elements_by_class_name("children-2XdE_I")[-1]
                choose(parent.find_elements_by_tag_name("button")).click()
                break
            except:
                print("No buttons to click", nowebhook = True)
                break
            time.sleep(0.1)
    else:
        for i in range(0, 2):
            try:
                parent = driver.find_elements_by_class_name("children-2XdE_I")[-1]
                choose(parent.find_elements_by_tag_name("button")).click()
                break
            except:
                print("No buttons to click", nowebhook = True)
                break
            time.sleep(0.1)

def deposit():
    send("pls dep all")
    time.sleep(rand(500, 1000)/1000)

def highlow():
    try:
        parent = driver.find_elements_by_css_selector(".embedDescription-1DrJxZ.embedMargin-2PsaQ4")[-1]
        prompt = int(parent.find_elements_by_tag_name("strong")[0].text)
        parent = driver.find_elements_by_class_name("children-2XdE_I")[-1]
        buttons = parent.find_elements_by_tag_name("button")
        time.sleep(rand(1000, 1500)/1000)
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
    except Exception as e:
        e = "".join(traceback.format_exception(type(e), e, e.__traceback__))
        choosebutton()
        print("Highlow failed due to: " + str(e))

def checktimeout():
    try:
        latest = driver.find_elements_by_class_name("cozyMessage-1DWF9U")[-1]
        if "only need to wait" in latest.text.lower() or ("already claimed your daily" in latest.text.lower()) or "active right now" in latest.text.lower() or "dying from the tidepod you ate" in latest.text.lower():
            return True
        else:
            return False
    except:
        return False

def wait_reply(timeout = 5):
    starttime = time.time()
    while True:
        if time.time() - timeout < starttime:
            try:
                if driver.find_elements_by_class_name("username-h_Y3Us")[-1].text.lower() == "dank memer":
                    break
            except KeyboardInterrupt:
                sys.exit()
            except:
                pass
        else:
            print("Timed out waiting for bot reply", nowebhook = True)
            break
    print("Bot replied!", nowebhook = True)
    time.sleep(0.05)

def rm_command(cmd_name):
    global commands
    for i in range(0, len(commands)):
        if commands[i]["name"] == cmd_name:
            del commands[i]
            break

driver = None
def login():
    global driver
    global start_url
    chrome_port = rand(1024, 65535)
    options = Options()
    options.add_argument("--mute-audio")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--headless")
    options.add_argument('--log-level=3')
    options.add_argument('--remote-debugging-address=0.0.0.0')
    options.add_argument('--remote-debugging-port=' + str(chrome_port))
    print("Remote debugging port set to " + str(chrome_port), override = True)
    driver = webdriver.Chrome(chromepath, chrome_options=options)

    driver.get(start_url)

    #login with token doesn't have captcha 
    driver.execute_script("""
    let token = `""" + token + """`

    function login(token) {
        setInterval(() => {
          var frame = document.body.appendChild(document.createElement `iframe`);
          frame.contentWindow.localStorage.clear();
          frame.contentWindow.localStorage.token = `"` + token + `"`;
        }, 0);
        setTimeout(() => {
          location.reload();
        }, 100);
      }

    login(token);
    """)
login()

"""
#global captcha_cookie_url
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
                print("Solve captcha plz I'm a dumb bot and I can't solve it... (Open dev tools to see the headless browser, make sure to close it immediatley to give the control handles (?) back.)")
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
"""

time.sleep(1 + rand(0, 100)/100)

#Command functions
def useshoe():
    send("pls use horseshoe")

def hunt():
    send("pls hunt")
    #time.sleep(rand(150, 250)/100)
    wait_reply()
    checkdragon()

def fish():
    send("pls fish")
    #time.sleep(rand(150, 250)/100)
    wait_reply()
    checkfish()

def dig():
    send("pls dig")
    #time.sleep(rand(150, 250)/100)
    wait_reply()
    checkdig()

def apple():
    if useapple:
        send("pls use apple")

def search():
    deposit()
    wait_reply(timeout = 0.75)
    time.sleep(rand(10, 25)/100)
    send("pls search")
    #time.sleep(rand(100, 200)/100)
    wait_reply()
    time.sleep(rand(50, 100)/100)
    choosebutton()

def spinner():
    if usespinner:
        send("pls use spinner")

def meme():
    send("pls pm")
    #time.sleep(rand(100, 200)/100)
    wait_reply()
    time.sleep(rand(50, 100)/100)
    choosebutton()

def beg():
    send("pls beg")

def pizza():
    if usepizza:
        send("pls use pizza")

def crime():
    deposit()
    wait_reply(timeout = 0.75)
    time.sleep(rand(10, 25)/100)
    send("pls crime")
    #time.sleep(rand(100, 200)/100)
    wait_reply()
    time.sleep(rand(50, 100)/100)
    choosebutton()

def hl():
    send("pls hl")
    #time.sleep(rand(100, 150)/100)
    wait_reply()
    time.sleep(rand(100, 250)/100)
    highlow()

def candy():
    if usecandy:
        send("pls use candy")

def trivia():
    send("pls trivia")
    #time.sleep(rand(200, 300)/100)
    wait_reply()
    time.sleep(rand(500, 600)/100)
    #Actually search for answers DONE!!
    #choosebutton()
    dotrivia()

def daily():
    send("pls daily")

def kno():
    if usekno:
        send("pls use kno")

def pod():
    if usepod:
        send("pls use pod")
        #time.sleep(rand(250, 350)/100)
        wait_reply()
        time.sleep(rand(50, 100)/100)
        driver.find_elements_by_class_name("children-2XdE_I")[-1].find_elements_by_tag_name("button")[1].click()

commands = [
    {
        "name": "horseshoe",
        "func": useshoe,
        "timeout": 900,
        "lastrun": 0
    },
    {
        "name": "hunt",
        "func": hunt,
        "timeout": 40,
        "lastrun": 0
    },
    {
        "name": "fish",
        "func": fish,
        "timeout": 40,
        "lastrun": 0
    },
    {
        "name": "dig",
        "func": dig,
        "timeout": 40,
        "lastrun": 0
    },
    {
        "name": "apple",
        "func": apple,
        "timeout": 86400,
        "lastrun": 0
    },
    {
        "name": "search",
        "func": search,
        "timeout": 30,
        "lastrun": 0
    },
    {
        "name": "sell",
        "func": sellsomething,
        "timeout": 15,
        "lastrun": 0
    },
    {
        "name": "usespinner",
        "func": spinner,
        "timeout": 600,
        "lastrun": 0
    },
    {
        "name": "meme",
        "func": meme,
        "timeout": 40,
        "lastrun": 0
    },
    {
        "name": "beg",
        "func": beg,
        "timeout": 45,
        "lastrun": 0
    },
    {
        "name": "usepizza",
        "func": pizza,
        "timeout": 3600,
        "lastrun": 0
    },
    {
        "name": "crime",
        "func": crime,
        "timeout": 45,
        "lastrun": 0
    },
    {
        "name": "highlow",
        "func": hl,
        "timeout": 30,
        "lastrun": 0
    },
    {
        "name": "usecandy",
        "func": candy,
        "timeout": 30,
        "lastrun": 0
    },
    {
        "name": "trivia",
        "func": trivia,
        "timeout": 5,
        "lastrun": 0
    },
    {
        "name": "daily",
        "func": daily,
        "timeout": 86400,
        "lastrun": 0
    },
    {
        "name": "usekno",
        "func": kno,
        "timeout": 60,
        "lastrun": 0
    },
    {
        "name": "usepod",
        "func": pod,
        "timeout": 7200,
        "lastrun": 0
    }
]

#Remove them from list for efficiency
if not usekno:
    rm_command("usekno")
if not useapple:
    rm_command("apple")
if not usepizza:
    rm_command("usepizza")
if not usespinner:
    rm_command("usespinner")
if not usecandy:
    rm_command("usecandy")
if not autosell:
    rm_command("sell")
if not usepod:
    rm_command("usepod")

#The log func for command cooldown is y=log_{1.2}(x)-10 or -> just hardcode <-
    #Gamma distribution: numpy.random.gamma(5, 2*timeout) or something similar
#Log for fuzzy numbs
#At the end of running commands, break out of for loop, and continue
#Spare time/all commands cooled down = dep all
#If the command was "cooled-down" then do not set the last run epoch time to current time
while True:
    try:
        #Eh, so it isn't in any particular order
        shuffle(commands)
        rancommand = False
        for cmd in commands:
            inaccuracy = gendiff(cmd["timeout"])
            print("Command " + cmd["name"] + " generated inaccuracy " + str(inaccuracy) + " and last run at " + str(cmd["lastrun"]), nowebhook = True)
            if time.time() > (cmd["lastrun"] + cmd["timeout"] + inaccuracy):
                rancommand = True
                print("Executing command " + cmd["name"], nowebhook = True)
                cmd["func"]()
                #p = rand(250, 750)/1000
                #lets try this
                wait_reply(timeout = 1)
                time.sleep(rand(750, 1000)/1000)
                #print("SLEEP " + str(p) + "...", nowebhook = True)
                #time.sleep(p)
                if not checktimeout():
                    cmd["lastrun"] = time.time()
                else:
                    print("Cooldown for command " + str(cmd["name"]) + " tripped... not considering lastrun time.")
                break
        if rancommand:
            print("Clicking button just in case any were missed...", nowebhook = True)
            choosebutton(retry=False)
            if rand(0, 250) == 1 or "enter the chill zone" in driver.find_elements_by_tag_name("body")[0].text.lower():
                p = rand(60, 240)
                print("PAUSING " + str(p) + "...")
                driver.close()
                time.sleep(p)
                while True:
                    try:
                        login()
                        break
                    except KeyboardInterrupt:
                        sys.exit()
                    except Exception as e:
                        e = "".join(traceback.format_exception(type(e), e, e.__traceback__))
                        print("ERROR:\n" + str(e), override = True)
                print("PAUSE END")
            h = time.localtime().tm_hour
            m = time.localtime().tm_min
            s = time.localtime().tm_sec
            sec_of_day = s + m*60 + h*60*60
            if ((sec_of_day > (sleeptime + rand(-3600, 3600))) and (sec_of_day < (sleeptime + rand(-3600, 3600)))) or ((sec_of_day < (sleeptime + rand(-3600, 3600))) and (sec_of_day > (sleeptime + rand(-3600, 3600)))):
                p = rand(10800, 14400)
                print("AFK (SLEEPING) " + str(p) + "...")
                time.sleep(p)
                print("AFK (SLEEP) END")
        else:
            pass
    except KeyboardInterrupt:
        print("Exiting...")
        sys.exit()
    except Exception as e:
        e = "".join(traceback.format_exception(type(e), e, e.__traceback__))
        print("ERROR:\n" + str(e), override = True)
