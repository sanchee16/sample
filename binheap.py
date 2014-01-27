'''priority queue in which you dequeue from front with highest priority at front.Best part is its complixity is O(log n).
BinHeap allows us to dequeue and enqueue in O(log n).Thus when you enqueue an item on a priority queue, the new item may move all the way to the front. 
Min heap max heap
Opertions:
BinHeap() creates a new, empty, binary heap.
insert(k) adds a new item to the heap.
findMin() returns the item with the minimum key value, leaving item in the heap.
delMin() returns the item with the minimum key value, removing the item from the heap.
isEmpty() returns true if the heap is empty, false otherwise.
size() returns the number of items in the heap.
buildHeap(list) builds a new heap from a list of keys.
Balanced complete binary tree-left to right.
Parent Node at p- child nodes-2p n 2p+1.
A priority queue is not a heap. A priority queue is an abstract concept like "a list" or "a map"; 
just as a list can be implemented with a linked list or an array, a priority queue can be implemented with a heap or a variety of other methods.
To improve performance, priority queues typically use a heap as their backbone, giving O(log n) performance for inserts and removals, 
and O(n) to build initially. Alternatively, when a self-balancing binary search tree is used, insertion and removal also take O(log n) time, 
although building trees from existing sequences of elements takes O(n log n) time; 
this is typical where one might already have access to these data structures, such as with third-party or standard libraries.
There are several specialized heap data structures that either supply additional operations or outperform these approaches. 
The binary heap uses O(log n) time for both operations, but also allows queries of the element of highest priority without removing it in constant time.
Binomial heaps add several more operations, but require O(log n) time for requests. 
Fibonacci heaps can insert elements, query the highest priority element, and increase an element's priority in amortized constant time,
though deletions are still O(log n). Brodal queues can do this in worst-case constant time.

Used in 
1.Bandwidth management
2.Discreet event simulation
3.Dijkstras algorithm
4.Huffman Coding
5.A* and SMA*
6.ROAM triangulation algorithm '''


class BinHeap:
	def __init__(self):
		self.heapList=[0]
		self.currentSize=0

	def percUp(self,i):
		while i//2>0:
			if self.heapList[i]<self.heapList[i//2]:
				tmp=self.heapList[i//2]
				self.heapList[i//2]=self.heapList[i]
				self.heapList[i]=tmp
			i=i//2

	def insert(self,k):
		self.heapList.append(k)
		self.currentSize=self.currentSize+1
		self.percUp(self.currentSize)

	def minChild(self,i):
		if i*2+1>self.currentSize:
			return i*2
		else:
			if self.heapList[i*2]<self.heapList[i*2+1]:
				return i*2
			else:
				return i*2+1

	def percDown(self,i):
		while (i*2)<=self.currentSize:
			mc=self.minChild(i)
			if self.heapList[i]>self.heapList[mc]: #use tuples
				tmp=self.heapList[i]
				self.heapList[i]=self.heapList[mc]
				self.heapList[mc]=tmp
			i=mc

	def delMin(self):
		retval=self.heapList[1]
		self.heapList[1]=self.heapList[self.currentSize]
		self.currentSize=self.currentSize-1
		self.heapList.pop()
		self.percDown(1)
		return retval

	def buildHeap(self,alist):
		i=len(alist)//2
		self.currentSize=len(alist)
		self.heapList=[0]+alist[:]
		while i>0:
			self.percDown(i)
			i=i-1

#using dictionaries