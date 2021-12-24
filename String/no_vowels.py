str1 = "welcome to geeksforgeeks"
new_list = ['a','e','i','o','u']

str_list =[i for i in str1]
no_vowels_list = []

for i in str_list:
    if i not in new_list:
        no_vowels_list.append(i)

new_str = ''.join([i for i in no_vowels_list])
print(new_str)
