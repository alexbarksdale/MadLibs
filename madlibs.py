# Stores the user's adjectives
adjArray = []

# Asks the user THREE adjectives before looping out and asking the user the other questions
phraseSelector = 0
phrases = ['Enter an adjective: ', 'Enter another adjective: ',
           'Please enter another adjective: ']
i = 0
while i <= 2:
    adjInput = adjArray.append(input(phrases[phraseSelector]))
    phraseSelector += 1
    i += 1

birdType = input('Enter a type of bird: ')
roomLocation = input('Enter a room in a house: ')
person = input('Enter someone\'s name: ')

# Stores the template for the story and uses f-strings (format strings)
# 'f' in the beginning states that the string will be an f-string. It allows you to embedded Python expressions inside string contents.


def storyTemplate():
    print(
        f'It was a {adjArray[0].lower()}, cold November day. I woke up to the {adjArray[1].lower()} smell of a {birdType.lower()} roasting in the {roomLocation.lower()}. ' +
        f'{person.title()}\'s {birdType.lower()} tacos are totally {adjArray[2].lower()}.')


# Calls the storyTemplate function
storyTemplate()
