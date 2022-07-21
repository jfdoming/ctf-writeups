# uwctf-s22/noob/steg

> Points: 48

## Question

> Raymo

Yes, it's been there on the homepage all this time. https://ctf.uwaterloo.ca/

## Solution

<details>
  <summary>Spoiler</summary>

A quick Google of the term "steg" reveals this challenge is likely related to [steganography](https://en.wikipedia.org/wiki/Steganography). The only image available on the linked website is the background image. Visiting the publicly linked Gitlab on the website, we can see there is [an additional image available for download](attachments/steg/background_nochall.png) from the same directory in which the background image is hosted. Going back to the original website and downloading both, diffing the images with the `compare` utility from ImageMagick yields the flag:

```sh
compare background* -compose src result.png
```

</details>

## Flag

<details>
  <summary>Spoiler</summary>

`uwctf{stegfrthistime_9b0a89e16a81af67}`

</details>
