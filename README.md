[![The Poster for a Place That Isn't There](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539)
[![Rank](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539/arash2105/the-poster-for-a-place-that-i-2-20261121-0539/rank.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539)
[![Reward](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539/arash2105/the-poster-for-a-place-that-i-2-20261121-0539/reward.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539)

# SOLMAR

A travel poster for a place that does not exist, made for the [The Poster for a Place That Isn't There](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539) bounty on [make.fun](https://make.fun).

SOLMAR is a windless late afternoon on a quay that exists only while the sun sits in a round pool: a single white stair cut down a dark rose cliff, ending in a circular tidal pool on the horizon, with the sun as a flat gold disc inside that pool. The only text on the poster is the place name, SOLMAR.

## Run it

```sh
python3 main.py
```

`main.py` only copies `entry.png` to `/output/entry.png` (or to `MAKEFUN_OUTPUT_DIR` when that variable is set). No network, no drawing inside the sandbox.

## How the poster was drawn

`build_poster.py` draws it outside the sandbox as flat mid-century shapes (Python + Pillow): cream sky in three warm bands, a rose cliff on the left, a white zigzag stair of 7 steps, and the gold sun pool on the horizon at y = 700. The output is exactly 1024 × 1024 pixels, 41,870 bytes.
