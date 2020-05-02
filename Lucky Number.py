# Unofficial

def luckyNumbers(a, b):
    
     
    def prime_num(num):
        if num > 1:

   
            for i in range(2,num):
                if (num % i) == 0:
                
                    return False
                    break
            else:

                return True
        

        else:

            return False
    def squre_num(num):
        sum=0
        for d in str(num):
            sum+=int(d)**2
        return sum

    half,temp=False,False
    count=0

    for i in range(a,b+1):
        sum_i=sum(map(int,str(i)))
        if(prime_num(sum_i)==True):
            half=True
            temp=prime_num(squre_num(i))
            if(half==temp):
                count+=1
            else:
                pass
        else:
            pass
        half,temp=False,False

    return count
