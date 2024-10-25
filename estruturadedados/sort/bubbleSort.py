def bubble_sort(element):
    size = len(element)
    for k in range(size-1):
        for i in range(size-1):
            if element[i]> element[i+1]:
                temp = element[i]
                element[i] = element[i+1]
                element[i+1] = temp
if __name__ == "__main__":
    elements = [5,9,2,1,67,34,88,34]
    elements2 = [1,2,4]
    bubble_sort(elements2)
    bubble_sort(elements)
    print(elements,elements2)

def sort_elements(arr):
    length = len(arr)
    for k in range(length-1):
        for j in range(length-1):
            if arr[j]['transaction_amount'] > arr[j+1]['transaction_amount']:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j]= temp 
    return arr 


arr = [{'name':'cassiano','transaction_amount':400},{'name':'dhaval','transaction_amount':200},{'name':'katy','transaction_amount':800}]
print(sort_elements(arr))
