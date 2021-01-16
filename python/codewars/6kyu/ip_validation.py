# https://www.codewars.com/kata/515decfd9dcfc23bb6000006
# IP Validation 

def is_valid_IP(strng) -> bool:
    def is_padded(x:str) -> bool:
        before = len(x) 
        after = len(str(int(x)))
        return before != after 
    def in_ranged(x:str) -> bool:
        return 0 <= int(x) <= 255
    
    def compose(func, var):
        return len(list(filter(func, var)))
    
    splitted = strng.split('.')
    if len(splitted) != 4: return False 
    if compose(str.isdigit, splitted) != 4: return False 
    if compose(in_ranged, splitted) != 4: return False
    if compose(is_padded, splitted): return False 
    return True