import hashlib
import itertools
import time
import numpy as np

def getSHA256(string: str):
    return hashlib.md5(str(string).encode('utf-8')).hexdigest()
     
def breakHash(actualHash):
    chars = 'abcdefghijklmnopqrstuvwxyz' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + '1234567890' + '`-=~_+!@#$%^&*()[]\{\}\\|;\':",.<>/?'
    attempts = 0
    length = 1
    while True:
        for guess in itertools.product(chars, repeat=length):
            attempts += 1
            guessPlain = ''.join(guess)
            guessHash = getSHA256(''.join(guess))
            if guessHash == actualHash:
                return f'password is {guessPlain}. found in {attempts} guesses.'
        length += 1

def breakUnHashed(string):
    chars = 'abcdefghijklmnopqrstuvwxyz' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + '1234567890' + '`-=~_+!@#$%^&*()[]\{\}\\|;\':",.<>/?'
    attempts = 0
    length = 1
    while True:
        for guess in itertools.product(chars, repeat=length):
            attempts += 1
            guessPlain = ''.join(guess)
            if guessPlain == string:
                return f'password is {guessPlain}. found in {attempts} guesses.'
        length += 1


if __name__ == '__main__':
    startTime = time.time()

    # actualHash = getSHA256('1234')
    # print(breakHash(actualHash))

    string = 'abcdef'
    print(breakUnHashed(string))

    endTime = time.time()
    print(f'{np.round((endTime - startTime), 3)} sec')