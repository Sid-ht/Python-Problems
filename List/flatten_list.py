nested_list = [[1,2,3],[4,5,6],[7]]
flat_list = [x for y in nested_list for x in y]
print(flat_list)

#recursion
nested_list = [[1,2,3],[4,5,6],[7]]
flat_list = []

def flatten_list(nested_list):
    for i in nested_list:
        if type(i) == list:
            flatten_list(i)
        else:
            flat_list.append(i)
    return flat_list

print(flatten_list(nested_list))

#simple but not fast enough
nested_list = [[1,2,3],[4,5,6],[7]]
print(sum(nested_list,[])) #iterates over each and sum them
