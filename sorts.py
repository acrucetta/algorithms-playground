from typing import List

def merge_sort(arr : List[int]) -> List[int]:
    # We need to split the array until we have 1 element in each, then
    # we compare the two elements and feed them back
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    return merge(left_sorted, right_sorted)

def merge(left : List[int], right : List[int]) -> List[int]:
    
    merged_lst = []
    left_idx, right_idx = 0, 0
    
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged_lst.append(left[left_idx])
            left_idx+=1
            continue
        merged_lst.append(right[right_idx])
        right_idx+=1
    
    merged_lst.extend(left[left_idx:])
    merged_lst.extend(right[right_idx:])
    
    return merged_lst

def main():
    arr = [1,3,4,51,12,23,45]
    sorted = merge_sort(arr)
    print(sorted)
    return sorted

if __name__ == "__main__":
    main()
