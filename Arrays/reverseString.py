def reverse_string(s: str) -> str:
    """
    Reverses the given string.
    
    Args:
        s (str): The string to be reversed.
    Returns:
        str: The reversed string.
        """
    if (s.length == 0 or s.length == 1 or type(s) != str):
         return "hmmm that's not good. It is either empty or just one character or not a string"
    reversed = []
    for i in range(len(s)-1, -1, -1):
         reversed.append(s[i])
    return "".join(reversed)

print(reverse_string("heellooo"))
    
        