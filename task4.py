def zeros(lst):
  
    i=0 
    j = 0 

    while j < len(lst):

        if lst[j] != 0:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1  
        j += 1  


my_list = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
zeros(my_list)
print(my_list)