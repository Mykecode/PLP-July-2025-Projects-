def data_structure_exercise():
    my_list = [ ]
    
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    my_list.append(40)
    print('Original List:',my_list)
    
    my_list[2] = 15
    print('After moldifying position 2:', my_list)
    
    my_list_extension = [50, 60, 70]
    my_list.extend(my_list_extension)
    print('After extension:', my_list)
    
    del my_list[-1]
    print('After deleting the last member:',my_list)
    
    my_list.sort()
    print('Sorting in ascending order:',my_list)
    
    index = my_list.index(60)
    print('Find index of a member:', index)
    
    
data_structure_exercise()