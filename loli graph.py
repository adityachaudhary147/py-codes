#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 
from tkinter import *
root=Tk()
global values
values=[10-i for i in range(10)]
 
# plot with no marker
plt.stem(values, markerfmt=' ')
#plt.show()
 
# change color and shape and size and edges
(markers, stemlines, baseline) = plt.stem(values)
plt.setp(markers, marker='D', markersize=10, markeredgecolor="orange", markeredgewidth=2)
# plt.show()
c = Canvas(root, width=700, height=550, bg='white')

def update(values):
    l=values
    n = len(l)
    for i in range(n):
        height = l[i] * 500 / max(l)
        c.create_rectangle(i * 700 / n, 500 - height, (i + 1) * 700 / n, 500, fill="green")
        c.create_text(i * 700 / n, 0, text=str(l[i]))

def bubblesort(arr):
     n = len(arr)
 
     # Traverse through all array elements
     for i in range(n):
 
          # Last i elements are already in place
          for j in range(0, n-i-1):
 
                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if arr[j] > arr[j+1] :
                     arr[j], arr[j+1] = arr[j+1], arr[j]
                yield arr
def sort():
    global values
    root.after(1000)
    update(values)
    root.update()

    b=bubblesort(values)
    for w in b:
        # time.sleep(0.0003)
        c.delete("all")
        coun=0
        while coun!=1000:
            coun+=1
        update(w)
        root.update()
        root.after(100)
c.pack()
mybutton=Button(root,text="sort",command=sort)
mybutton.pack()
root.mainloop()