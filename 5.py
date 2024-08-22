# String to Integer
s="123"
#s="abc"
try:
    r = int(s)
    print(r)
except ValueError:
    print("String is not valid integer")    