def reverse_string(sentence):
    arr = [c for c in sentence]
    start = 0
    end = len(sentence) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return ''.join(arr)


print(reverse_string("I'm Siddharth"))
