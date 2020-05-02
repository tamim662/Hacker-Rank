def count_substring(string, sub_string):
    str1=string
    str2=sub_string

    count=0
    ind=0

    occurrence=0
    i=0
    while(i<len(str1)):
        if(str1[i]==str2[ind]):
            count+=1
            i+=1
            ind+=1
            if count==len(str2):
                occurrence+=1
                index=str1.find(str2)
                str1=str1[0:index]+str1[index+1:]
                i=index
                ind=0
                count=0
        else:
            i+=1
    return occurrence


        
