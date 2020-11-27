def swap_first_and_last_word(sentence):
    arr = sentence.split(' ')
    arr[0], arr[len(arr)-1] = arr[len(arr)-1], arr[0]

    return ' '.join(arr)


print(swap_first_and_last_word("Practice makes Perfect"))
