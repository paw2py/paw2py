#basic quick sort algo 
# pivote = last element of array
# check each value of array against pivote and split them into two array 
# itm_lower --> all that are lesser then pivote
# itm_greater --> all that are greated then pivote
# call the function in a recurresive fashion as we have to sort the itm_lower and itm_greater untill there are no more item in arr to sort

def quk_srt(seq):
    if len(seq) <=1:
        return seq
    else:
        pvt =  seq.pop()
        itm_greater = []
        itm_lower = []
        
        for val in seq:
            if val > pvt:
                itm_greater.append(val)
            else:
                itm_lower.append(val)
        
        return quk_srt(itm_lower) + [pvt] + quk_srt(itm_greater)
    
print(quk_srt([10,7,20,3,6,0,2,43,66,5,3,2,7]))

#out: [0, 2, 2, 3, 3, 5, 6, 7, 7, 10, 20, 43, 66]
