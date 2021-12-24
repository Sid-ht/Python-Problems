str1 = "Geeks for Geeks"
str2 = "Learning from Geeks for Geeks"

str3 = ""

list1 = str1.split(" ")
list2 = str2.split(" ")
list3 = []

for i in list1:
    if i not in list2:
            list3.append(i)

for i in list2:
    if i not in list1:
        list3.append(i)

str3 = ' '.join([i for i in list3])
print(str3) #Learning from
