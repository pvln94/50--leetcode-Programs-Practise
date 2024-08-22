# Valid Anagram

def check(a,b):
    return sorted(a) == sorted(b)

if __name__ == "__main__":
    a = "gram"
    b = "arm"
    if(check(a,b)):
        print("It is valid Anagram")
    else:
        print("Not valid")