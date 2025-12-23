# EVEN RSA CAN BE BROKEN???

## Description

This service provides you an encrypted flag. Can you decrypt it with just N & e?

Connect to the program with netcat: `nc verbal-sleep.picoctf.net PORT`

### RSA Overview

RSA is one of the most widely used public-key cryptosystems. It’s based on **the difficulty of factoring large numbers**. Here's the core idea:

#### Key Generation
1. Pick two large prime numbers, `p` and `q`.
2. Compute `N = p * q` (the modulus).
3. Compute `φ(N) = (p - 1) * (q - 1)` (Euler’s totient function).
4. Choose an encryption exponent `e` (3, 15, 17 or 65537).
5. Compute the decryption exponent `d` such that `d * e ≡ 1 (mod φ(N))`. In other words, `d * e - 1` is divisible by `φ(N)`.

#### Encryption
1. Convert the message `m` into an integer.
2. Compute ciphertext:  `c = m^e mod N`

#### Decryption
1. Compute the original message:  `m = c^d mod N`

**Important:** `N` and `e` are public keys, while `d` is private key.

For Reference: [How To Encrypt with RSA](https://youtu.be/wcbH4t5SJpg?si=ayQqE_PIZxJWvsqZ)

## Solution

By connecting to the program it gives us long value of N, e and Ciphertext

<img width="761" height="46" alt="image" src="https://github.com/user-attachments/assets/9fa0cf39-e49f-4cc0-aeac-354df0627102" />


Checking the program's source code, it generates a **1024-bit RSA key** (`N = p * q`) using two primes `p` and `q` of 512 bits each and encrypts a secret message (the flag) using the public key `(N, e)`.

```
from sys import exit
from Crypto.Util.number import bytes_to_long, inverse
from setup import get_primes

e = 65537

def gen_key(k):
    """
    Generates RSA key with k bits
    """
    p,q = get_primes(k//2)
    N = p*q
    d = inverse(e, (p-1)*(q-1))

    return ((N,e), d)

def encrypt(pubkey, m):
    N,e = pubkey
    return pow(bytes_to_long(m.encode('utf-8')), e, N)

def main(flag):
    pubkey, _privkey = gen_key(1024)
    encrypted = encrypt(pubkey, flag) 
    return (pubkey[0], encrypted)

if __name__ == "__main__":
    flag = open('flag.txt', 'r').read()
    flag = flag.strip()
    N, cypher  = main(flag)
    print("N:", N)
    print("e:", e)
    print("cyphertext:", cypher)
    exit()
```

Since the `get_primes` function can sometimes return the same primes, it may be possible to **guess or recover `p` and `q`**, and thus compute the private key `d` to decrypt the flag.

First we are checking if it is a bad RSA meaning if p and q are equal (`p == q`).

```
import math

N = 23862185798830751009889860713242506336407155564844571569331063263059787388258961240693779669520708309449009060229945082284733848534704566446587578564254334
p = math.isqrt(N)
if p * p == N:
    print("Found p = q =", p)
```

But this does not give any result meaning this is not a bad RSA. So now we use [FactorDB](https://factordb.com/) as it knows many resused RSA Moduli, so if it gives FF (Fully Factored) meaning we got the `p` and `q`.

Putting the `N` value in FactorDB gives us FF meaning it is fully factored in which there are two prime numbers `p = 2` and `q = 119310928994153755049449303566212531682035777824222857846655316315298936941294806203468898347603541547245045301149725411
42366924267352283223293789282127167`

Now making a Python code to decrypt the message by the equation `m = c^d mod N`

from Crypto.Util.number import inverse, long_to_bytes

N = 23862185798830751009889860713242506336407155564844571569331063263059787388258961240693779669520708309449009060229945082284733848534704566446587578564254334
e = 65537
ciphertext = 9363550598512256141009592723377401954361782944980141332523084391874743968414447752918905836544928936106832298941808972062761329178586685120858940536987921

# factors from FactorDB
p = 2
q = 11931092899415375504944930356621253168203577782422285784665531631529893694129480620346889834760354154724504530114972541142366924267352283223293789282127167


assert p * q == N

# phi for broken RSA
phi = q - 1

d = inverse(e, phi)

m = pow(ciphertext, d, N)
flag = long_to_bytes(m).decode()

print("FLAG:", flag)









