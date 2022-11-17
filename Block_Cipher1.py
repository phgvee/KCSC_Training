from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from random import choice
from os import urandom

FLAG = b'KCSC{?????????????????????}'

if __name__ == '__main__':
    for i in range(100):
        x = choice(['ECB','CBC'])
        if x == 'ECB':
            cipher = AES.new(urandom(16), AES.MODE_ECB)
        else:
            cipher = AES.new(urandom(16), AES.MODE_CBC, urandom(16))

        try:
            msg = bytes.fromhex(input())
            assert len(msg) <= 16
            print(cipher.encrypt(pad(msg,16)).hex())
            ans = input()
            assert ans == x
            print('Correct!')
        except:
            print("Exiting...")
            quit()

    print(FLAG)