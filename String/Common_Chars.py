"""str1 = "geeksforgeeks"
str2 = "gemkstones"
str3 = "acknowledges"
str4 = "aguelikes"
str_new = ""
"""

str1 = "apple"
str2 = "oranges"
str_new = ""

for i in str1:
    if i in str2: #if i in str2 and i in str3 and i in str4:
        str_new += i

new_list = [c for c in str_new]
new_list = list(set(new_list))
print(new_list) # ['a', 'e']
