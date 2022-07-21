# uwctf-s22/noob/Passwords

> Points: 49

## Question

> Raymo

Charlie the C programmer forgot his password that will make the program print his flag! He also accidentally deleted his original source file, and may have made a mistake writing it in the first place...

Bonus chall: figure out what the mistake Charlie made was :)

[a.out](attachments/Passwords/a.out)

## Solution

<details>
  <summary>Spoiler</summary>

The hardest part of this challenge was getting the executable to run! 😞

We're told this is a C program, so we know we need to find a way to run this on the correct platform. Inspecting the first few bytes of the executable reveals it's a file in [ELF format](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format), which is common on Unix systems. After pulling down a few assorted docker images, the latest Arch Linux image is able to run this executable. We see:

```
Password:
```

Inspecting the executable binary again and searching for "Password:", we see the string "correct_horse_battery_staple" (classic). Trying this as the password and sending `EOF` (`CTRL-D`) prints the flag (a lot).

Side note: I never did figure out the mistake Charlie made...

</details>

## Flag

<details>
  <summary>Spoiler</summary>

`uwctf{xkcdgoodpasswd_4676d47590b4876e}`

</details>
