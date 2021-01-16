# https://www.codewars.com/kata/57814d79a56c88e3e0000786
# Simple Encryption #1 - Alternating Split


from itertools import zip_longest

def decrypt(encrypted_text, n):
    res = encrypted_text
    for _ in range(0, n):
        mid = len(res) // 2
        res = ''.join(map(lambda x: ''.join(x[::-1]), zip_longest(res[:mid], res[mid:], fillvalue='')))
    return res


def encrypt(text, n):
    res = text
    for _ in range(0, n):
        res = res[1::2] + res[0::2] 
    return res