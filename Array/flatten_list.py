data = [1,2,3,[4],[5,[6]],7,[8,[9]]]

flat_data = []

def flatten_list(data):
  for element in data:
    if type(element) == list:
      flatten_list(element)
    else:
        flat_data.append(element)

flatten_list(data)

print(flat_data)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
