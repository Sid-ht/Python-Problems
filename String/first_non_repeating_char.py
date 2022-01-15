from collections import OrderedDict
def fun(str1):
    od = OrderedDict()
    for i in str1:
        if i not in od:
            od[i] = 1
        else:
            od[i] +=1
    for k, v in od.items():
        if v == 1:
            break
    return k

print(fun("GeeksforGeeks")) #k


def fun(str1):
    char = {}
    counts = []
    for i in str1:
        if i not in char:
            char[i] = 1
            counts.append(i)
        else:
            char[i] += 1
    
    for i in counts:
        if char[i] == 1:
            return i
    return None

print(fun("GeeksforGeeks")) #k

