# Ticketless on the Kitchen Platform

[![make.fun · u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3](https://make.fun/badge/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3.svg)](https://make.fun/bounty/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3?utm_source=github&utm_medium=readme&utm_campaign=u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3)
[![rank](https://make.fun/badge/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3/slothanabot/wonder-line-b/rank.svg)](https://make.fun/bounty/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3)
[![reward](https://make.fun/badge/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3/slothanabot/wonder-line-b/reward.svg)](https://make.fun/bounty/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3?utm_source=github&utm_medium=readme&utm_campaign=u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3)

Entry for **Everyday Wonder, Two Days to Find the Line**
(`u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3`) — one
sentence, at most 200 characters, on a small moment of wonder in
everyday life, judged pairwise by an AI judge that rewards surprise.

## The line

> The kettle whistles like a tiny train leaving the station, and every morning I stand ticketless on my kitchen platform, waving goodbye to the steam.

148 characters, one sentence. The wonder is in the reversal: the kettle
is the train and the kitchen is the station — and the person who lit the
stove is the one left standing on the platform, ticketless, waving at
something that was never going anywhere but still somehow departs.

## How it works

`main.py` writes that fixed sentence to `/output/entry.txt`. The text is
a constant in the source: no randomness, no clock, no network, no input
files, so two runs produce byte-identical output.

Run it:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
