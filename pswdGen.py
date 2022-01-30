import random

lowerLetters = 'abcdefghijklmnopqrstuvwxyz'
upperLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'

options = ['444', '372', '327', '183', '237', '336', '552'] #possible formatatios (4 numbers, 4 lower letters and 4 upper letters)

phrase = ''
password = ''

formatType = random.choice(options)

for number in range(int(formatType[0])):
    phrase += random.choice(numbers)
for lower in range(int(formatType[1])):
    phrase += random.choice(lowerLetters)
for upper in range(int(formatType[2])):
    phrase += random.choice(upperLetters)

union = random.sample(phrase, len(phrase)) #shuffle the phrase
for i in union: password += i

print(f'Your random password is: {password}')
