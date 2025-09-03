grades = [10, 20, 6, 20, 15, 5] 
print(grades)
# bubble sort algorithme
# 1) lenght for the array
length = len(grades)
# 2) loop on elements in array 
for index in range(0, length-1):
    for compare in range(0, length - index - 1):
        first = grades[compare]
        second = grades[compare + 1]
        if first > second:
            grades[compare] = second
            grades[compare + 1] = first


print(grades)