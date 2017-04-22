def is_palindrome(string):
    result = True
    str_len = len(string)
    for i in range(0, int(str_len/2)): # you need to check only half of the string
        if string[i] != string[str_len-i-1]:
            result = False
            break
    return result