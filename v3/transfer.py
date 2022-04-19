from selenium import webdriver
import sys
import time
from threading import Thread
from random import randint as rand
from pyautogui import size
from math import floor

origin = int(sys.argv[1])
target = int(sys.argv[2])
money = sys.argv[3]
splitscreen = [
    {
        'height': 1407,
        'width': 1294,
        'x': -7,
        'y': 0
    },
    {
        'height': 1407,
        'width': 1294,
        'x': 1273,
        'y': 0
    }
]

done = [False, False]

driver_path = "C:\\Users\\ning\\Documents\\chromedriver.exe"

accounts = [
#First one is the main alt to autotype
    {
        "u": "cowaw32964@niekie.com",
        "p": "Stop Banning Me",
        "id": 906316173384228944
    },
    {
        "u": "alanyu08+storage1@gmail.com",
        "p": "7)W.DDidtsA~zYT",
        "id": 746221182373724230
    },
    {
        "u": "alanyu08+storage2@gmail.com",
        "p": "We'reTotallyNotViolatingToS",
        "id": 905223837438840832
    },
    {
        "u": "alanyu08+storage3@gmail.com",
        "p": "We'reTotallyNotViolatingToS",
        "id": 905226246810640434
    },
    {
        "u": "alanyu08+storage4@gmail.com",
        "p": "We'reTotallyNotViolatingToS",
        "id": 905227435086340106
    },
    {
        "u": "alanyu08+storage5@gmail.com",
        "p": "I think using a different passcode would be better...",
        "id": 905229215924895775
    },
    {
        "u": "alanyu08+storage6@gmail.com",
        "p": "New Passcode!",
        "id": 905231729776795688
    },
    {
        "u": "alanyu08+storage7@gmail.com",
        "p": "LeMotDePasse",
        "id": 905233844884602891
    },
    {
        "u": "alanyu08+storage8@gmail.com",
        "p": "passingpasscode123",
        "id": 905237245454323753
    }
]

def send(msg, driver):
    succeeded = False
    while not succeeded:
        try:
            driver.find_elements_by_class_name("slateTextArea-1Mkdgw")[0].send_keys(msg + "\n")
            succeeded = True
        except KeyboardInterrupt:
            sys.exit()
        except:
            pass


def clickbutton(index, driver):
    for i in range(0, 5):
        try:
            driver.find_elements_by_class_name("secondaryButton-BIo-2g")[0].click()
        except:
            pass
        try:
            parent = driver.find_elements_by_class_name("children-2goeSq")[-1]
            parent.find_elements_by_tag_name("button")[index].click()
            #break Just click more just in case
        except:
            print("No buttons to click")
            try:
                driver.find_elements_by_class_name("secondaryButton-BIo-2g")[0].click()
            except:
                pass
        time.sleep(0.1)

def origin_acc():
    global money
    global origin
    global target
    global accounts
    global done
    global splitscreen

    acc1 = webdriver.Chrome(driver_path)
    acc1.set_window_rect(**splitscreen[0])

    acc1.get("https://discord.com/app/")

    while True:
        try:
            acc1.find_element_by_name("email").send_keys(accounts[origin]["u"] + "\t")
            time.sleep(rand(0, 100)/100)
            acc1.find_element_by_name("password").send_keys(accounts[origin]["p"] + "\n")
            break
        except KeyboardInterrupt:
            sys.exit()
        except Exception as e:
            print("Could not find elements")
        time.sleep(0.1)

    print("Logged in...")

    captcha = False

    while True:
        try:
            try:
                acc1.find_elements_by_css_selector('[role="treeitem"]')[0].click()
            except:
                acc1.find_element_by_css_selector('[aria-label="Close"]').click()
                time.sleep(rand(0, 100)/100)
                acc1.find_elements_by_css_selector('[role="treeitem"]')[0].click()
            break
        except:
            try:
                if not captcha:
                    captchaframe = acc1.find_elements_by_css_selector('[title="widget containing checkbox for hCaptcha security challenge"]')[0]
                    acc1.switch_to.frame(captchaframe)
                    acc1.find_elements_by_css_selector("#anchor-tc")[0].click()
                    acc1.switch_to.default_content()
                    print("Solve captcha plz I'm a dumb bot and I can't solve it...")
                    captcha = True
            except KeyboardInterrupt:
                sys.exit()
            except:
                print("Could not select server")
                try:
                    acc1.find_element_by_name("password").send_keys("\n\n")
                except:
                    pass
        time.sleep(0.1)
    while True:
        try:
            acc1.find_elements_by_class_name("channelName-2YrOjO")[1].click()
            break
        except KeyboardInterrupt:
            sys.exit()
        except:
            print("Could not select channel")
        time.sleep(0.1)

    send("pls with all", acc1)
    time.sleep(rand(100,300)/100)

    send("pls trade " + money + " 1 pink <@" + str(accounts[target]["id"]) + ">", acc1)
    time.sleep(3)
    clickbutton(1, acc1)

    print("Origin acc job done")
    done[0] = True
    sys.exit()

def target_acc():
    global money
    global target
    global accounts
    global done
    global splitscreen

    acc2 = webdriver.Chrome(driver_path)
    acc2.set_window_rect(**splitscreen[1])

    acc2.get("https://discord.com/app/")

    while True:
        try:
            acc2.find_element_by_name("email").send_keys(accounts[target]["u"] + "\t")
            time.sleep(rand(0, 100)/100)
            acc2.find_element_by_name("password").send_keys(accounts[target]["p"] + "\n")
            break
        except KeyboardInterrupt:
            sys.exit()
        except:
            print("Could not find elements")
        time.sleep(0.1)

    print("Logged in...")

    captcha = False

    while True:
        try:
            try:
                acc2.find_elements_by_css_selector('[role="treeitem"]')[0].click()
            except:
                acc2.find_element_by_css_selector('[aria-label="Close"]').click()
                time.sleep(rand(0, 100)/100)
                acc2.find_elements_by_css_selector('[role="treeitem"]')[0].click()
            break
        except:
            try:
                if not captcha:
                    captchaframe = acc2.find_elements_by_css_selector('[title="widget containing checkbox for hCaptcha security challenge"]')[0]
                    acc2.switch_to.frame(captchaframe)
                    acc2.find_elements_by_css_selector("#anchor-tc")[0].click()
                    acc2.switch_to.default_content()
                    print("Solve captcha plz I'm a dumb bot and I can't solve it...")
                    captcha = True
            except KeyboardInterrupt:
                sys.exit()
            except:
                print("Could not select server")
                try:
                    acc2.find_element_by_name("password").send_keys("\n\n")
                except:
                    pass
        time.sleep(0.1)
    while True:
        try:
            acc2.find_elements_by_class_name("channelName-2YrOjO")[1].click()
            break
        except KeyboardInterrupt:
            sys.exit()
        except:
            print("Could not select channel")
        time.sleep(0.1)

    while not done[0]:
        print("Origin account not done...")

    time.sleep(3)
    clickbutton(1, acc2)

    print("Target acc job done")
    done[1] = True
    sys.exit()

Thread(target=origin_acc, daemon=True).start()
Thread(target=target_acc, daemon=True).start()

while (not done[0]) or (not done[1]):
    pass