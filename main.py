import random
import time
import tkinter
import matplotlib.pyplot as plt
from sorts import runSorter

def main():
    sorts = input("Enter sort\n 'ms' for mergesort,\n 'ss' for selection sort,\n 'is' for insertion sort,\n 'qs' for quick sort,\n 'bs' for bubble sort,\n or 'all' for all sorts\n")
    if sorts == 'all':
        sorts = ['ss', 'ms', 'qs', 'is', 'bs']
    else:
        sorts = sorts.split()
    max_size = int(input('Enter max array elements\n'))
    inc = int(input('Enter size increment\n'))


    sizer = [x for x in range(inc, max_size+inc, inc)]
    print(sizer)
    timer = {"ss": [], "ms": [], "is": [], "qs": [], "bs": []}
    

    for srt in sorts:
        for sze in sizer:
            single_time = runSorter(srt, sze)
            timer[srt].append(single_time)

    for sort in timer.keys():
        if timer[sort] != []:
            plt.plot(sizer, timer[sort], label=sort)
    
    plt.xlabel('Size of array')
    plt.ylabel('Time take in seconds')
    plt.title(f"Sorting Algorithms")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()