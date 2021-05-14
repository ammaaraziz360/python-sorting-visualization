from tkinter import *
import time
import random
import sorts

length = 720
width = 1280

def displayArray(nums):
    canvas.delete("all")

    divider = width/len(nums)
    last_x1 = divider*-1
    last_x2 = 0

    max_element = max(nums)

    for i in nums:
        height = i/max_element
        canvas.create_rectangle(last_x1+divider, length-(length*height), last_x2+divider, length)
        last_x1 += divider
        last_x2 += divider
    
    root.update()

def bubbleSort(nums):
    for i in range(len(nums)):
        for j in range(0, len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
        
        displayArray(nums)

def insertionSort(nums):
    for i in range(1, len(nums)):
        curr_val = nums[i]
        j = i
        while j > 0 and nums[j-1] > curr_val:
            nums[j] = nums[j-1]
            j -= 1
            displayArray(nums)
        nums[j] = curr_val

def selectionSort(nums):
    for i in range(len(nums)):
        min_idx = i
        for j in range(i+1, len(nums)):
            if nums[min_idx] > nums[j]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
        displayArray(nums)

def quickSort(nums, i , j):
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

    displayArray(numers)
    return j

def merge(arr, start, mid, end):
    start2 = mid + 1
 
    # If the direct merge is already sorted
    if (arr[mid] <= arr[start2]):
        return
 
    # Two pointers to maintain start
    # of both arrays to merge
    while (start <= mid and start2 <= end):
 
        # If element 1 is in right place
        if (arr[start] <= arr[start2]):
            start += 1
        else:
            value = arr[start2]
            index = start2
 
            # Shift all the elements between element 1
            # element 2, right by 1.
            while (index != start):
                arr[index] = arr[index - 1]
                index -= 1
                displayArray(arr)
 
            arr[start] = value
            # Update all the pointers
            start += 1
            mid += 1
            start2 += 1
        displayArray(arr)
 
def mergeSort(arr, l, r):
    if (l < r):
 
        # Same as (l + r) / 2, but avoids overflow
        # for large l and r
        m = l + (r - l) // 2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
 
        merge(arr, l, m, r)

if __name__ == "__main__":

    sorting_algo = input("Enter sort\n 'ms' for mergesort,\n 'ss' for selection sort,\n 'is' for insertion sort,\n 'qs' for quick sort,\n 'bs' for bubble sort\n")
    list_size = int(input("Size of array\n"))

    numers = sorts.randomList(list_size)

    root = Tk()
    canvas = Canvas(width=width, height=length, bg='white')
    canvas.pack()

    displayArray(numers)

    if sorting_algo == 'ms':
        mergeSort(numers, 0, len(numers)-1)
    elif sorting_algo == 'ss':
        selectionSort(numers)
    elif sorting_algo == 'is':
        insertionSort(numers)
    elif sorting_algo == 'qs':
        quickSort(numers, 0, len(numers)-1)
    elif sorting_algo == 'bs':
        bubbleSort(numers)
    else:
        print("Invalid input detected. Try Again.")

    root.mainloop()



    