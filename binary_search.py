def binarySearch (arr, l, r, x): 
 
	if r >= l: 

		mid = l + (r - l) // 2

		# If element is present at the middle itself 
		if arr[mid] == x: 
			return mid 
		
		# If element is smaller than mid, then it 
		# can only be present in left subarray 
		elif arr[mid] > x: 
			return binarySearch(arr, l, mid-1, x) 

		# Else the element can only be present 
		# in right subarray 
		else: 
			return binarySearch(arr, mid + 1, r, x) 

	else: 
		# Element is not present in the array 
		return -1
#One thing to note here is that we have to provide a sorted list for binary search to work!
arr = [ 34, 35, 78, 100, 480 ] 
x = 100
result = binarySearch(arr, 0, len(arr)-1, x) 
if result != -1: 
	print ("Found at position % d" % result) 
else: 
	print ("Element is not present in array") 

