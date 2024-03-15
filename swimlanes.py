
from typing import List, Tuple

"""

Events -> (1,2) , (2,4) ...

Swim Lanes
    (1,2) (2,4)
    (1,3) (3,5)
    (2,5) (5,10)
    ...

Sort the events. Then place it in the first swim lane it matches. If it doesn't
match in that swim lane, try the next one. If it doesn't match any of the
swim lanes, place it in a new one and add that swim lane to the list
we're iterating through.

Overlapping events: (1,2) (1,3);
Not overlapping: (1,2) (2,3);

Edge cases:
- Empty events
- All events overlap
- No events overlap


"""

def print_swimlane(events : List[Tuple[int,int]]) -> List[List[Tuple[int,int]]] | None:
    """
    Given a list of events, return a list of strings representing the events in a swimlane format.
    """
    if not events:
        raise ValueError("No events provided.")

    events.sort(key=lambda x:x[0])

    swimlanes = [[events[0]]]

    for event in events:
        start, end = event[0], event[1]
        placed = False
        for lane in swimlanes:
            if lane:
                # Check the current start/end doesn't overlap
                last_start, last_end = lane[-1]
                print(f"Last event: {last_start}, {last_end}")
                if start>=last_end and end>=last_end:
                    print(f"Adding event {start},{end} to current swimlane {lane}")
                    lane.append(event)
                    placed = True
                    break
        if not placed: # If we didn't find a place to put the event, create a new swimlane
            print(f"Didn't find a match for event {start},{end}")
            swimlanes.append([event])
    print(swimlanes)
    return swimlanes

def main():
    events = [(1,2),(3,4),(5,6)]
    events_overlap = [(1,2),(2,3),(2,4),(3,4),(4,5),(5,6)]
    # print_swimlane(events)
    print_swimlane(events_overlap)

if __name__ == "__main__":
    main()
