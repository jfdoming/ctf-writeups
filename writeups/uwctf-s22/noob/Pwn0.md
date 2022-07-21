# uwctf-s22/noob/Pwn0

> Points: 44

## Question

> Jazzy

`nc uwctf.ml 6001`

[chall0.c](attachments/Pwn0/chall0.c)

## Solution

<details>
  <summary>Spoiler</summary>

Based on the message that greets you upon entering the hint command (as well as the source code), we probably need to overflow a buffer in the program:

```
Welcome to Buffer Overflow 0
Can you hack me?
```

A good first thing to try with buffer overflows is overflowing the buffer (😛). In this case, that's actually all that's needed! Typing `AAAAAAAAAAAAAAAAAAAAA` and pressing enter immediately prints the flag.

</details>

## Flag

<details>
  <summary>Spoiler</summary>

`uwctf{buff3r0v3rf10w0_3f8361abc77504c5}`

</details>
