# Log Hunt 🔎🧾

## Description

Our server seems to be leaking pieces of a secret flag in its logs. The parts are scattered and sometimes repeated. Can you reconstruct the original flag?

Download the logs and figure out the full flag from the fragments.

## Solution

By downloading the logs and opening this file in Notepad, we can see important part in the logs as INFO FLAGPART: which indicates the contents of the flag that will be combined to reveal the full flag.

The first part is INFO FLAGPART: picoCTF{us3_

Second part is INFO FLAGPART: y0urlinux_

Third part is INFO FLAGPART: sk1lls_

And final part is INFO FLAGPART: cedfa5fb}

Combining all these parts will reveal the flag!
