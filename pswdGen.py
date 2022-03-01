import random

class PasswordGenerator:

    def __init__(self):

        self.letters = 'abcdefghijklmnopqrstuvwxyz'
        self.numbers = '0123456789'
        self.phrase = ''
        self.password = ''
    
    def formatation(self):
        self.passwordFormat = ['444', '372', '327', '183', '237', '336', '552']
        self.formatType = random.choice(self.passwordFormat)
        return self.formatType
    
    def createPassword(self):
        self.formatPassword = self.formatation()

        for number in range(int(self.formatPassword[0])):
            self.phrase += random.choice(self.numbers)
        for lower in range(int(self.formatPassword[1])):
            self.phrase += random.choice(self.letters)
        for upper in range(int(self.formatPassword[2])):
            self.phrase += random.choice(self.letters).upper()

        self.union = random.sample(self.phrase, len(self.phrase))
        for i in self.union: self.password += i
        return self.password

    def ShowPassword(self):
        self.shufledPassword = self.createPassword()
        return f'Password: {self.shufledPassword}'

p1 = PasswordGenerator()
print(p1.ShowPassword())
