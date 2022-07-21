# uwctf-s22/noob/Meow

> Points: 24

## Question

> Author: Raymo

Please talk to `ctf.csclub.uwaterloo.ca` on the alternative port for HTTP, it will meow you your flag.

## Solution

<details>
  <summary>Spoiler</summary>

The hint to connect "on the alternative port for HTTP" seems to indicate ports `8000` or `8080` by convention. Connecting via a normal HTTP connection (e.g., with `curl`) times out on `8000` but errors out on `8080`, seeming to indicate that `8080` is the port we want to target.

```sh
$ curl ctf.csclub.uwaterloo.ca:8000
curl: (28) Failed to connect to ctf.csclub.uwaterloo.ca port 8000 after 75017 ms: Operation timed out

$ curl ctf.csclub.uwaterloo.ca:8080
curl: (1) Received HTTP/0.9 when not allowed
```

All the cat references seem to indicate we might try connecting with [netcat](https://en.wikipedia.org/wiki/Netcat) ("noob/Meow", "it will meow you your flag"), and running `nc ctf.csclub.uwaterloo.ca 8080` does in fact meow back the flag!

</details>

## Flag

<details>
  <summary>Spoiler</summary>

`uwctf{netcat_bcf2e43f3c9e97e9}`

</details>
