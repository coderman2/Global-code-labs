i=0
while(i < 10):
    i = i + 1
    print(i)
    
print("\n")
    

i = 6
while( i < 19):
    i +=1
    print(i)
print("\n")
    

i = 12
while( i < 20-2):
    i +=2
    print(i)
    
def evens(num1,num2):
    i = num1
    if num1%2== 0:
        i = (num1+1) - 2
        
    
   while (i < num2-2):
      i+=2
       print (i)
    
    
print("\n")

num1= int(input("First number "))
num2 = int(input("Second number"))
Numbers = evens(num1,num2)
print(Numbers)


num1= int(input("First number "))
num2 = int(input("Second number"))
def reverse_evens(num1,num2):
    while (num2>num1):
        if num2%2==0:
            print(num2)
        num2 -=1
        
            
       
    
reverse_evens(num1,num2)
