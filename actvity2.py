#XOR of even number is odd 
#XOR of even number is even 



def isEvenOdd(n):
    if(n^1 == n+1):
        return True
    else:
        return False
    

number = int(input("enter a number"))
if isEvenOdd(number):
    print(number, "is even")



else:
    print(number, "is a odd number")
