def Insertion_Sort(array):
    '''
     Function to do insertion sort
     Traverse through 1 to len(arr) Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
    '''
    i=1
    for i in range(len(array)):
        j = i - 1
        temp = array[i]
        
        while j >= 0 and temp < array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = temp

    return array



if __name__=="__main__":
    print ( Insertion_Sort([8,4,23,42,16,15]))










