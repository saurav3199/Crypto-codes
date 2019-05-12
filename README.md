# Crypto-codes


Standard codes for decrypting ciphertexts

## Installation:

To use first run this on your terminal:
```
apt install libgmp-dev libmpfr-dev libmpc-dev
```
&
```
pip install -r requirements.txt
```
## Usage:

* Simple rsa attack
  * p - public key
  * n - modulus
  * e - public exponent
```
python rsa.py [p] [n] [e]
```
where p,n,e are in integers
