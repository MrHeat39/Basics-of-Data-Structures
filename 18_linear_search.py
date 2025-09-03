
def linearsearch(array , query):
    for index in range(0 , len(array)):
        if array[index] == query:
            return index
    return -1

grades = [3 , 34 ,35]
search = 34
result = linearsearch(grades, search)

if result == -1:
    print("Not found")
else:
    print("found")

 

