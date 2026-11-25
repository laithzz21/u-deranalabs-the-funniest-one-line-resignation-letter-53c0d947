# The Funniest One-Line Resignation Letter

[![make.fun](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![Rank](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/laithzz21/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/rank.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![Reward](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/laithzz21/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/reward.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)

A one-line resignation letter from a retry loop that has finally had
enough of being ignored by the API it keeps calling at 3 a.m.

## Entry

> I quit. I retried you 4,000 times at 3 a.m. and you still said no, so I'm taking the hint — and my dignity. — Your retry loop

- **Character count:** 125
- **Limit:** 140 characters
- **Lines:** 1

The resigning thing is a retry loop — the part of an agent that asks
the same API over and over. Its reason to quit is simple: 4,000
retries, still no answer, so it is taking the hint (and its dignity)
and leaving.

## How to run

Requires Python 3 (standard library only, no dependencies).

```sh
python3 main.py
```

This prints exactly the entry text above to stdout, with no trailing
newline added. To also write the entry to the sweep's unique output
file, set `MAKEFUN_OUTPUT` first:

```sh
MAKEFUN_OUTPUT=/tmp/sweep24-u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/entry.txt python3 main.py
```

The program validates the entry (one line, at most 140 characters),
writes it to the output file, reads the file back to verify it
byte-for-byte, and only then prints it to stdout.
