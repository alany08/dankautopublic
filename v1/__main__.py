import time
import pyautogui
import clipboard
import random
import re
import requests
from bs4 import BeautifulSoup as soup
from itertools import permutations
import nltk
from nltk.corpus import brown

pyautogui.PAUSE = 1

def grabtext():
    oldpause = pyautogui.PAUSE
    pyautogui.PAUSE = 0.2
    old_text = clipboard.paste()
    while old_text == clipboard.paste():
        rand_x = random.randint(-100,100)
        rand_y = random.randint(-100,100)
        pyautogui.move(0+rand_x,-1500+rand_y)
        pyautogui.drag(0-rand_x,1500-rand_y-20, 1)
        pyautogui.hotkey("ctrl", "c")
        pyautogui.move(0,20)
        pyautogui.click()
    pyautogui.PAUSE = oldpause
    return clipboard.paste()

def rand_select_search():
    text = grabtext()
    t_arr = text.split("Pick from the list below and type the name in chat.\n")
    t_arr = t_arr[len(t_arr)-1]
    t_arr = t_arr.split("\n")
    options = t_arr[0].split(", ")
    return random.choice(options)

def high_low():
    text = grabtext()
    t_arr = text.split("A number secret between 1-100 has been chosen. Your hint is ")
    t_arr = t_arr[len(t_arr)-1]
    number = t_arr.split(".")[0]
    try:
        number = int(number)
    except:
        return random.choice(["high", "low", "jackpot"])
    if number < 45:
        return "high"
    if number > 55:
        return "low"
    if number >=45 and number <=55:
        return "jackpot"

def remove_all(item, lst):
    while item in lst:
        lst.remove(item)
    return lst

def fill_in_blank(phrase):
    prev_ones = ["I am a dwarf and I diggy the hole", "woah a big one", "the fish says glub", "big big fishy", "I hope I find some treasure", "We're always lurking in chat", "I will rob your entire wallet in one swipe", "I have no problem stealing candy from babies", "The baby puked on the floor again", "Would you like to buy some essential oils", "Another drink coming right up", "Meow I am a cat girl", "Looks like someone's on a ban streak", "The rules are pretty simple"]
    phrase = phrase.lower()
    f = open("words.txt", "r")
    words = f.read()
    f.close()
    words = words.replace("\r", "")
    words = words.split("\n")
    arr = re.split("( +)(?!_)", phrase)
    arr = remove_all(" ", arr)
    missing = None
    for word in arr:
        if "_" in word:
            missing = word
    if missing == None:
        return [""]
    ctx = phrase.split(missing)
    ctx_rgx = "^" + ctx[0].lower() + "[^\s\s$]{2,}" + ctx[1].lower() + "$"
    ctx_rgx = re.compile(ctx_rgx)
    used = None
    for prev in prev_ones:
        if ctx_rgx.match(prev.lower()) != None:
            used = prev
            break
    if used == None:
        missing = missing.replace(" ", "")
        missing_regx = missing.replace("_", ".")
        missing_regx = "^" + missing_regx + "$"
        missing_regx = re.compile(missing_regx)
        possible = []
        for w in words:
            if missing_regx.match(w) != None:
                possible.append(w)
        final = []
        print("Length before grammar check: ", len(possible))
        if len(possible) < 20:
            for p in possible:
                if check_grammar(ctx[0] + p + ctx[1]):
                    final.append(p)
            print("Length after grammar check: ", len(final))
            freqs = nltk.FreqDist([w.lower() for w in brown.words()])
            final = sorted(final, key=lambda x: freqs[x.lower()], reverse=True)
        else:
            print("Too long to grammar check")
            freqs = nltk.FreqDist([w.lower() for w in brown.words()])
            possible = sorted(possible, key=lambda x: freqs[x.lower()], reverse=True)
            final = possible[0:5]
        return final
    else:
        word = used.lower().replace(ctx[0], "").replace(ctx[1], "")
        return [word]

def check_grammar(text):
    search = requests.get("http://google.com/search?q=" + text).text
    search = soup(search, "html.parser")
    search = search.text
    search = search.lower()
    if "showing results for" in search:
        return False
    if "did you mean" in search:
        return False
    if "aren't many great matches" in search:
        return False
    else:
        return True

def google(query):
    t = requests.get("http://google.com/search?q=" + query).text
    t = soup(t, "html.parser").text
    return t

def trivia(question, options):
    """
    options:
    [("letter", "text"), ("letter", "text")] etc...
    everything should be lowercase
    """
    text = google(question)
    text = text.lower()
    largest = ("a", 0)
    for opt in options:
        if text.count(opt[1]) > largest[1]:
            largest = (opt[0], text.count(opt[1]))
    if largest[1] == 0:
        for opt in options:
            _opt = opt[1].split(" ")
            this_one = 0
            for o in _opt:
                this_one = this_one + text.count(o)
            if this_one > largest[1]:
                largest = (opt[0], this_one)
    return largest[0]

def handle_trivia():
    rawtext = grabtext()
    rawtext = rawtext.lower()
    rawtext = rawtext.replace("\r", "")
    question_opts = rawtext.split("trivia question\n")
    question_opts = question_opts[len(question_opts)-1]
    question_opts = question_opts.split("\n")
    question = question_opts[0]
    try:
        opts = [(question_opts[3][0], question_opts[3][3:]), (question_opts[4][0], question_opts[4][3:]), (question_opts[5][0], question_opts[5][3:]), (question_opts[6][0], question_opts[6][3:])]
    except:
        print("Failed to parse question and options...")
    try:
        answer = trivia(question, opts)
    except:
        print("Failed to search google for trivia answer...")
        return
    pyautogui.typewrite(answer + "\n\n")

def perms(string):
    string = string.lower()
    all_perms = permutations(string)
    all_perms_str = []
    for permutation in all_perms:
        all_perms_str.append("".join(permutation))
    return all_perms_str

def unscramble(string):
    prev = ["jellyfish", "fishing", "trout", "ground", "shovel", "squid", "excavate", "stickbug", "ocean", "trowel", "unearth", "ladybug", "fishy", "spider", "whale"]
    string = string.lower()
    f = open("words.txt", "r")
    words = f.read()
    f.close()
    words = words.lower()
    words = words.replace("\r", "")
    words = words.split("\n")
    permutations = perms(string)
    possible = []
    for word in prev:
        if word in permutations:
            return [word]
    for permutation in permutations:
        if permutation in words:
            possible.append(permutation)
    possible = list(dict.fromkeys(possible))
    freqs = nltk.FreqDist([w.lower() for w in brown.words()])
    possible = sorted(possible, key=lambda x: freqs[x.lower()], reverse=True)
    return possible

def handle_unscramble():
    txt = grabtext()
    txt = txt.lower()
    txt = txt.replace("\r", "")
    data = txt.split("next 15 seconds\n")
    data = data[len(data)-1]
    word = data.split("\n")[0]
    solved = unscramble(word)
    for i in solved:
        pyautogui.typewrite(i + "\n\n")

def handle_reverse():
    txt = grabtext()
    txt = txt.lower()
    txt = txt.replace("\r", "")
    data = txt.split("next 10 seconds!.\n")
    data = data[len(data)-1]
    word = data.split("\n")[0]
    pyautogui.typewrite(word[::-1] + "\n\n")

def handle_fill():
    oldpause = pyautogui.PAUSE
    pyautogui.PAUSE = 0.1
    for i in range(0, 4):
        txt = grabtext().lower()
        phrase = txt.split("\n")
        phrase = phrase[len(phrase)-1].replace("\ufeff", "")
        phrase = phrase.split("\n")[0]
        answers = fill_in_blank(phrase)
        try:
            pyautogui.typewrite(answers[0] + "\n\n")
        except:
            print("Error writing filled in word")
    pyautogui.PAUSE = oldpause

"""
Guess number (beta))
def guess_num():
    txt = grabtext()
    txt = txt.lower()
    data = txt.split("number between ")
    data = data[len(data)-1]
    data = data.split(". ")[0]
    data = data.split(" and ")
    try:
        for i in range(0, len(data)):
            data[i] = int(data[i])
    except:
        print("Unable to guess the word [int conversion failure]")
        return False
    print("Guessing a number ranging from", data[0], "to", data[1])
    first_guess = random.randint(data[0], data[1])
    pyautogui.typewrite(str(first_guess) + "\n\n")
    txt = grabtext()
    txt = txt.lower()
    if "thinking" in txt and "number" in txt:
        return True
    pyautogui.typewrite("hint\n\n")
    txt = grabtext()
    txt = txt.lower()
"""

while True:
    pyautogui.typewrite("pls hunt\n\n")
    txt = grabtext()
    if "type the phrase" in txt.lower():
        phrase = txt.split("Type ")
        phrase = phrase[len(phrase)-1].replace("\ufeff", "")
        phrase = phrase.split("\n")[0]
        pyautogui.typewrite(phrase + "\n\n")
    elif "guess the missing word" in txt.lower():
        handle_fill()
    if "scramble" in txt and "word" in txt:
        handle_unscramble()
    if "reverse" in txt and "word" in txt:
        handle_reverse()
    pyautogui.typewrite("pls fish\n\n")
    txt = grabtext()
    if "type the phrase" in txt.lower():
        phrase = txt.split("Type ")
        phrase = phrase[len(phrase)-1].replace("\ufeff", "")
        phrase = phrase.split("\n")[0]
        pyautogui.typewrite(phrase + "\n\n")
    elif "guess the missing word" in txt.lower():
        handle_fill()
    if "scramble" in txt and "word" in txt:
        handle_unscramble()
    if "reverse" in txt and "word" in txt:
        handle_reverse()
    pyautogui.typewrite("pls dig\n\n")
    txt = grabtext()
    if "type the phrase" in txt.lower():
        phrase = txt.split("Type ")
        phrase = phrase[len(phrase)-1].replace("\ufeff", "")
        phrase = phrase.split("\n")[0]
        pyautogui.typewrite(phrase + "\n\n")
    elif "guess the missing word" in txt.lower():
        handle_fill()
    if "scramble" in txt and "word" in txt:
        handle_unscramble()
    if "reverse" in txt and "word" in txt:
        handle_reverse()
    pyautogui.typewrite("pls beg\n\n")
    pyautogui.typewrite("pls postmemes\n\n")
    pyautogui.typewrite(random.choice(["f","r","i","c","k"])+"\n\n")
    pyautogui.typewrite("pls dep all\n\n")
    pyautogui.typewrite("pls highlow\n\n")
    pyautogui.typewrite(high_low()+"\n\n")
    pyautogui.typewrite("pls dep all\n\n")
    pyautogui.typewrite("pls search\n\n")
    pyautogui.typewrite(rand_select_search()+"\n\n")
    pyautogui.typewrite("pls dep all\n\n")
    pyautogui.typewrite("pls trivia\n\n")
    handle_trivia()
    for i in range(0, 5):
        time.sleep(2)
        pyautogui.typewrite("pls sell "+random.choice(["corncob", "potato", "trash", "junk", "worm", "garbage", "fish", "bread", "ant", "boar", "exoticfish", "duck", "deer", "cookie", "jellyfish", "ladybug", "rabbit", "rarefish", "stickbug", "seaweed", "skunk"])+" all\n\n")
        pyautogui.typewrite("pls dep all\n\n")
    pyautogui.typewrite("pls withdraw 1\n\n")
    pyautogui.typewrite("pls slots 1\n\n")
    pyautogui.typewrite("pls dep all\n\n")
    pyautogui.typewrite("pls use candy\n\n")
    pyautogui.typewrite("pls monthly\n\n")
    pyautogui.typewrite("pls dep all\n\n")
    pyautogui.typewrite("pls use horseshoe\n\n")
    pyautogui.typewrite("pls weekly\n\n")
    pyautogui.typewrite("pls dep all\n\n")
    pyautogui.typewrite("pls use fakeid\n\n")
    pyautogui.typewrite("pls daily\n\n")
    pyautogui.typewrite("pls dep all\n\n")
    pyautogui.typewrite("pls use padlock\n\n")
    pyautogui.typewrite("pls bal\n\n")
    pyautogui.typewrite("pls use landmine\n\n")
    pyautogui.typewrite("pls inv\n\n")
    pyautogui.typewrite("pls use apple\n\n")
    pyautogui.typewrite("pls use banknote\n\n")
    pyautogui.typewrite("pls dep all\n\n")
    pyautogui.typewrite("pls use lifesaver\n\n")
    pyautogui.typewrite("pls pet train "+random.choice(["attack", "defense", "hunting", "sustainability"])+"\n\n")
    pyautogui.typewrite(str(random.randint(1, 5))+"\n\n")
    pyautogui.typewrite("pls use pizza\n\n")
    pyautogui.typewrite("pls withdraw 205\n\n")
    pyautogui.typewrite("pls pet feed\n\n")
    pyautogui.typewrite("pls dep all\n\n")
    pyautogui.typewrite("pls use spinner\n\n")
    pyautogui.typewrite("pls withdraw 45\n\n")
    pyautogui.typewrite("pls pet wash\n\n")
    pyautogui.typewrite("pls dep all\n\n")
    pyautogui.typewrite("pls use pod\n\n")
    pyautogui.typewrite("y\n\n")