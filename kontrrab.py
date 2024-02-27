def filter_strings():
    size = int(input("Введите размер массива строк: "))
    strings = []
    for i in range(size):
        string = input(f"Введите строку {i+1}: ")
        strings.append(string)
    new_strings = []
    for string in strings:
        if len(string) <= 3:
            new_strings.append(string)
    
    return new_strings
