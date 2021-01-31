def reverse_string_iterative(string):
    size = len(string)
    reversed = ''

    for i in range(size):
        reversed = string[i] + reversed
    
    return(reversed)

def reverse_string_recursive(string):
    if string == '':
        return string
    else:
        character = string[-1]
        string = string[:-1]
        return character + reverse_string_recursive(string)

print(reverse_string_iterative('This is a test'))
print(reverse_string_recursive('This is a test'))