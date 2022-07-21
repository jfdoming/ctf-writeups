# uwctf-s22/noob/Strings, literally

> Points: 32

## Question

> Author: Raymo

Uh oh! GIMP corrupted my file while I was making a steg chall, can you still find the flag?

[steg.xcf](attachments/Strings%2C%20literally/steg.xcf)

## Solution

<details>
  <summary>Spoiler</summary>

The challenge title hints at opening the attachment in a text editor; doing so and searching for `uwctf` reveals the flag.

Fun fact: Apparently, the intended solution used the `strings` utility on Linux to get the flag directly. Who would have thought, considering the title of the challenge...

</details>

## Flag

<details>
  <summary>Spoiler</summary>

`uwctf{h1dd3n5t3g_54c10511eda3e8f9}`

</details>
