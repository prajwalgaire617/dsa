import time
def selection_sort(array):
   

    start_time=time.time()
    for step in range(len(array)):
        min_idx = step

        for i in range(step + 1, len(array)):
         
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])

    end_time=(time.time()-start_time)*1000
    return [array,end_time]

        
        
        
        