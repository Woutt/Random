# i made this for a minecraft game that called scufflemc and every 10 min there is a quest in the chat where you can get alot of money from in game
# i was in a server with 800+ players always the winner and the devs/admins didnt know or care
# richest player in the server ez

# imports
import re
import os
import time
import datetime
import random
import itertools
import winsound
import pyperclip # pip install pyperclip

# files
file_name = str('net/' + datetime.date.today().strftime('%Y-%m-%d') + '.txt')
if not os.path.exists(file_name):
    open(file_name, "w").close()

# variables
otime = os.path.getmtime(file_name)
htime = os.path.getmtime(file_name)

# functions
def copy_func(text):
    text = str(text)
    pyperclip.copy(text)

def empty_file():
    with open(file_name, 'w') as x:
            x.write('')
empty_file()

def game_signal(x): # freq | dur
    if (x == "updating"):
        winsound.Beep(500, 50)
        winsound.Beep(500, 50)
    else:
        winsound.Beep(440, 100)
        winsound.Beep(200, 100)
        winsound.Beep(500, 300) 

def math_game():
    def replace_char(string):
        string = string.replace('x', '*')
        string = string.replace('^', '**')
        return string

    with open(file_name, 'r') as f:
        match = re.search(r'out\s+(.+)\s+gets', f.read())
        if match:
            result = eval(replace_char(match.group(1)))
            data_result = match.group(1) + ' = ' + str(result)
            print(data_result)
            copy_func(result)
            with open('data/math.txt', 'r') as c:
                if not data_result + '\n' in c.readlines():
                    with open('data/math.txt', 'a') as g:
                            g.writelines(data_result + '\n')
        else:
            print('math_game func: ERROR')
    game_signal("")
    empty_file()

def unscramble_game():   
    def unscramble(word):
        with open('data/unscramble.txt', 'r') as f:
            wordlist = [line.strip() for line in f]
            perms = list(itertools.permutations(word))
            for perm in perms:
                unscrambled = ''.join(perm)
                if unscrambled in wordlist:
                    return unscrambled
            return ''
    with open(file_name, 'r') as f:
        match = re.search(r'unscramble\s+(.+)\s+gets', f.read())
        if match:
            scramble_result = match.group(1)
            unscramble_result = unscramble(scramble_result)
            if not unscramble_result:
                game_signal("updating")
                empty_file()
                while True:
                    time.sleep(2)
                    with open(file_name, 'r') as f:
                        time.sleep(0.1)
                        unscramble_word = re.search(r'saying\s+(.+)\s+first', f.read())
                        if unscramble_word:
                            print('ADDED UNSCRABLE WORD: ' + unscramble_word.group(1))
                            with open('data/unscramble.txt', 'r') as c:
                                data = unscramble_word.group(1) + '\n'
                                if not data in c.readlines():
                                    with open('data/unscramble.txt', 'a') as g:
                                            g.writelines(data)
                                            break
            else:
                print(scramble_result + ' | ' + unscramble_result)
                copy_func(unscramble_result)
                game_signal("")
        else:
            print('unscramble_game func: ERROR')
    empty_file()

def say_game(): 
    with open(file_name, 'r') as f:
        match = re.search(r'say\s+(.+)\s+gets', f.read())
        if match:
            result = match.group(1)
            print(result)
            copy_func(result)
            with open('data/words.txt', 'r') as c:
                if not result + '\n' in c.readlines():
                    with open('data/words.txt', 'a') as g:
                            g.writelines(result + '\n')
        else:
            print('say_game func: ERROR')
    game_signal("")
    empty_file()

while True:
    with open(file_name, 'r') as f:
        time.sleep(random.uniform(0.1, 1))
        for regel in f:
            if 'First person to work out' in regel:
                math_game()
            elif 'First person to unscramble' in regel:
                unscramble_game()
            elif 'First person to say' in regel:
                say_game()
    time.sleep(random.uniform(0.7, 1))
