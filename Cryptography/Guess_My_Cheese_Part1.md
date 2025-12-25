# Guess My Cheese (Part 1)

## Description

Try to decrypt the secret cheese password to prove you're not the imposter!

By connecting to the program by netcat: `nc verbal-sleep.picoctf.net PORT`

It gives us a description with secret cheese `OMOCHKLLKXCV` and options to either (g)uess the cheese or (e)ncrypt the cheese.

<img width="948" height="146" alt="image" src="https://github.com/user-attachments/assets/3d7e711d-aef6-4d13-a745-6b536f124525" />

## Solution

We cannot directly guess the cheese and there is also no description that would hint of any algorithm so checking the hint it says "affinity for linear equations" which hints for the **Affine Cipher** as it contains linear equation to encrypt and decrypt the original message.

First for checking, choose (e)ncrypt for cheese so it asks for a message to encrypt so I use original cheese name such as `CHEDDAR` which luckily gave its encrypted message `WFKDDIX`.

<img width="484" height="143" alt="image" src="https://github.com/user-attachments/assets/6922eca7-bc20-42bc-9631-7c4c35f27ecc" />

### Affine Cipher Overview

Each letter is first converted to a number:

A = 0, B = 1, C = 2, ..., Z = 25


Then encryption is done using:

E(x)
 
=
 
(a
 
×
 
x
 
+
 
b)
 
mod
 
26
E(x) = (a × x + b) mod 26

Where:

x = numerical value of the plaintext letter

a = multiplicative key

b = additive key

26 = number of letters in the English alphabet

a must be coprime with 26

This ensures decryption is possible.

Valid values for a:

1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25


If gcd(a, 26) ≠ 1, the cipher cannot be decrypted.

To decrypt, you need the modular inverse of a:

\textbf{D(y) = a^{-1}(y - b) mod 26}

Where:

y = encrypted letter

a⁻¹ = modular inverse of a (mod 26)

So for the decryption we need the a and b values so putting the encrypted message earlier in [DCode](https://www.dcode.fr/affine-cipher) to get the a and b values which we get a = 7 and b = 8 amd with the help of that we can get the generate all the letters of the original message

<img width="337" height="336" alt="image" src="https://github.com/user-attachments/assets/dfc6eac3-d633-4665-b545-d890c90e715b" />


