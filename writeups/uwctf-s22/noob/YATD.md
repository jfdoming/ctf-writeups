# uwctf-s22/noob/YATD

> Points: 48

## Question

> Raymo

Yet another cipher to decode:

```
FH4E7LC@Ecf0243hbfh37_ge35fcN
```

## Solution

<details>
  <summary>Spoiler</summary>

In line with the previous cipher challenge, we might think to try a ROT cipher. However, this ciphertext contains symbols, so that indicates the previous ROT13 will not work. Trying ROT47 (for printable ASCII characters) on the first five characters gives `uwctf`, providing an indication that this cipher will give the flag.

</details>

## Flag

<details>
  <summary>Spoiler</summary>

`uwctf{rot47_acb9379bf086bd74}`

</details>
