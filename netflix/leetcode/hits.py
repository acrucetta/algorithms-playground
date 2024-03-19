# Design a hit counter which counts the number of hits received in the past 5 minutes.

# Each function accepts a timestamp parameter (in seconds granularity) and
# you may assume that calls are being made to the system in chronological
# order (ie, the timestamp is monotonically increasing).
# You may assume that the earliest timestamp starts at 1.

# It is possible that several hits arrive roughly at the same time.

"""
HitCounter counter = new HitCounter();

// hit at timestamp 1.
counter.hit(1);

// hit at timestamp 2.
counter.hit(2);

// hit at timestamp 3.
counter.hit(3);

// get hits at timestamp 4, should return 3.
counter.getHits(4);

// hit at timestamp 300.
counter.hit(300);

// get hits at timestamp 300, should return 4.
counter.getHits(300);

// get hits at timestamp 301, should return 3.
counter.getHits(301);

Approach:

Data Structures
- Receiving hit (1) at timestamp
- Need to get the # of hits < timestamp

Strategies:
- Array of timestamps where we increment the value at idx
based on the # of hits.
    Pros: easy to calculate; relatively low footprint
    Cons: what if we add a lot of hits long into the future
    the array would grow at O(N); what if we have long
    periods without hits
- Dict of timestamps; we would have a ts a counter at each
    one {ts:hits}
    Pros: easier to manage than the array; easy to allocate high
    ts values without impacting the memory as much
    Cons: rehashing if we receive a lot of hits at a given time

What if the number of hits per second could be very large? Does your design scale?
Ans: Nope, because we need to sort each time we call get_hits

Alternative:
Use a binary search tree (BST) or a self-balancing BST like a
Red-Black Tree to store the timestamps and their corresponding hit counts.
This will allow for efficient insertion and retrieval of hits based on
timestamps. The time complexity of insertion and retrieval in a balanced
BST is O(log n), where n is the number of unique timestamps.
"""

from dataclasses import dataclass

class Node:
    def __init__(self, timestamp, hits) -> None:
        self.timestamp = timestamp
        self.hits = hits
        self.left = None
        self.right : None

def insert(node, timestamp): # O(logN)
    if not node:
        return Node(timestamp, 1)
    if timestamp > node.timestamp:
        node.left =  insert(node.left, timestamp)
    elif timestamp < node.timestamp:
        node.right = insert(node.right, timestamp)
    else: # Found a matching timestamp; return Node with increased hit counter
        node.hits += 1
    return node

def search(node, timestamp): # O(logN)
    if not node:
        return 0
    if timestamp > node.timestamp:
        return search(node.right, timestamp)
    elif timestamp < node.timestamp:
        return search(node.left, timestamp)
    return node.hits

class HitCounter:

    def __init__(self) -> None:
        self.hits = {}

    def hit(self, timestamp:int) -> None:
        self.hits[timestamp] = self.hits.get(timestamp,0) + 1 # O(1)

    def get_hits(self, timestamp:int) -> int:
        sorted_hits = dict(sorted(self.hits.items())) # O(nlogn)
        hit_tally = 0
        print(f"Sorted hits {sorted_hits}")
        for ts, hits in sorted_hits.items(): # O(n)
            if ts <= timestamp:
                print(f"Adding {hits} hits from timestamp {ts}")
                hit_tally += hits
            else:
                break
        print(f"Total hit tally: {hit_tally}")
        return hit_tally


counter = HitCounter();
counter.hit(1);
counter.hit(2);
counter.hit(3);
hits = counter.get_hits(4);
assert hits == 3, f"got {hits} expected 3"

counter.hit(300);
counter.get_hits(300);
assert hits == 3
