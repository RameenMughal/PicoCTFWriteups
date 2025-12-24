# EVEN RSA CAN BE BROKEN???

## Description

This service provides you an encrypted flag. Can you decrypt it with just N & e?

Connect to the program with netcat: `nc verbal-sleep.picoctf.net PORT`

## RSA Overview

RSA is one of the most widely used public-key cryptosystems. Its security is based on the **computational difficulty of factoring large composite numbers**. RSA uses a pair of mathematically related keys: a public key for encryption and a private key for decryption.

### Key Generation

1. Choose two large prime numbers:

$$
p,\ q
$$

2. Compute the modulus:

$$
N = p \times q
$$

3. Compute Euler’s totient function:

$$
\varphi(N) = (p - 1)(q - 1)
$$

4. Choose a public encryption exponent \( e \) such that:

$$
1 < e < \varphi(N)
$$

and

$$
\gcd(e, \varphi(N)) = 1
$$

Common choices for \( e \) include:

$$
e = 65537
$$

5. Compute the private decryption exponent \( d \) such that:

$$
d \times e \equiv 1 \pmod{\varphi(N)}
$$

This means \( d \) is the modular multiplicative inverse of \( e \).

### Encryption

1. Convert the plaintext message into an integer \( m \) such that:

$$
0 \le m < N
$$

2. Compute the ciphertext:

$$
c = m^e \bmod N
$$

### Decryption

1. Recover the original message using the private key:

$$
m = c^d \bmod N
$$

2. Convert the resulting integer back into readable plaintext.

### Key Properties

- The **public key** consists of:

$$
(N, e)
$$

- The **private key** is:

$$
d
$$

- Without knowledge of \( d \) (or the factors of \( N \)), recovering \( m \) from \( c \) is computationally infeasible when RSA is implemented correctly.

For Reference: [How To Encrypt with RSA](https://youtu.be/wcbH4t5SJpg?si=ayQqE_PIZxJWvsqZ)

## Solution

By connecting to the program it gives us long value of N, e and Ciphertext

<img width="800" height="100" alt="image" src="https://github.com/user-attachments/assets/9fa0cf39-e49f-4cc0-aeac-354df0627102" />

Checking the program's source code, it generates a **1024-bit RSA key** (`N = p * q`) using two primes `p` and `q` of 512 bits each and encrypts a secret message (the flag) using the public key `(N, e)`.

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

Putting the `N` value in FactorDB gives us FF meaning it is fully factored in which there are two prime numbers `p = 2` and `q = 11931092899415375504944930356621253168203577782422285784665531631529893694129480620346889834760354154724504530114972541142366924267352283223293789282127167`

Now making a Python code named as `flag_reveal.py` to decrypt the message by the equation `m = c^d mod N` 

Running the program gives us the flag!

<img width="300" height="100" alt="RSA" src="https://github.com/user-attachments/assets/c98ae544-2ce6-4537-82d6-ff191474c00c" />
