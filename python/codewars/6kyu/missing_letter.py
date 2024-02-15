# https://www.codewars.com/kata/5839edaa6754d6fec10000a2
# Find the missig letter 

def find_missing_letter(chars):
    for i, char in enumerate(chars[:-1]):
        next_char = chars[i+1]
        if ord(char) + 1 != ord(next_char):
            return chr(ord(char) + 1)
    return chr(ord(chars[-1])+1)