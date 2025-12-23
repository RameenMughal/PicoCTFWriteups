# interencdec

## Description

Can you get the real meaning from this file.

By downloading the file we get encrypted flag `YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclgya3lNRFJvYTJvMmZRPT0nCg==`

## Solution

By the `==` sign it is encrypted with base64 so using CyberChef and choosing From Base64 to get the output

<img width="740" height="278" alt="image" src="https://github.com/user-attachments/assets/4d97bb94-26f3-490d-ba36-c5484eb43b09" />

The `b'...'` is just Python's way of showing that the value is a bytes object meaning each character inside the quotes (like `d`, `3`, `B`, `q`, …) is 1 byte.

Therefore, inside the `b'...'` is the actual string which is `d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX2kyMDRoa2o2fQ==` and this is still encrypted with base64.

Again doing the From Base 64 as this the input and getting the output

<img width="600" height="281" alt="image" src="https://github.com/user-attachments/assets/465c8869-569c-46db-beba-ebff88888105" />

We get the formatted flag but alphabets are mixed up so we can focus on that the format of the flag is `picoCTF{}` so the first letter is `w` (position 23) and we want `p` (position 16).

The difference between the position of `w` and `p` is 7 and we want to shift backward 7 times to get the `p`. This is about ROT13, a specific type of Ceaser Cipher.

Putting this text in the input and choosing ROT13 with `Amount = -7` as we want to shoft backward 7 times and we get the flag!

<img width="527" height="290" alt="rot13" src="https://github.com/user-attachments/assets/446a92a6-67e0-4396-9718-5c6273eb6119" />
