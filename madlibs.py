# Stores the template for the story and uses f-strings (format strings)
# 'f' in the beginning states that the string will be an f-string. It allows you to embedded Python expressions inside string contents.


def storyTemplate():
    print(
        f'It was a {adjArray[0]}, cold November day. I woke up to the {adjArray[1]} smell of {birdType} roasting in the {roomLocation}.')


# Stores the user's adjectives
adjArray = []

# Asks the user TWO adjectives before looping out and asking the user the other questions
i = 0
while i <= 1:
    adjInput = adjArray.append(input('Enter an adjective: '))
    i += 1

birdType = input('Enter a type of bird: ')
roomLocation = input('Enter a room in a house: ')

# Calls the storyTemplate function
storyTemplate()
