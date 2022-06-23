import hashlib
import itertools
import time
import numpy as np

class Breaker:
    __hashMethods = {
        'plain': lambda x: x,
        'md5': hashlib.md5,
        'sha1': hashlib.sha1,
        'sha224': hashlib.sha224,
        'sha256': hashlib.sha256,
        'sha384': hashlib.sha384,
        'sha512': hashlib.sha512
    }
    def __init__(self):
        self.method = 'sha256'

    def __getHash(self, string: str):
        if self.method != 'plain':
            return self.__hashMethods[self.method](string).hexdigest()
        else:
            return string

    def setHashMethod(self, method):
        if method in self.__hashMethods:
            self.method = method
            return self
        else:
            raise ValueError('Invalid hash method')

    def breakHash(self, hashedString):
        chars = 'abcdefghijklmnopqrstuvwxyz' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + '1234567890' + '`-=~_+!@#$%^&*()[]\{\}\\|;\':",.<>/?'
        attempts = 0
        length = 1
        while True:
            for guess in itertools.product(chars, repeat=length):
                attempts += 1
                guessPlain = ''.join(guess)
                guessHash = self.__getHash(''.join(guess))
                if guessHash == hashedString:
                    return f'password is {guessPlain}. found in {attempts} guesses.'
            length += 1

if __name__ == '__main__':

    breaker = Breaker()

    method = input('Enter hash method: ')
    breaker.setHashMethod(method)

    string = input('Enter string to break (hashed with the method you entered previously): ')

    startTime = time.time()
    res = breaker.breakHash(string)
    endTime = time.time()
    
    print(res)
    
    print(f'{np.round((endTime - startTime), 3)} sec')