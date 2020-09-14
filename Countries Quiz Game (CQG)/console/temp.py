from pandas import read_csv as read
import sys
from os import system as os_sys
from platform import system as pltf_sys

# constants
continents = ['Africa', 'Asia', 'Australia', 'Europe', 'North America', 'South America']


# End constants


# choices
def choices_0_1():
    response = str(input()).lower().strip()
    CHOICES = {'yes', 'no', '1', '0', 'y', 'n'}
    while response not in CHOICES:
        print("please enter your choice correctly!")
        response = str(input()).lower().strip()
    return response in ['yes', '1', 'y']


def choices_to_n(a, n):
    while True:
        number = str(input()).lower().strip()
        try:
            number = int(number)
            if number < a or number > n:
                print("please enter valid number")
            else:
                break
        except:
            print("please enter your choice correctly!")
        print("choice from 1 to {}".format(n))
    return number


def print_yes_no():
    print(prefix_word('Yes or 1', 'if you agree', width=15))
    print(prefix_word('No or 0', 'if you are not agree', width=15))


def again():
    print_yes_no()
    return choices_0_1()


# End choices


# load data
def read_data():
    try:
        df = read('data.csv')
    except:
        # my csv file on google drive if user deleted the original file
        url = 'https://drive.google.com/uc?export=download&id=1jEGI-T3xlMQKuFkmSvexP8AslqtVcrf4'
        try:
            df = read(url)
            df.to_csv('data.csv', index=False)
        except:
            print(
                "Please make sure that you are connected to the internet to download program data\nreopen the program")
            sys.exit()
    return df


# End load data


#
def token_time(start, end):
    token = int(end - start)
    h, m, s = 0, 0, 0
    h = int(token / (60 * 60))
    token = (token % (60 * 60))
    m = int(token / 60)
    token = token % 60
    s = token
    time = ''
    if h > 0:
        time = "{} hour, {}, minutes, {} seconds".format(h, m, s)
    elif m > 0:
        time = "{} minutes, {} seconds".format(m, s)
    else:
        time = "{} seconds".format(s)
    return time


# print formats
def title(word, position='^', width=44):
    return "{:{pos}{w}}".format(word, pos=position, w=width).title()


def line(char='-', length=44):
    return str(char) * length


def prefix_word(word, sentence, position='<', width=10):
    return "{:{pos}{w}} {}".format(word, sentence, pos=position, w=width)


def suffix_word(word, sentence, position='>', width=10):
    return "{} {:{pos}{w}}".format(sentence, word, pos=position, w=width)


def center_word(word, sentence1, sentence2, position='^', width=10):
    return "{} {:{pos}{w}} {}".format(sentence1, word, sentence2, pos=position, w=width)


# End print formats

# screen
def clear():
    platform = pltf_sys().lower()
    screen = ''
    if platform == 'Windows'.lower():
        screen = 'clr'
    else:
        screen = 'clear'
    os_sys(screen)
# End screen
