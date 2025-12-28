# 🧀 Guess My Cheese (Part 2)

## Description

The imposter was able to fool us last time, so we've strengthened our defenses!

By connecting to the challenge by netcat: `nc verbal-sleep.picoctf.net PORT`

It gives us a description and a secret cheese (hash) `f25da7cde02d90d38708c5011c5b1a791291cecb786ce769ac2f75b2043441f1` and the only option is to `(g)uess the cheese`

So we cannot `(e)ncrypt the cheese` and identify the cipher like the last time

<img width="945" height="162" alt="image" src="https://github.com/user-attachments/assets/c3688f38-9a69-4cd7-8db7-3aab8399fd42" />

## Solution

### Identifying the Hash Algorithm

The given hash consists of `64` hexadecimal characters.
- `1` hexadecimal character = `4` bits
- `64` hex characters × `4` bits = `256` bits

📌 SHA-256 produces exactly `256-bit` hashes, which are displayed as `64` hexadecimal characters.

**Why it’s 64 hex characters**

We can group the hash as: `f25da7cd e02d90d3 8708c501 1c5b1a79 1291cecb 786ce769 ac2f75b2 043441f1`

This gives: `8` groups
- `8` hex characters per group
- `8 × 8` = `64` hex characters

This strongly indicates that the hash algorithm used is **SHA-256**.

To get the hash cracked, I went to the [CrackStation](https://crackstation.net/) website but got an unknown hash 

But we are confirmed that it is SHA-256 hash so it is **salted up**.

----

### 🧂 What Is a Salted Hash?

A salted hash is created by adding extra data (called a salt) to the input before hashing.

An unsalted hash creates the same hash so salted hash is used as **different salt with the hash creates different hashes**.

**Example**:
- `salt + hash` creates different hash
- `hash + salt` creates different hash
- `ha salt sh` creates different hash

----

### Why Salted Hashes Matter

- **Without salt**
  - An attacker cracks one hash
  - Instantly knows all users with the same password
- **With salt**
  - Each hash must be cracked individually
  - Much slower and computationally expensive
- That’s why real-world password databases always use salted hashes.

----

### Salt Usage in This Challenge

From the hint: **Exactly 2 nibbles of hexadecimal-character salt**

This means:
- `1 nibble = 4 bits`
- `2 nibbles = 1 byte (8 bits)`

Possible salt values: `00 → ff` (256 possibilities)

So the server likely computes something like: `hash = SHA256(salt + cheese)`

----

### What We Know vs What We Don’t

- **Known**
  - Hash algorithm: SHA-256
  - Salt size: 1 byte
  - Cheese names come from `cheese_list.txt`
- **Unknown**
  - Where the salt is placed (prepend, append, or inserted)
  - Whether the salt is raw bytes or hex text
  - What string encoding is used
  - Whether case sensitivity matters

Because these details are unknown, we must **brute force all reasonable combinations**.

**Note**
- **Raw bytes** are the actual byte values (0–255) used directly by the computer (e.g., `\x0f` = one byte).  
- **Hex text** is a human-readable string representing hex values (e.g., `0f` = two characters → two bytes).

----

### 🛠️ Brute Force Strategy

We create a script (`solve.py`) that:

1. Takes the target SHA-256 hash
2. Loads all cheese names from `cheese_list.txt`
3. Generates all 256 possible salt values
4. Tries multiple combinations:
   - Salt prepended
   - Salt appended
   - Salt inserted at different positions
   - Raw byte salt vs hex string salt
   - Case variations
   - Different encodings
5. Hashes each candidate and compares it to the target hash

Once a match is found, the correct cheese name is revealed.

Run the script with the target hash `f25da7cde02d90d38708c5011c5b1a791291cecb786ce769ac2f75b2043441f1` and we get the correct cheese name with all the information.

<img width="400" height="150" alt="image" src="https://github.com/user-attachments/assets/666d23f1-314b-416a-853d-641ce979131a" />

Select the `(g)uess the cheese` and then put the cheese name, it asks for the salt

<img width="535" height="335" alt="image" src="https://github.com/user-attachments/assets/f33814cd-bac4-43d7-b64c-c2d5e685283b" />

Put the value of salt in **hex format**, Then we get our flag!

<img width="344" height="361" alt="RSASalt" src="https://github.com/user-attachments/assets/430ffc50-bfe1-4965-bd4b-298c0139be23" />
