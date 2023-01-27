#3 Unique elements 
def unique_elements(arr: list) -> list:
    i = []
    if len(arr) == len(set(arr)):
        i = []
    else:
        for a in arr:
            if arr.count(a) == 1:
                    i.append(a)
            else:
                    continue
    return i
result_3 = unique_elements(arr=[1, 2, 3, 2, 4, 5, 5])
print(result_3)