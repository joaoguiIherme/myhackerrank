def count_substring(string, sub_string):
    i = 0
    for x in range(0, len(string) - len(sub_string) + 1):
        if string[x:x+len(sub_string)] == sub_string:
            i += 1
    return i
