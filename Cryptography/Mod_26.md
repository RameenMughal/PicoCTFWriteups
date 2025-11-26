# Mod 26

## Description

Cryptography can be easy, do you know what ROT13 is? 

`cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_nSkgmDJE}`

## Solution

This challenge focuses on a classic substitution cipher based on modulo 26 arithmetic. The title “Mod 26” hints at operations on the 26 letters of the English alphabet, commonly used in simple ciphers. 

The description references ROT13, a well-known cipher that shifts each letter by 13 positions using the formula `(x + 13) mod 26`. 

Since the alphabet length is 26, applying ROT13 twice returns the original text.

Putting the ciphertext in [CyberChef](https://gchq.github.io/CyberChef/) website and selecting ROT13 with `amount = 13` (by default), then we get the flag!

<img width="700" height="300" alt="Screenshot 2025-11-26 150158" src="https://github.com/user-attachments/assets/39d9c86e-b8d1-46ee-b257-58b306e5aac8" />



