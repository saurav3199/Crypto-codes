import sys
import traceback
import binascii
from Crypto.Util.number import inverse

try:
    l=map(int,sys.argv[1:])
    p,n,e=l
    c=int(input("Enter the ciphertext you want to uncipher:"))
    q=n//p
    h=(p-1)*(q-1)
    d=inverse(e,h)
    plain=hex(pow(c,d,n))[2:]
    print("The original plaintext is: " + ''.join([chr(int(''.join(c), 16)) for c in zip(plain[0::2],plain[1::2])]))
    #print(binascii.unhexlify(plain)) # If you want to use binascii
except Exception:
    print("Bad Input!!!")
    #traceback.print_exc()    # If you want to debug