#!/usr/bin/python3
#!/usr/bin/python3
def uppercase(str):
    uppercase_str = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            uppercase_str += chr(ord(i) - 32)
        else:
            uppercase_str += i
    print("{}".format(uppercase_str))
