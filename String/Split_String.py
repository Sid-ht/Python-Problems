str = 'This is my world'
list1 = []
temp_string = ''

for c in str:
  if c == ' ':
    list1.append(temp_string)
    temp_string = ''
  else:
    temp_string += c

if temp_string:
  list1.append(temp_string)
  
print(list1)
 
