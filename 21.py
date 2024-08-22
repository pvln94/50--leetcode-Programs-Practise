# Valid Palindrome 

def palindrome(l):
    a = str(l) # converts integer numbers group into strings
    if a == a[::-1]:
        return 1
    return 0

if __name__ == "__main__":    
    l = 123432
    r = palindrome(l)
    if(r):
        print("Yes")
    else:
        print("No")
        