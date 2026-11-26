# One Line, One Minute: The Vending Machine Pickup Line Contest

[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee.svg)](https://make.fun/c/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/Fauziwildan0856/makefun-vending-pickup/rank.svg)](https://make.fun/c/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/Fauziwildan0856/makefun-vending-pickup/reward.svg)](https://make.fun/c/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)

Entry for the [make.fun](https://make.fun/c/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee) bounty **"One Line, One Minute: The Vending Machine Pickup Line Contest"** — one pickup line, 200 characters at most, spoken by a vending machine to a passing human: its hum, its spinning coils, its jealous snacks, and the button that turns out to be the machine itself.

## The entry

> Hey gorgeous — I've been humming all day, my coils are spinning, and every snack in here is jealous. Press B7... that's me.

## How it works

`main.py` (Python 3, standard library only) writes the pickup line to `MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt` when the variable is unset), and checks it against the kit gate first: UTF-8 text, 1–200 characters, not only whitespace, exactly one line.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
