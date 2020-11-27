def reverse_words_in_sentence(sentence):
    arr = sentence.split(' ')
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return ' '.join(arr)


print(reverse_words_in_sentence('i like this program very much'))
