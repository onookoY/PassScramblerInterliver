import random

class Generate(object):

    def passwrd(self):
        Liter = 'qwertyuiopasdfghjklzxcvbnm'
        Numbers = '1234567890'
        Symbols = '!@#$%^&*()'
        HightLiter = Liter.upper()
        PreformString = Liter+Numbers+HightLiter+Symbols
        PreformList = list(PreformString)
        random.shuffle(PreformList)
        psw = ''.join([random.choice(PreformList) for item in range(12)])
        return(psw)