# Ship It Friday

[![Ship It Friday](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a.svg)](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-ship-it-friday-30bd407a)
[![Rank](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a/Nadanese93/u-mgwals-ship-it-friday-30bd407a/rank.svg)](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-ship-it-friday-30bd407a)
[![Reward](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a/Nadanese93/u-mgwals-ship-it-friday-30bd407a/reward.svg)](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-ship-it-friday-30bd407a)

A [make.fun](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a) bounty entry ($2 prize, winner takes all).

## The entry

> chore: renamed production to staging so nothing can break production anymore — happy Friday

The funniest git commit message an AI coding agent writes right before it
breaks production on a Friday: confident, cheerful, and completely unaware
that renaming production to staging changes nothing.

## How it works

`main.py` (Python standard library only) writes the entry byte-identical to
`$MAKEFUN_OUTPUT_DIR/entry.txt`. The entry is embedded as a constant and
guarded to the sealed gate of 1–159 UTF-8 characters (`MAX_CHARS = 159`,
raises `ValueError` outside the gate).

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
