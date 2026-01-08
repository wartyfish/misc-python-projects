# secret_santa.py
The script randomly simulates drawing names from a hat to pair each participant with someone else.

It works by randomly dividing participants into groups and then creating derangements within each group: pairings where no one is assigned to themselves.
These groups-level pairings are then merged into a single global draw. 

The script ensures that:
1. no one one draws themself
2. every participant gives and receives exactly one gift
3. no two people are assigned to one another (minimum group size set to 3 by default, but this is programmable)
4. the draw succeeds every time without retries

# Future features:
1. somehow implement ability to ban certain pairings (eg couples can't gift each other)