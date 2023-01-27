# Second largest element

def second_largest_element(arr_1: list) -> int:

    for a in arr_1:
        if a == max(arr_1):
            arr_1 == arr_1.remove(a)
    u = max(arr_1)
    return u


result_5 = second_largest_element(arr_1=[1, 2, 3, 2, 4, 5, 5, 99, 105, 267])
print(result_5)
