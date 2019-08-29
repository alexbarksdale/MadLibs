import random
import re

# inputChecker uses REGEX to look through the user's input and checks to see if there are only words (A-Z)
# If it contains any special characters such as $ or @, it'll return false. '*$' means it'll check all the way through the input


def inputChecker(userInput):
    if re.match(r'^[a-zA-Z]*$', userInput):
        return True
    else:
        return False


# Stores the user's adjectives
adjArray = []

# Asks the user THREE adjectives before looping out and asking the user the other questions
phraseSelector = 0
phrases = ['Enter an adjective: ', 'Enter another adjective: ',
           'Please enter another adjective: ']

for userInput in phrases:
    adjInput = input(phrases[phraseSelector])
    if inputChecker(adjInput):
        adjArray.append(adjInput)
    phraseSelector += 1


birdType = input('Enter a type of bird: ')
roomLocation = input('Enter a room in a house: ')
personName = input('Enter someone\'s name: ')

# Stores the template for the story and uses f-strings (format strings)
# 'f' in the beginning states that the string will be an f-string. It allows you to embedded Python expressions inside string contents


def storyTemplate():
    print(
        f'It was a {random.choice(adjArray).lower()}, cold November day. I woke up to the {random.choice(adjArray).lower()} smell of a {birdType.lower()} roasting in the {roomLocation.lower()}. ' +
        f'{personName.title()}\'s {birdType.lower()} tacos are totally {random.choice(adjArray).lower()}.')


# Calls the storyTemplate function
storyTemplate()
