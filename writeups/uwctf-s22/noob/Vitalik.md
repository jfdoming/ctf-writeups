# uwctf-s22/noob/Vitalik

> Points: 49

## Question

> Author: Rahul

Vitalik's creation uses a hashing function. Find our path to the mapping for nothing.

## Solution

<details>
  <summary>Spoiler</summary>

Vitalik Buterin is a famous (notorious?) University of Waterloo graduate (founder of Ethereum), who coincidentally is the first person to pop up on Google when searching "Vitalik." His "creation" almost certainly refers to Ethereum, and a quick search reveals that Ethereum uses an algorithm called `Keccak-256`. This algorithm accepts "null" (empty) input, and the resulting hash is `c5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470`. Treating this as a "path" on the CTF website (as hinted) downloads a file which contains the flag.

An interesting note: When I originally solved this challenge, I was the only one who did, so it was worth 50 points. Now it's worth only 49... deflation? 😛

</details>

## Flag

<details>
  <summary>Spoiler</summary>

`uwctf{6c48c02b6682151e}`

</details>
