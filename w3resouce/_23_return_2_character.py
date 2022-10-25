def two_character(string, n):
    if (len(string) >= 2):
        return string[:2] * n
    else:
        return string * n


print(two_character("p", 3))
