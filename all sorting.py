import tkinter as tk
import random

# SORTING ALGORITHMS

# BUBBLE SORT
def bubsort(l):
	 last = len(l)
	 swapped = True
	 while swapped:
		  swapped = False
		  for j in range(1, last):
				if l[j - 1] > l[j]:
					l[j], l[j - 1] = l[j - 1], l[j]
					swapped = True
					last = j
					yield l


# INSERTION SORT
def insort(l):
	 for i in range(1, len(l)):
		  curval = l[i]
		  pos = i
		  while pos > 0 and l[pos - 1] > curval:
				l[pos] = l[pos - 1]
				pos -= 1
				yield l
		  l[pos] = curval
		  yield l


# SELECTION SORT
def selsort(l):
	 for i in range(len(l)):
		  min_idx = i
		  for j in range(i + 1, len(l)):
				if l[min_idx] > l[j]:
					 min_idx = j
					 root.update()
					 root.after(slider.get())
		  l[i], l[min_idx] = l[min_idx], l[i]
		  yield l


# MERGE SORT
def merge_sort(arr):
	 n = len(arr) - 1
	 c = 1
	 start = 0
	 end = 0
	 while c <= n:
		  while end < n:
				mid = start + c // 2
				end = start + c
				if (start < n) and (end <= n):
					 yield from merge(arr, start, mid, end)
					 start = end + 1
				else:
					 yield from merge(arr, start - c - 1, start - 1, n)
		  c = 2 * c + 1
		  start = 0
		  end = 0


# Merge Function
def merge(a, l, m, r):
	 n1 = m - l + 1
	 n2 = r - m
	 L = [0] * n1
	 R = [0] * n2
	 for i in range(0, n1):
		  L[i] = a[l + i]
	 for i in range(0, n2):
		  R[i] = a[m + i + 1]
	 i, j, k = 0, 0, l
	 while i < n1 and j < n2:
		  if L[i] > R[j]:
				a[k] = R[j]
				j += 1
		  else:
				a[k] = L[i]
				i += 1
		  k += 1
		  yield a
	 while i < n1:
		  a[k] = L[i]
		  i += 1
		  k += 1
		  yield a
	 while j < n2:
		  a[k] = R[j]
		  j += 1
		  k += 1
		  yield a


# HEAP SORT
def heap_sort(l):
	 n = len(l)
	 yield from buildMaxHeap(l, n)
	 for i in range(n - 1, 0, -1):
		  l[0], l[i] = l[i], l[0]
		  yield l
		  j, index = 0, 0
		  while True:
				index = 2 * j + 1
				if (index < (i - 1) and
						  l[index] < l[index + 1]):
					 index += 1
				if index < i and l[j] < l[index]:
					 l[j], l[index] = l[index], l[j]
					 yield l
				j = index
				if index >= i:
					 break


# Build Heap
def buildMaxHeap(l, n):
	 for i in range(n):
		  if l[i] > l[int((i - 1) / 2)]:
				j = i
				while l[j] > l[int((j - 1) / 2)]:
					 (l[j],
					  l[int((j - 1) / 2)]) = (l[int((j - 1) / 2)],
													  l[j])
					 j = int((j - 1) / 2)
					 yield l


# QUICK SORT
def quick_sort(l, left, right):
	 if left >= right:
		  return
	 pivot_idx = left
	 old_r = right
	 pivot = l[left]
	 left += 1
	 while True:
		  # manual check, does it work when l=pivot_idx, r=l+1 for a[l] <= a[r], and for a[l] > a[r] ?
		  while l[right] > pivot:
				right -= 1
		  if left >= right:
				break
		  while left < right and l[left] <= pivot:
				left += 1
		  # pre-conditions to swap: l == r, or a[l] > pivot from 2nd loop, and a[r] <= pivot from 1st loop
		  l[left], l[right] = l[right], l[left]
	yield l
	 l[pivot_idx], l[right] = l[right], l[pivot_idx]
	 yield l
	 yield from quick_sort(l, pivot_idx, right)
	 yield from quick_sort(l, right + 1, old_r)


# GUI
root = tk.Tk()
root.title('Sorting Visualizer')
root.geometry('800x600')

e = tk.Entry(root)

choice = tk.StringVar(root)

slider = tk.Scale(root, from_=1, to=1000, orient='horizontal')
slider.set(100)

sort_dic = {
	 "bubble": bubsort,
	 "insertion": insort,
	 "selection": selsort,
	 "merge": merge_sort,
	 "heap": heap_sort,
	 "quick": lambda l: quick_sort(l, 0, len(l) - 1)
}
choices = set(sort_dic.keys())
menu = tk.OptionMenu(root, choice, *choices)

lb = tk.Label(root, text='START')
c = tk.Canvas(root, width=700, height=550, bg='white')


def visualize(l):
	 n = len(l)
	 for i in range(n):
		  height = l[i] * 500 / max(l)
		  c.create_rectangle(i * 700 / n, 500 - height, (i + 1) * 700 / n, 500, fill="green")
		  c.create_text(i * 700 / n, 0, text=str(l[i]))


stopped = False
paused = False


def start():
	 global c, delay, stopped, paused
	 stopped = False
	 paused = False
	 root.update()
	 c.delete("all")
	 lb.config(text="this is the array")
	 n = int(e.get())

	 sl = [random.randrange(1,100) for i in range(n, 0, -1)]

	 visualize(sl)
	 root.after(1000)
	 root.update()

	 lb.config(text=choice.get() + " sorting " + e.get() + " values")

	 g = sort_dic[choice.get()](sl)

	 for l_iter in g:
		  c.delete("all")
		  visualize(l_iter)
		  delay = root.after(slider.get())
		  root.update()
		  while paused:
				root.update()
		  if stopped:
				c.delete("all")
				break


def pause():
	 global paused, pause_button
	 if paused:
		  paused = False
		  lb.config(text=choice.get() + " sorting " + e.get() + " values")
		  pause_button.config(text='PAUSE')
	 else:
		  paused = True
		  lb.config(text="paused")
		  pause_button.config(text='CONTINUE')


def stop():
	 global stopped
	 stopped = True
	 lb.config(text="stopped")


buttons = tk.Frame(root)
start_button = tk.Button(buttons, text='GO', command=start)
pause_button = tk.Button(buttons, text='PAUSE', command=pause)
stop_button = tk.Button(buttons, text='STOP', command=stop)

e.pack()
menu.pack()
slider.pack(fill='x', expand=True)
start_button.pack(side='left', fill='x', expand=True)
pause_button.pack(side='left', fill='x', expand=True)
stop_button.pack(side='right', fill='x', expand=True)
buttons.pack()
lb.pack()
c.pack()
root.mainloop()