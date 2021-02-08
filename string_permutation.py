def permute(data, i, length): 
    #print('i before loop :',i)
    if i==length: 
        print(''.join(data) )
    else: 
        for j in range(i,length): 
            #print('i: ',i)
            #print('j: ',j)
            #print('before swap: ',data)
            #swap
            data[i], data[j] = data[j], data[i]
            #print('dataswap: ', data)
            #print('i+1: ', i+1)
            #fix and swap remaining string
            permute(data, i+1, length) 
            #backtracking to get original string
            data[i], data[j] = data[j], data[i]  
            #print('data afer i+1: ', data)
            #print('i after i+1: ', i)
            #print('j after i+1: ', j)


string = "ABC"
n = len(string) 
data = list(string) 
permute(data, 0, n)
