# uwctf-s22/noob/WASM

> Points: 36

## Question

> Author: Rahul

https://ctf.csclub.uwaterloo.ca/ctf-uploads/noob/wasm/chall.html

## Solution

<details>
  <summary>Spoiler</summary>

A quick visit to the linked page reveals some text:

```
check_flag() likes technology's blue, red, yellow, blue, green, red.
```

This seems to hint that there's a function called `check_flag` which we can call; indeed, inspect element reveals such a function. However, the implementation of the function is hidden in Web Assembly! Thus, we must rely on the other portion of the hint: the sequence of colours in "technology's blue, red, yellow, blue, green, red" matches the colours in the Google logo, and indeed, `check_flag("Google")` returns the flag.

</details>

## Flag

<details>
  <summary>Spoiler</summary>

`uwctf{W45M_4772a105377592cd}`

</details>
