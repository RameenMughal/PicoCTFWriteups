# Guess My Cheese (Part 2)

## Description

The imposter was able to fool us last time, so we've strengthened our defenses!

By connecting to the challenge by netcat: `nc verbal-sleep.picoctf.net PORT`

It gives us a description and a secret cheese (hash) `1be510ae28597ee63424a477506352b3c8c80e02e662e2e14fca662b9406dfde` and the only option is to `(g)uess the cheese`

So we cannot `(e)ncrypt the cheese` and identify the cipher like the last time

<img width="944" height="146" alt="image" src="https://github.com/user-attachments/assets/afacf880-d805-46c9-9c72-9905db042779" />

## Solution

The length of the string indicates the hash is of SHA-256 hash as it has `64` hex characters and each hex takes `4` bits (`1 hex = 4 bits`) so `64 x 4 = 265` bits which is the length of SHA-256 hash

**Note**: How it is `64` hex characters? You can group the characters into `8` groups and and each group have `8` hex characters so `8 x 8 = 64 hex characters`

To get the hash cracked, I went to the [CrackStation](https://crackstation.net/) website but got an unknown hash 

But we are confirmed that it is SHA-256 hash so it is **salted up**

