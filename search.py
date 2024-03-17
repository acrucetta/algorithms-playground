from typing import List


def binary_search(lst: List[int], target: int, low:int=0, high=None) -> int:
    if high is None:
        high = len(lst) - 1

    if low > high:
        return -1

    mid = (low + high) //2
    mid_val = lst[mid]

    if mid_val > target: # take left side (e.g target (2) < 4)
        binary_search(lst, target, low , mid-1)
    elif mid_val < target:
        binary_search(lst[mid:],target, mid+1,high)
    else:
        print(f"Found {mid_val}")
        return mid

def main():
    arr = [1,3,4,51,12,23,45]
    resp = binary_search(arr,2)
    if resp == 0:
        print("No value found")
    print("Value found!")
    return ""

if __name__ == "__main__":
    main()
