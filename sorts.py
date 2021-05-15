import random
import time
import tkinter
import animation
import matplotlib.pyplot as plt

def mergeSort(nums: list):
    if len(nums) > 1:
        mid = len(nums)//2
        l = nums[:mid]
        r = nums[mid:]

        mergeSort(l)
        mergeSort(r)
        i = j = k = 0

        while j < len(l) and k < len(r):
            if l[j] < r[k]:
                nums[i] = l[j]
                j += 1
            else:
                nums[i] = r[k]
                k += 1
            i += 1
        
        while j < len(l):
            nums[i] = l[j]
            j += 1
            i += 1
        
        while k < len(r):
            nums[i] = r[k]
            k += 1
            i += 1

def selectionSort(nums):
    for i in range(len(nums)):
        min_idx = i
        for j in range(i+1, len(nums)):
            if nums[min_idx] > nums[j]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]

def insertionSort(nums):
    for i in range(1, len(nums)):
        curr_val = nums[i]
        j = i
        while j > 0 and nums[j-1] > curr_val:
            nums[j] = nums[j-1]
            j -= 1
        nums[j] = curr_val
            

def bubbleSort(nums):
    for i in range(len(nums)):
        for j in range(0, len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
        
    

def quickSort(nums, i, j):
    if i < j:
        pivot = partition(nums, i, j)

        quickSort(nums, i, pivot-1)
        quickSort(nums, pivot+1, j)

def partition(nums, i, j):
    
    # pivot_index = j
    
    # median of three
    # pivots = sorted([random.randint(i, j),random.randint(i, j),random.randint(i, j)])
    # pivoter = pivots[1]

    #random pivot
    #pivoter = random.randint(i, j)

    #nums[pivoter], nums[j] = nums[j], nums[pivoter]

    pivot_index = i
    pivot = nums[pivot_index]

    while i < j:
        while i < len(nums) and nums[i] <= pivot:
            i += 1
        while nums[j] > pivot:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    nums[pivot_index], nums[j] = nums[j], nums[pivot_index]

    return j
    
def binarySearch(nums, start, end, num_to_find):
    if len(nums) > 1:
        mp = (start+end) // 2

        if nums[mp] == num_to_find:
            return mp

        if nums[mp] > num_to_find:
            return binarySearch(nums, start, mp, num_to_find)
        else:
            return binarySearch(nums, mp, end, num_to_find)
    elif nums[start] == num_to_find:
        return start

def linearSearch(nums, num_to_find):
    for i in range(len(nums)):
        if nums[i] == num_to_find:
            return i


def randomList(size):
    rand_list = []
    for i in range(size):
        rand_list.append(random.randint(0, 100000))
    
    return rand_list

def runSorter(sortType, size):
    nums = randomList(size)

    if sortType == "ss":
        start_time = time.time()
        selectionSort(nums)
        time_taken = time.time() - start_time
    elif sortType == "is":
        start_time = time.time()
        insertionSort(nums)
        time_taken = time.time() - start_time
    elif sortType == "ms":
        start_time = time.time()
        mergeSort(nums)
        time_taken = time.time() - start_time
    elif sortType == 'qs':
        start_time = time.time()
        quickSort(nums, 0, len(nums)-1)
        time_taken = time.time() - start_time
    elif sortType == 'bs':
        start_time = time.time()
        bubbleSort(nums)
        time_taken = time.time() - start_time
    elif sortType == 'ts':
        start_time = time.time()
        sorted(nums)
        time_taken = time.time() - start_time
    elif sortType == 'bins':
        to_find = nums[random.randint(0, len(nums)-1)]
        mergeSort(nums)

        start_time = time.time()
        found_index = binarySearch(nums, 0, len(nums), to_find)
        time_taken = time.time() - start_time
        print(f'To find: {to_find}, Found: {nums[found_index]}')
    elif sortType == 'lins':
        to_find = nums[random.randint(0, len(nums)-1)]

        start_time = time.time()
        found_index = linearSearch(nums, to_find)
        time_taken = time.time() - start_time

        print(f'To find: {to_find}, Found: {nums[found_index]}')
    else:
        return 0.0



    
    print(f'--- {sortType} took {time_taken} seconds for a {size} element list ---')

    return time_taken




if __name__ == "__main__":
    main()