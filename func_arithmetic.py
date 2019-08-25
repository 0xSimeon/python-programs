# A program to compute the arithmetic mean of numbers provided by the user
def arithmetic_mean():
    
    a = [] # an emtpy list is created
    i = 0 #initialized i as zero, where  i is used to iterate
    num = int(input('How many numbers do you want to compute: ')) #asked the user for amount of number they want to compute for
    while i <num: #run the while loop till i(0 at this point) == num (number user specified in 'num' input)
        i +=1 # at first 0 +1, now i = 1. this continues till num user specified
        b = int(input('Enter the nth number: ' ))
# Converted i(int) to string 
        z = str(i) 
        print (str('#' + z ))
        a.append(b) #adds the num to the empty list created earlier
        ar = int(sum(a) / len(a))
        
    print('The Arithmetic mean is ', ar)
        
        
        

arithmetic_mean()


    

    
    
    
    
    

