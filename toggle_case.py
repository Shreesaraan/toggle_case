def toggle_case(strng):
    result=""
    for i in strng:
        asc = ord(i) ^ (1 << 5)
        result += chr(asc)
    return result


strng=input("Enter the String : ")
print(toggle_case(strng))