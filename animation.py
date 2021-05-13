from tkinter import *
import time


def displayArray():
    divider = 1000/len(numers)
    last_x1 = divider*-1
    last_x2 = 0

    max_element = max(numers)

    for i in numers:
        height = i/max_element
        canvas.create_rectangle(last_x1+divider, 500-(500*height), last_x2+divider, 500)
        last_x1 += divider
        last_x2 += divider


    # canvas.create_rectangle(last_x1+divider, 300, last_x2+divider, 500)
    # canvas.create_rectangle(500, 300, 750, 500)
    # canvas.create_rectangle(750, 300, 1000, 500)

if __name__ == "__main__":
    from sorts import randomList, bubbleSort

    numers = randomList(10)

    root = Tk()
    canvas = Canvas(width=1000, height=500, bg='white')
    canvas.pack()


    displayArray()
    bubbleSort(numers)


    root.mainloop()