def binarySearch(array, search , lowIndex , highIndex):
    
    while lowIndex <= highIndex:
        mid = lowIndex + (highIndex - lowIndex) // 2 # floor()

        if array[mid] == search:
            return mid 
        
        elif array[mid] < search:
            lowIndex = mid + 1 

        else:
            highIndex = mid - 1 
    return -1

grades = [10 , 12 , 14 , 15 , 17 , 19 , 20] #length = 7
search = 10 

result = binarySearch(grades, search, 0, len(grades) - 1)

if result == -1 :
    print("Not found")
else:
    print("found")

