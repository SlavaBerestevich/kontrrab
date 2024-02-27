def filter_strings(array):
    new_array = []
    for string in array:
        if len(string) <= 3:
            new_array.append(string)
    return new_array