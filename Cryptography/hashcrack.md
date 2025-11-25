# hashcrack

## Description
A company stored a secret message on a server which got breached due to the admin using weakly hashed passwords. Can you gain access to the secret stored within the server?

Launch the instance and connect to the shell by command `nc verbal-sleep.picoctf.net PORT`

## Solution
By connecting to the instance, we see our first hash and asks for the password

<img width="687" height="131" alt="Screenshot 2025-11-25 221717" src="https://github.com/user-attachments/assets/46693228-4ff7-40a9-ac44-cebf6c35de9b" />

By website [CrackStation](https://crackstation.net/), we can get our cracked hash.

<img width="772" height="295" alt="Screenshot 2025-11-25 223033" src="https://github.com/user-attachments/assets/d3af90b7-97c2-46cc-9ffc-d14e2cc745a1" />

We can see that this is the MD5 Hash (Message-Digest) Algorithm producing 128 bit hash value that was designed in 1991. As it is an old algorithm so it can be cracked easily.

Entering the password, we get another hash to find the flag.

<img width="600" height="200" alt="Screenshot 2025-11-25 222530" src="https://github.com/user-attachments/assets/ef9d9d88-3b94-451d-969d-dfcebeec1c72" />

Same with the CrackStation website, it is SHA-1 Hash producing 160 bit hash value that was designed in 1995.

Entering the cracked password, we get another hash to find the flag.

<img width="600" height="250" alt="Screenshot 2025-11-25 224016" src="https://github.com/user-attachments/assets/547e948d-1fb7-4421-b1d9-69d99c821da9" />

Same with CrackStation, it is SHA-256 Hash producing 256 bit (32 byte) hash value that was designed in 2001.

Entering the cracked password, we get the flag!

<img width="700" height="250" alt="Screenshot 2025-11-25 224448" src="https://github.com/user-attachments/assets/be027924-3482-4c39-b07d-ec43ffdde69f" />









