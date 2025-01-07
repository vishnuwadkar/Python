#BINARY SEARCH -> Searching technique to search the element in the sorted array

def binarySearch(list,target):
    low, high = 0, len(list) - 1
    count = 1   #to count the number of iterations
    while low<=high:    #till there is atleast one element in the list
        mid = (low+high)//2 #find the middle element; // because / returns a floating point
    
        if list[mid] == target : #if the middle element is the target
            while list[mid] == list[mid-1]: #if the target repwats, check first if it is the first occurrence
                mid = mid-1     #if not, then shift mid to first occurrence
            return mid,count #return the index of the target
        elif list[mid]<target:  #when the mid is lesser than target
            count += 1
            low = mid+1     #set the low as the next element of mid i.e search the right side of the array
        elif list[mid]>target:      #when the mid is greater than target
            count += 1
            high = mid-1        #set the high as the previous element of mid i.e search the left side of the array
    else:
        return -1 #if the target is not found in the list
    
# l = [19,15,14,13,9,7,4,3,2]
l = []
for i in range(1000000,0,-1):       # a bigger test case
    l.append(i)
myCards = list(reversed(l))
# print(myCards) #print the list in reverse order
target = 990112
output = 4
print(f"The binary search is : {binarySearch(myCards,target)[0]} in {binarySearch(myCards,target)[1]} iterations") #output: 4


