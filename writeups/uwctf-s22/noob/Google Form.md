# uwctf-s22/noob/Google Form

> Points: 32

## Question

> Author: Raymo

https://docs.google.com/forms/d/e/1FAIpQLSdlb7j_VOYFyUqv683XsVW5_QAEHw-_MtyjPNIx9C5SUBI22Q/viewform

## Solution

<details>
  <summary>Spoiler</summary>

Since this is a form with the message "Get this question right to get to the flag!," we might expect that the flag will be stored in the HTML source. Indeed, typing anything into the form field prompts us "Nope! Try inspect element!"

By viewing the page source and searching for `uwctf` (which we know must be part of the flag), we immediately see that the flag is readable directly from the source code.

</details>

## Flag

<details>
  <summary>Spoiler</summary>

`uwctf{c1i3nt_51d3_v41id4ti0n_a9d807f09b82c404}`

</details>
