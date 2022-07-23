#find distince b/w string programmer in give array, the programmer is give array can be jubmbled and rearranging the string should make string progreammer
e.g: pawxxxpoanw : distance is 3 as firs 3 char are paw and last 5 char can be rearrahced to get paw so the distace b/2 fist occurance and last occurance is 
3 

def programmerStrings(s):
    # Write your code here'
    temp ={'p':1 ,'a':1, 'w':1}
    #pppprogrammer
    #progrpammper
    chk = 'programmer'
    numchar = 0
    numnotprog = 0
    fndflg = 0
    dist_len = 0
    for i in range(len(s)):
        if s[i] in temp:
            fndflg = 0
            #print(s[i])
            temp[s[i]] -= 1
            #print(temp[s[i]])
            if temp[s[i]] == 0:
                temp.pop(s[i])
            if not temp:
                temp = {'p':1 ,'a':1, 'w':1}
                fndflg += 1
        else:
            if fndflg > 0:
                #fndflg = 0
                dist_len +=1
    return  dist_len         
    
print(programmerStrings('pawxxapazw'))
                
