from BST import BST
import random
import time
import matplotlib.pyplot as plt

def populate(n):
	list = [random.randint(0, n) for i in range(n)]
	bst = BST()
	[bst.append(i) for i in list]
	return (list, bst)

def isin(collection, x):
	if isinstance(collection, BST):
		return collection.isin(x)
	else:
		for item in collection:
			if item == x:
				return True
		return False

def do_search(n):
	list, bst = populate(n)

	list_start = time.time()
	[isin(list, n) for x in list]
	list_end = time.time()

	bst_start = time.time()
	[isin(bst, n) for n in list]
	bst_end = time.time()

	return ((list_end-list_start), (bst_end-bst_start))

def main():
	list_times = []
	bst_times = []

	for i in range(1, 10000, 10):
		times = do_search(i)
		list_times.append(times[0])
		bst_times.append(times[1])

	plt.plot(range(1, 10000, 10), list_times, label='List')
	plt.plot(range(1, 10000, 10), bst_times, label='BST')
	plt.legend()
	plt.show()

main()
