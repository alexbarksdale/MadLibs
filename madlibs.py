import sys
import random
import re
from colorama import Fore, Back, Style

title = """
 _______          _           _   _   _                          _               
|__   __|        (_)         | | | \ | |                        | |              
   | |_   _ _ __  _  ___ __ _| | |  \| | _____   _____ _ __ ___ | |__   ___ _ __ 
   | | | | | '_ \| |/ __/ _` | | | . ` |/ _ \ \ / / _ \ '_ ` _ \| '_ \ / _ \ '__|
   | | |_| | |_) | | (_| (_| | | | |\  | (_) \ V /  __/ | | | | | |_) |  __/ |   
   |_|\__, | .__/|_|\___\__,_|_| |_| \_|\___/ \_/ \___|_| |_| |_|_.__/ \___|_|   
       __/ | |                                                                   
      |___/|_|                                                                   
"""

print(Fore.CYAN + title + Fore.RESET)
print('If you do not enter a value, a random MadLib will be generated for you.')


# inputChecker uses REGEX to look through the user's input and checks to see if there are only words (A-Z)
# If it contains any special characters such as $ or @, it'll return false. '*$' means it'll check all the way through the input


def inputChecker(userInput):
    if re.match(r'^[a-zA-Z]*$', userInput):
        return True
    else:
        print('You cannot use special characters.')
        return False


# Dictionary contains predetermined words that will be selected at random incase the user doesn't input anything
noInput = {
    'adjList': ['bitter', 'disfigured', 'disloyal'],
    'birdList': ['flamingo', 'mockingjay', 'robin'],
    'roomList': ['basement', 'living room', 'bedroom'],
    'nameList': ['Mike', 'Rob', 'Abby']
}


# Stores the user's adjectives
adjArray = []

phraseSelector = 0
phrases = ['Enter an adjective: ', 'Enter another adjective: ',
           'Please enter another adjective: ']

# While phraseSelector is less than the size of the list it will run
# The phraseSelector will only increase if the inputChecker returns true. If it returns false it will ask the question again
while(phraseSelector < len(phrases)):
    adjInput = input(phrases[phraseSelector])
    # Checks to see if the input is blank (false). If it's false it will get a word from the dictionary
    if not adjInput.strip():
        adjArray.append(random.choice(noInput.get('adjList')))
        phraseSelector += 1
    elif inputChecker(adjInput):
        adjArray.append(adjInput)
        phraseSelector += 1

birdType = input('Enter a type of bird: ')
if not birdType.strip():
    birdType = random.choice(noInput.get('birdList'))
roomLocation = input('Enter a room in a house: ')
if not roomLocation.strip():
    roomLocation = random.choice(noInput.get('roomList'))
personName = input('Enter someone\'s name: ')
if not personName.strip():
    personName = random.choice(noInput.get('nameList'))

# Stores the template for the story and uses f-strings (format strings)
# 'f' in the beginning states that the string will be an f-string. It allows you to embedded Python expressions inside string contents

# TODO Make multiple stories and have it randomized and add ascii art to mactch the story name


def storyTemplate():
    print(
        'Your MadLib was generated: \n' +
        f'It was a {random.choice(adjArray).lower()}, cold November day. I woke up to the {random.choice(adjArray).lower()} smell of a {birdType.lower()} roasting in the {roomLocation.lower()}. ' +
        f'{personName.title()}\'s {birdType.lower()} tacos are totally {random.choice(adjArray).lower()}.')


storyTemplate()
