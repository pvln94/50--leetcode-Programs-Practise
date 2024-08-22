# Palindrome Number

# generate all palindrome numbers less than a given number

def check(a):
    l = str(a)
    return l == l[::-1] 

def all_pallindromes(a):
    for i in range(1,a):
        if(check(i)):
            print(i,end=" ")
  
if __name__ == "__main__":
    a = 104
    
    print(all_pallindromes(a))




