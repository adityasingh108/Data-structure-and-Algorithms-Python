import math 

def bubbleSort(customList):
    for i in range(len(customList) - 1):
        for j in range(len(customList) -i -1):
            if customList[j] > customList[j+1]:
                customList[j] ,customList[j+1] = customList[j+1] ,customList[j]
                
    print(customList)
    
list = [9,6,7,8,4,1,3,2,5]    
# bubbleSort(list)    


def selectionSort(customList):
    for i in range(len(customList)):
        min_index = i
        for j in range(i+1, len(customList)):
            if customList[min_index] > customList[j]:
                min_index = j
        customList[i], customList[min_index] = customList[min_index], customList[i]
    print(customList)          

# selectionSort(list)

def insertionSort(customList):
    for i in range(1,len(customList)):
        key = customList[i]
        j =  i-1
        while  j >= 0 and key < customList[j]:
            customList[j+1] = customList[j]
            j -=1
        customList[j+1] = key
    return customList        


# print(insertionSort(list))

def bucketSort(customList):
    numberOfBuckets = round(math.sqrt(len(customList)))
    max_value = max(customList)
    arr = []
    
    for i in range(numberOfBuckets):
        arr.append([])
        
    for j in customList:
        index_b = math.ceil(j* numberOfBuckets/max_value)
        arr[index_b -1].append(j)
    
    for i in range(numberOfBuckets):
        arr[i] = insertionSort(arr[i])
        
    k = 0
    for i in range(numberOfBuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k +=1
    return customList



# print(bucketSort(list))      


def merge(customList, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = customList[l+i]
    
    for j in range(0, n2):
        R[j] = customList[m+1+j]
    
    i = 0 
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            customList[k] = L[i]
            i += 1
        else:
            customList[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        customList[k] = L[i]
        i += 1
        k += 1
    
    while j < n2:
        customList[k] = R[j]
        j += 1
        k += 1
                
def mergeSort(customList,l,r):
    if l < r:
        m = (l+(r-1)) //2
        mergeSort(customList,l,m)                        
        mergeSort(customList,m+1,r)
        merge(customList,l,m,r)
    return customList


# print(mergeSort(list,0,5))             


def partition(customList, low, high):
    i = low - 1
    pivot = customList[high]
    for j in range(low,high):
        if customList[j] <= pivot:
            i += 1
            customList[i], customList[j] = customList[j], customList[i]
    customList[i+1], customList[high] = customList[high], customList[i+1]
    return (i+1)

def quickSort(customList, low, high):
    if low < high:
        pi = partition(customList, low, high)
        quickSort(customList, low, pi-1)
        quickSort(customList, pi+1, high)
        
        
        
# quickSort(list,0,8)
# print(list)        

def heapify(customList,n,i):
    smallest = i
    L = 2*i + 1
    R = 2*i +2                

    if L< n and customList[L] < customList[smallest]:
        smallest = L
    if R< n and customList[R] < customList[smallest]:
        smallest = R
    
    if smallest != i:
        customList[i],customList[smallest] = customList[smallest],customList[i]
        heapify(customList,n,smallest)
def heapSort(customList):
    n = len(customList)
    for i in range(int(n/2)-1, -1, -1):
        heapify(customList, n, i)
    
    for i in range(n-1,0,-1):
        customList[i], customList[0] = customList[0], customList[i]
        heapify(customList, i, 0)
    customList.reverse()
                        
heapSort(list)
print(list)                        
      
                